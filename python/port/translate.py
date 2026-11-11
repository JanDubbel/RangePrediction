"""Translate the lowered LOWTRAN statements into Python control flow."""
import keyword
import re
import sys
from pathlib import Path

from elftools.elf.elffile import ELFFile


TYPES = r'(?:real|integer|unsigned integer|logical|complex|character)\(kind=\d+\)|bitsizetype|sizetype'
NAME = r'[a-zA-Z_][a-zA-Z_0-9.]*'
DECL = re.compile(rf'(static )?({TYPES})(\[[^\]]+\])?\s+([*&]?)(?:restrict )?({NAME})(\[[^\]]+\])?(\[[^\]]+\])?(?: \[value-expr: (.*?)\])?(?: = (.*))?;')
NUMBER = r'(?:\d+\.\d*(?:e[+-]?\d+)?|\d+)(?:B)?'
IDENT = re.compile(rf'^({NAME})(?:\[(.*?)\])?$')
TOK = re.compile(rf'"(?:\\.|[^"\\])*"|{NUMBER}|{NAME}|\S')


def split_args(text):
    level = 0
    start = 0
    for match in TOK.finditer(text):
        token = match[0]
        if token in ('(', '[', '{'):
            level += 1
        elif token in (')', ']', '}'):
            level -= 1
        elif token == ',' and level == 0:
            yield text[start:match.start()].strip()
            start = match.end()
    if text[start:].strip():
        yield text[start:].strip()


def dtype(spec, char_size=1):
    if spec.startswith('character'):
        return f'S{char_size}'
    if spec.startswith('complex'):
        return '<c8'
    if spec.startswith('real'):
        return '<f' + spec[-2]
    if spec.startswith('integer'):
        return '<i' + spec[-2]
    if spec.startswith('logical'):
        return '<i4'
    return '<i8'


def py(name):
    clean = name.replace('.', '_')
    if keyword.iskeyword(clean) or clean in {'abs', 'max', 'min', 'int', 'float', 'bool', 'complex', 'bytes', 'str'}:
        return 'v_' + clean
    return clean


def address(die):
    location = die.attributes.get('DW_AT_location')
    if location and location.form == 'DW_FORM_exprloc':
        loc = bytes(location.value)
        if len(loc) == 9 and loc[0] == 3:
            return int.from_bytes(loc[1:], 'little')


def dname(die):
    name = die.attributes.get('DW_AT_name')
    return name.value.decode() if name else ''


def static_image(elf, out):
    # Writable numeric initializers and zero-initialized work areas.
    data = elf.get_section_by_name('.data')
    bss = elf.get_section_by_name('.bss')
    start = data['sh_addr']
    image = bytearray(bss['sh_addr'] + bss['sh_size'] - start)
    image[:data['sh_size']] = data.data()
    # The linker reserves the first eight bytes for its own data-start pointer.
    image[:8] = bytes(8)
    (out / '_tables.bin').write_bytes(image)
    return start


