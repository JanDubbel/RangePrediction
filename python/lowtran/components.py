"""Component transmittance spectra from LOWTRAN 7 (transmission-only mode).

The numerical kernel stores original Fortran TX(1:63) in each output row.
The H2O continuum stored at TX(5) includes TX(5), TX(9), TX(10)
continuum terms BEFORE they are converted to transmission factors.
After the transmission-only IEMSCT=0 branch, TX(7) additionally includes
cirrus TX(16), and TX(50) includes UV O2 TX(58).
TX(10) is transformed into 1 - aerosol absorption transmittance: it is
NOT a multiplicative transmittance channel at output.
"""
from dataclasses import dataclass
import numpy as np
from ._api import _simulate

# Original Fortran indices (1-based). Not all are used as distinct channels.
_NAMES = {
    "h2o_lines": (17,), "h2o_continuum": (5,),
    "co2": (36,), "o3": (31, 8),
    "aerosol_including_cirrus": (7,), "rayleigh": (6,),
    "n2_continuum": (4,), "hno3": (11,),
    "co": (44,), "ch4": (46,), "n2o": (47,), "o2": (50,),
    "nh3": (52,), "no": (54,), "no2": (55,), "so2": (56,),
}

@dataclass(frozen=True)
class ComponentSpectrum:
    wavenumber_cm: np.ndarray
    wavelength_um: np.ndarray
    total: np.ndarray
    components: dict[str, np.ndarray]
    h2o: np.ndarray
    other_gases: np.ndarray
    closure_error: float

    def sorted(self):
        ix=np.argsort(self.wavelength_um)
        return ComponentSpectrum(self.wavenumber_cm[ix], self.wavelength_um[ix],
                                 self.total[ix], {k:v[ix] for k,v in self.components.items()},
                                 self.h2o[ix],self.other_gases[ix],self.closure_error)


def components_spectrum(wl_min_um, wl_max_um, *, step_cm=20, **conditions):
    """Read genuine separately calculated LOWTRAN TX channels (not reruns with gases disabled).

    Keep IEMSCT=0 (transmission only); component definitions refer to
    original LOWTRAN source TRANS() and its TX array.
    """
    if conditions.get("iemsct",0) != 0:
        raise ValueError("components_spectrum requires IEMSCT=0")
    if not 0.2 <= wl_min_um < wl_max_um:
        raise ValueError("Invalid wavelength range")
    tx, v, lam, *_ = _simulate(10000/wl_max_um,10000/wl_min_um,step_cm,**conditions)
    comp={name:np.prod(tx[:,np.array(cols)-1].astype(np.float64),axis=1) for name,cols in _NAMES.items()}
    h2o=comp['h2o_lines']*comp['h2o_continuum']
    non_h2o=['co2','o3','n2_continuum','hno3','co','ch4','n2o','o2','nh3','no','no2','so2']
    other_gases=np.prod(np.array([comp[n] for n in non_h2o]),axis=0)
    reconstructed=h2o*comp['aerosol_including_cirrus']*comp['rayleigh']*other_gases
    err=float(np.max(np.abs(reconstructed-tx[:,8])))
    return ComponentSpectrum(v.copy(),lam.copy(),tx[:,8].astype(float).copy(),comp,
                             h2o,other_gases,err)
