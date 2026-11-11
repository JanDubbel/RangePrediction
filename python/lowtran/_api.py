"""Array input and output for the LOWTRAN kernel."""
from dataclasses import dataclass

import numpy as np

from ._core import _ft_lwtrn7
from ._runtime import LowtranError, State


def _run(kernel, nwl, v1, v2, dv, model, itype, iemsct, im, iseasn,
         ird1, zmdl, p, t, wmol, h1, h2, angle, range_km, ihaze=0, visibility_km=0.0, return_state=False):
    zmdl, p, t = (np.atleast_1d(np.asarray(a, dtype=np.float32)) for a in (zmdl, p, t))
    wmol = np.asarray(wmol, dtype=np.float32)
    if not (zmdl.ndim == p.ndim == t.ndim == 1 and len(zmdl) == len(p) == len(t)):
        raise ValueError('zmdl, p and t must have the same number of atmospheric levels')
    if wmol.shape != (12,):
        raise ValueError('wmol must contain 12 molecular inputs')

    tx = np.zeros((nwl, 63), np.float32, order='F')
    v, alam, trace, unif, suma, sumvv = np.zeros((6, nwl), np.float32)
    irrad = np.zeros((nwl, 3), np.float32, order='F')

    def integer(value):
        return np.array([value], dtype=np.int32)

    def real(value):
        return np.array([value], dtype=np.float32)

    args = (
        integer(1), integer(nwl), real(v1), real(v2), real(dv),
        tx.ravel(order='F'), v, alam, trace, unif, suma, irrad.ravel(order='F'),
        sumvv, integer(model), integer(itype), integer(iemsct), integer(im),
        integer(iseasn), integer(len(zmdl)), integer(ird1), zmdl, p, t, wmol,
        real(h1), real(h2), real(angle), real(range_km),
    )
    with np.errstate(all='ignore'):
        kernel(*args, ihaze=ihaze, visibility_km=visibility_km)
    result = (tx, v, alam, trace, unif, suma, irrad, sumvv)
    return (result, kernel) if return_state else result


def _point_count(v1, v2, dv):
    """Mirror the original bounds and step rounding before allocating arrays."""
    if not np.isfinite([v1, v2, dv]).all() or not 0 <= v1 <= v2 <= 50000 or not 5 <= dv <= 50000:
        raise ValueError('Use 0 <= v1 <= v2 <= 50000 and 5 <= dv <= 50000 cm^-1')

    def snap(value):
        return 5 * int(np.float32(value) / 5 + np.float32(0.1))

    low, high, step = map(snap, (v1, v2, dv))
    return (high - low + step - 1) // step + 1


def _simulate(v1, v2, dv=20, *, model=5, itype=3, iemsct=0, im=0,
              iseasn=0, ird1=0, zmdl=0, p=0, t=0, wmol=(0,) * 12,
              h1=0, h2=0, angle=0, range_km=0, ihaze=0, visibility_km=0,
              _return_state=False):
    nwl = _point_count(v1, v2, dv)
    if model not in range(8) or itype not in (1, 2, 3) or iemsct not in (0, 1, 2, 3):
        raise ValueError('Invalid LOWTRAN model, path type or calculation mode')
    if model == 0 and (itype != 1 or im != 1 or np.size(zmdl) != 1):
        raise ValueError('Model 0 requires a horizontal path and one atmospheric level')
    if model == 7 and (im != 1 or not 2 <= np.size(zmdl) <= 33):
        raise ValueError('Model 7 requires 2 to 33 supplied atmospheric levels')
    if iemsct == 3 and itype != 3:
        raise ValueError('Direct solar irradiance requires a path to space')
    if not np.isfinite([h1, h2, angle, range_km]).all() or not 0 <= angle <= 180 or range_km < 0:
        raise ValueError('Use finite geometry, a zenith angle of 0 to 180 degrees and a nonnegative range')
    # IHAZE=3 needs marine wind/air-mass controls; 7 uses additional cards;
    # 10 requires wind controls.  Expose only self-contained built-in modes.
    if ihaze not in (0, 1, 2, 4, 5, 6, 8, 9):
        raise ValueError('Supported aerosol IHAZE values: 0, 1, 2, 4, 5, 6, 8, 9')
    if not np.isfinite(visibility_km) or visibility_km < 0:
        raise ValueError('visibility_km must be finite and nonnegative (0 = model default)')
    state = State()
    result = _run(
        lambda *args, **kwargs: _ft_lwtrn7(state, *args, **kwargs),
        nwl, v1, v2, dv, model, itype, iemsct, im, iseasn, ird1,
        zmdl, p, t, wmol, h1, h2, angle, range_km, ihaze, visibility_km,
    )
    tx, v, alam, trace, unif, suma, irrad, sumvv = result
    if not alam.any():
        raise LowtranError('LOWTRAN did not return a spectrum for this geometry')
    if iemsct not in (1, 2):
        sumvv.fill(0)
    if iemsct != 2:
        irrad[:, 2] = 0
    if iemsct != 3:
        irrad[:, :2] = 0
    return (result, state) if _return_state else result


@dataclass(frozen=True)
class Spectrum:
    wavenumber_cm: np.ndarray
    wavelength_um: np.ndarray
    transmission: np.ndarray
    radiance: np.ndarray
    irradiance: np.ndarray
    pathscatter: np.ndarray


def spectrum(wl_min_um, wl_max_um, *, step_cm=20, **conditions):
    """Calculate a spectrum using µm, cm⁻¹, km, degrees, mbar and K."""
    if not np.isfinite([wl_min_um, wl_max_um]).all() or not 0.2 <= wl_min_um <= wl_max_um:
        raise ValueError('Use 0.2 <= wl_min_um <= wl_max_um')
    tx, v, alam, _, _, _, irrad, sumvv = _simulate(
        1e4 / wl_max_um, 1e4 / wl_min_um, step_cm, **conditions,
    )
    return Spectrum(v, alam, tx[:, 8], sumvv, irrad[:, 0], irrad[:, 2])


def lwtrn7(python, nwl, v1, v2, dv, model, itype, iemsct, im,
           iseasn, ird1, zmdl, p, t, wmol, h1, h2, angle, range_km):
    """Compatibility entry point for callers of check().lwtrn7()."""
    if not python:
        raise ValueError('Use Python inputs for lwtrn7')
    result = _simulate(
        v1, v2, dv, model=model, itype=itype, iemsct=iemsct, im=im,
        iseasn=iseasn, ird1=ird1, zmdl=zmdl, p=p, t=t, wmol=wmol,
        h1=h1, h2=h2, angle=angle, range_km=range_km,
    )
    if len(result[1]) != nwl:
        raise ValueError(f'For the effective spectral grid, use nwl={len(result[1])}')
    return result