class Routine:
    def __init__(self, signature, lines, locations, common, image_start, functions):
        match = re.fullmatch(rf'(void|{TYPES}) ({NAME}) \((.*)\)', signature)
        self.return_type, self.name, params = match.groups()
        self.functions = functions
        self.locations = locations.get(self.name, {})
        self.common = common
        self.image_start = image_start
        self.params = []
        self.vars = {}
        self.globals = {}
        self.boxed = set()
        self.code = []
        struct = False
        for arg in split_args(params):
            self.params.append(arg.rsplit(' ', 1)[-1])
        for line in lines:
            line = line.strip()
            if line in ('static union', 'static union {'):
                struct = True
            if struct:
                if line.startswith('} equiv.'):
                    struct = False
                continue
            if not line or line in ('{', '}', 'else', 'try', 'finally') or line.startswith('//'):
                continue
            if (decl := DECL.fullmatch(line)):
                self.declare(*decl.groups())
                continue
            if line.endswith('= {CLOBBER};') or line.endswith('= {CLOBBER(eos)};'):
                continue
            self.code.append(line)
        for line in self.code:
            for var in re.findall(r'&(' + NAME + ')', line):
                if var in self.vars and not self.vars[var][1] and var not in self.globals:
                    self.boxed.add(var)

    def declare(self, static, spec, pre, pointer, name, count, char, alias, value):
        if spec.startswith('character'):
            char_shape = char or count or pre
            if char_shape and ':' in char_shape:
                char_size = int(char_shape[3:-1])
                if char_shape == count:
                    count = None
                elif char_shape == pre:
                    pre = None
            else:
                char_size = 1
            kind = dtype(spec, char_size)
        else:
            kind = dtype(spec)
        count = int(count[1:-1]) if count and count[1:-1].isdigit() else None
        self.vars[name] = (kind, count, bool(pointer or pre), value)
        if alias:
            loc = self.locations.get(name, self.common.get(alias))
            if loc is None:
                raise ValueError((self.name, name, alias))
            self.globals[alias] = (loc, kind, count is not None)
        elif static and name in self.locations:
            self.globals[name] = (self.locations[name], kind, count is not None)

    def reference(self, expr, target=False, addr=False):
        char = re.fullmatch(r'(.*)\[(.*?)\]\{lb: \d+ sz: \d+\}', expr)
        if char:
            base, char_index = char.groups()
            ref = self.reference(base, addr=True)
            return f'_read_char({ref}, {self.expr(char_index)} - 1)' if not target else f'{ref}.view("u1")[{self.expr(char_index)} - 1]'
        match = re.fullmatch(rf'\(\*({NAME})\)\[(.*?)\]', expr)
        if match:
            name, index = match.groups()
            return self.array(py(name), index, addr)
        if expr.startswith("(*") and expr.endswith(")"):
            return self.reference(expr[1:-1], target, addr)
        if expr.startswith('*'):
            p = py(expr[1:])
            return p if addr else p + '[0]'
        match = IDENT.fullmatch(expr)
        if not match:
            raise ValueError(f'unknown reference {expr}')
        name, index = match.groups()
        p = py(name)
        if index is not None:
            return self.array(p, index, addr)
        if addr:
            if name in self.params and name not in self.vars:
                raise ValueError(f'address of parameter {name}')
            return p
        if name in self.boxed or name in self.globals and not self.globals[name][2]:
            return p + '[0]'
        return p

    def array(self, name, index, addr):
        i = self.expr(index)
        return f'{name}[{i}:]' if addr else f'{name}[{i}]'

    def expr(self, value, target=False):
        if value.startswith('((') and value.endswith('))'):
            return self.expr(value.strip('()'))
        if value.startswith('&"'):
            return 'b' + TOK.findall(value)[1]
        if value.startswith('&'):
            return self.reference(value[1:], addr=True)
        if value.startswith('"'):
            return 'b' + value
        cast = re.fullmatch(rf'\(({TYPES})\) (.*)', value)
        if cast:
            spec, operand = cast.groups()
            converter = {'<f4': '_f32', '<f8': '_f64', '<i4': '_int', '<i8': '_int', '<c8': '_c64'}[dtype(spec)]
            return f'{converter}({self.expr(operand)})'
        gcc_expr = re.fullmatch(r'([A-Z_]+)_EXPR <(.*)>', value)
        if gcc_expr:
            op, args = gcc_expr.groups()
            helper = {'MIN': 'min', 'MAX': 'max', 'ABS': 'abs', 'IMAGPART': '_imag', 'REALPART': '_real', 'COMPLEX': '__complex__'}[op]
            return f'{helper}({", ".join(self.expr(a) for a in split_args(args))})'
        call = re.fullmatch(rf'({NAME}) \((.*)\)', value)
        if call:
            name, args = call.groups()
            translated = [self.expr(arg) for arg in split_args(args)]
            if name in self.functions:
                return f'_ft_{name}(_state{", " if translated else ""}{", ".join(translated)})'
            return f'{name}({", ".join(translated)})'
        if re.fullmatch('-?' + NUMBER, value):
            return value.removesuffix('B')
        binary = re.fullmatch(r'(.*?) ([-+*/%|&^]|==|!=|[<>]=?|<<|>>) (.*)', value)
        if binary:
            left, op, right = binary.groups()
            a, b = self.expr(left), self.expr(right)
            return f'_div({a}, {b})' if op == '/' else f'{a} {op} {b}'
        if value.startswith('-'):
            return '-' + self.expr(value[1:])
        if value.startswith('~'):
            op = '~' if value[1:].startswith('stride.') else 'not '
            return op + self.expr(value[1:])
        if value.startswith('!'):
            return 'not ' + self.expr(value[1:])
        return self.reference(value, target)

    def setup(self):
        used = set(re.findall(NAME, '\n'.join(self.code)))
        for name, (loc, kind, _) in self.globals.items():
            if name in used:
                yield f'{py(name)} = _state.view({loc - self.image_start}, {kind!r})'
        for name, (kind, count, pointer, value) in self.vars.items():
            if name not in used or name in self.globals or name in self.params or pointer:
                continue
            v = py(name)
            if name in self.boxed or count is not None or kind.startswith('S'):
                if value is not None:
                    if value.startswith('{'):
                        if re.fullmatch(r'\{\[0 \.\.\. \d+\]=0\.0\}', value):
                            value = None
                        else:
                            parts = list(split_args(value[1:-1]))
                            value = ', '.join(self.expr(item.split('=')[-1]) for item in parts)
                    else:
                        value = self.expr(value)
                if value is None:
                    yield f'{v} = _zeros({count or 1}, {kind!r})'
                else:
                    yield f'{v} = _array([{value}], {kind!r})'
            elif value is not None:
                yield f'{v} = {self.coerce(kind, self.expr(value))}'
            else:
                zero = {'<f4': '_ZERO32', '<f8': '_ZERO64', '<c8': '_c64(0)'}.get(kind, '0')
                yield f'{v} = {zero}'

    @staticmethod
    def coerce(kind, expr):
        converter = {'<f4': '_f32', '<f8': '_f64', '<i4': '_int', '<i8': '_int', '<c8': '_c64'}.get(kind)
        return f'{converter}({expr})' if converter else expr

    def blocks(self):
        blocks = [('entry', [])]
        for line in self.code:
            if line.endswith(':'):
                label = line[:-1]
                blocks.append((label, []))
            else:
                blocks[-1][1].append(line)
                if line.startswith(('goto ', 'if (', 'return', 'switch ')):
                    blocks.append((f'continuation_{len(blocks)}', []))
        # Map consecutive labels to the next non-empty block.
        dest = {}
        for label, body in reversed(blocks):
            if body:
                next_block = label
            dest[label] = locals().get('next_block', None)
        active = [(label, body) for label, body in blocks if body]
        ids = {label: i for i, (label, _) in enumerate(active)}
        return active, {label: ids.get(to, -1) for label, to in dest.items()}

    def statements(self, block, labels):
        for line in block:
            if line.startswith('if ('):
                match = re.fullmatch(r'if \((.*?)\) goto (.*?); else goto (.*?);', line)
                test, yes, no = match.groups()
                yield f'_pc = {labels[yes]} if {self.expr(test)} else {labels[no]}'
                yield 'continue'
            elif line.startswith('goto '):
                yield f'_pc = {labels[line[5:-1]]}'
                yield 'continue'
            elif line.startswith('switch '):
                match = re.fullmatch(r'switch \((.*?)\) <default: ([^,]+), (.*)>', line)
                key, default, cases = match.groups()
                table = {}
                for case in cases.split(', '):
                    selector, label = re.fullmatch(r'case (.*?): (.*)', case).groups()
                    if ' ... ' in selector:
                        low, high = map(int, selector.split(' ... '))
                        table.update(dict.fromkeys(range(low, high + 1), labels[label]))
                    else:
                        table[int(selector)] = labels[label]
                yield f'_pc = {table}.get({self.expr(key)}, {labels[default]})'
                yield 'continue'
            elif line.startswith('return'):
                yield 'return' if line == 'return;' else 'return ' + self.expr(line[7:-1])
            elif ' = ' in line:
                lhs, rhs = line[:-1].split(' = ', 1)
                target = self.expr(lhs, target=True)
                expr = self.expr(rhs)
                if lhs in self.vars and lhs not in self.globals and lhs not in self.boxed and '[' not in target:
                    kind, _, ptr, _ = self.vars[lhs]
                    if not ptr:
                        expr = self.coerce(kind, expr)
                yield f'{target} = {expr}'
            elif line.endswith(';'):
                yield self.expr(line[:-1])
            else:
                raise ValueError(f'unrecognized line: {line}')

    def emit(self):
        active, labels = self.blocks()
        yield f'def _ft_{self.name}(_state{", " if self.params else ""}{", ".join(map(py, self.params))}):'
        for line in self.setup():
            yield '    ' + line
        if len(active) == 1:
            for line in self.statements(active[0][1], labels):
                yield '    ' + line
            return
        yield '    _pc = 0'
        yield '    while True:'
        yield '        match _pc:'
        for number, (label, block) in enumerate(active):
            yield f'            case {number}:  # {label}'
            for line in self.statements(block, labels):
                yield '                ' + line
            if not block[-1].startswith(('goto ', 'return', 'if (', 'switch ')):
                yield f'                _pc = {number + 1}' if number + 1 < len(active) else '                return'
        yield "            case -1: return"
        yield "            case _: raise RuntimeError('Invalid LOWTRAN control flow')"


