"""Small runtime for the generated numerical kernel."""
import math
from pathlib import Path

import numpy as np

_array = np.array
_zeros = np.zeros
_f32 = np.float32
_f64 = np.float64
_c64 = np.complex64
_ZERO32 = _f32(0)
_ZERO64 = _f64(0)
_initial_state = Path(__file__).with_name('_tables.bin').read_bytes()


class LowtranError(ValueError):
    """LOWTRAN could not evaluate the requested conditions."""


class State:
    """Private working copy of Fortran's shared arrays and saved variables."""

    def __init__(self):
        self.memory = bytearray(_initial_state)
        self.views = {}

    def view(self, offset, dtype):
        key = (offset, dtype)
        if key not in self.views:
            kind = np.dtype(dtype)
            size = (len(self.memory) - offset) // kind.itemsize
            self.views[key] = np.frombuffer(self.memory, kind, size, offset)
        return self.views[key]


def _int(value):
    if isinstance(value, (float, np.floating)) and not np.isfinite(value):
        return -2147483648
    return int(value)


def _div(left, right):
    if isinstance(left, (int, np.integer)) and isinstance(right, (int, np.integer)):
        left, right = int(left), int(right)
        quotient = abs(left) // abs(right)
        return -quotient if (left < 0) != (right < 0) else quotient
    return left / right


def _read_char(array, index):
    return array.view('u1')[index]


def __builtin_memmove(destination, source, size):
    destination.view('u1')[:size] = source.view('u1')[:size].copy()


def _gfortran_stop_string(message, size, quiet):
    raise LowtranError(message[:size].decode('ascii').strip())


def _gfortran_stop_numeric(code, quiet):
    raise LowtranError(f'LOWTRAN stopped with status {code}')


def _gfortran_random_r4(destination):
    destination[0] = np.random.default_rng().random(dtype=_f32)


def __complex__(real, imag):
    return _c64(complex(real, imag))


_real = np.real
_imag = np.imag
__builtin_sqrtf = np.sqrt
__builtin_sqrt = np.sqrt
def _single_precision(function, fallback):
    # Double evaluation followed by rounding tracks the Fortran scalar
    # intrinsics more closely near refractive tangent-point boundaries.
    def evaluate(*arguments):
        try:
            return _f32(function(*arguments))
        except (OverflowError, ValueError):
            return fallback(*arguments)
    return evaluate


__builtin_powf = _single_precision(math.pow, np.power)
__builtin_expf = _single_precision(math.exp, np.exp)
__builtin_exp = np.exp
__builtin_logf = _single_precision(math.log, np.log)
__builtin_log10f = _single_precision(math.log10, np.log10)
__builtin_cosf = np.cos
__builtin_cos = np.cos
__builtin_sinf = np.sin
__builtin_sin = np.sin
__builtin_tanf = np.tan
__builtin_atanf = np.arctan
__builtin_asinf = np.arcsin
__builtin_acosf = np.arccos
__builtin_acos = np.arccos
__builtin_fmodf = np.fmod


def __builtin_powif(base, exponent):
    return np.power(_f32(base), int(exponent))


__all__ = [
    name for name in globals()
    if name.startswith(('__builtin_', '_gfortran_')) or name in {
        '__complex__', '_array', '_zeros', '_f32', '_f64', '_c64',
        '_ZERO32', '_ZERO64', '_int', '_div', '_read_char', '_real', '_imag',
    }
]
