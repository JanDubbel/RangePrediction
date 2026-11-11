from __future__ import annotations
from typing import Any

import numpy as np

from ._api import _point_count, _simulate


def check():
    """Return the Python numerical backend."""
    from . import _api
    return _api


def nm2lt7(short_nm: float, long_nm: float, step_cminv: float = 20) -> tuple[float, float, float]:
    """converts wavelength in nm to cm^-1
    minimum meaningful step is 20, but 5 is minimum before crashing lowtran

    short: shortest wavelength e.g. 200 nm
    long: longest wavelength e.g. 30000 nm
    step: step size in cm^-1 e.g. 20

    output in cm^-1
    """
    short = 1e7 / short_nm
    long = 1e7 / long_nm

    return short, long, _point_count(long, short, step_cminv)


def loopuserdef(c1: dict[str, Any]):
    """
    golowtran() is for scalar parameters only
    (besides vector of wavelength, which Lowtran internally loops over)

    wmol, p, t must all be vector(s) of same length
    """

    import xarray

    wmol = np.atleast_2d(c1["wmol"])
    P = np.atleast_1d(c1["p"])
    T = np.atleast_1d(c1["t"])
    time = np.atleast_1d(c1["time"])

    assert (
        wmol.shape[0] == len(P) == len(T) == len(time)
    ), "WMOL, P, T,time must be vectors of equal length"

    N = len(P)
    # %% 3-D array indexed by metadata
    TR = xarray.Dataset(coords={"time": time, "wavelength_nm": None, "angle_deg": None})

    for i in range(N):
        c = c1.copy()
        c["wmol"] = wmol[i, :]
        c["p"] = P[i]
        c["t"] = T[i]
        c["time"] = time[i]

        TR = TR.merge(golowtran(c), join="outer", compat="no_conflicts")

    #   TR = TR.sort_index(axis=0) # put times in order, sometimes CSV is not monotonic in time.

    return TR


def loopangle(c1: dict[str, Any]):
    """
    loop over "ANGLE"
    """
    import xarray

    angles = np.atleast_1d(c1["angle"])
    TR = xarray.Dataset(coords={"wavelength_nm": None, "angle_deg": angles})

    for a in angles:
        c = c1.copy()
        c["angle"] = a
        TR = TR.merge(golowtran(c), join="outer", compat="no_conflicts")

    return TR


def golowtran(c1: dict[str, Any]):
    """Run LOWTRAN and return the original xarray Dataset."""
    import xarray

    wlshort, wllong, _ = nm2lt7(c1["wlshort"], c1["wllong"], c1.get("wlstep", 20))
    defaults = {
        "h1": 0, "h2": 0, "angle": 0, "im": 0, "iseasn": 0, "ird1": 0,
        "range_km": 0, "zmdl": 0, "p": 0, "t": 0, "wmol": (0,) * 12,
    }
    conditions = {name: c1.get(name, default) for name, default in defaults.items()}
    for name in ("model", "itype", "iemsct"):
        conditions[name] = c1[name]
    tx, _, alam, _, _, _, irrad, sumvv = _simulate(
        wllong, wlshort, c1.get("wlstep", 20), **conditions,
    )
    dims = ("time", "wavelength_nm", "angle_deg")
    return xarray.Dataset(
        {
            "transmission": (dims, tx[:, 8][None, :, None]),
            "radiance": (dims, sumvv[None, :, None]),
            "irradiance": (dims, irrad[:, 0][None, :, None]),
            "pathscatter": (dims, irrad[:, 2][None, :, None]),
        },
        coords={
            "time": [c1.get("time")],
            "wavelength_nm": alam * 1e3,
            "angle_deg": [conditions["angle"]],
        },
    )