def main():
    out = Path(sys.argv[1])
    with Path('port.so').open('rb') as file:
        elf = ELFFile(file)
        image_start = static_image(elf, out)
        locations = {}
        common = {}
        for unit in elf.get_dwarf_info().iter_CUs():
            for routine in unit.get_top_DIE().iter_children():
                if routine.tag != 'DW_TAG_subprogram':
                    continue
                slots = locations.setdefault(dname(routine), {})
                for child in routine.iter_children():
                    if child.tag == 'DW_TAG_common_block':
                        for var in child.iter_children():
                            if (loc := address(var)) is not None:
                                name = dname(var)
                                slots[name] = loc
                                common[f'{dname(child)}.{name}'] = loc
                    elif child.tag == 'DW_TAG_variable' and (loc := address(child)) is not None:
                        slots[dname(child)] = loc
    source = next(Path('.').glob('port.so*.gimple')).read_text()
    routines = re.findall(r'^(void [^\n]*|(?:real|integer)\(kind=\d+\) [^\n]*)\n\{\n(.*?)^\}', source, re.M | re.S)
    functions = {sig.split(' ')[1] for sig, _ in routines}
    with (out / '_core.py').open('w') as result:
        result.write('"""Generated Python port of LOWTRAN 7. See README.md for provenance."""\n')
        result.write('from ._runtime import *\n\n')
        for sig, body in routines:
            try:
                routine = Routine(sig, body.splitlines(), locations, common, image_start, functions)
                result.write('\n'.join(routine.emit()) + '\n\n\n')
            except Exception as err:
                raise RuntimeError(sig) from err


if __name__ == '__main__':
    main()
