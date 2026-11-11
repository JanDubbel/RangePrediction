from pathlib import Path
import re
import sys
src = Path(sys.argv[1]).read_text()
statement = []
def flush():
    if not statement:
        return
    clean = lambda line: re.split(r"!(?=(?:[^']*'[^']*')*[^']*$)", line[6:], maxsplit=1)[0].rstrip()
    code = ' '.join(clean(line) for line in statement).strip()
    for mode in ('read', 'write', 'print', 'open', 'close', 'format', 'rewind', 'backspace'):
        match = re.match(rf"(?i)(?:if\s*\(.*\)\s*)?({mode})\b\s*[( *]", code)
        if match:
            label = statement[0][:5]
            if mode == 'read':
                print(label + " " + code[:match.start(1)] + "STOP 'TAPE5 input is outside the Python API'")
            elif label.strip():
                print(label + ' CONTINUE')
            break
    else:
        print('\n'.join(statement))
    statement.clear()
for line in src.splitlines():
    if not line.strip() or line[:1] in 'cC*!' or line.lstrip().startswith('!'):
        continue
    if line[5] == ' ':
        flush()
    statement.append(line)
flush()
