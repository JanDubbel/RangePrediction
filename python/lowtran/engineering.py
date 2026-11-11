"""Engineering-friendly MWIR interface for the native Python LOWTRAN 7 port.

No Fortran compiler is required. NumPy is needed for calculations; Matplotlib
is needed only when calling plot_* functions.
"""
from dataclasses import dataclass
from typing import Optional

import numpy as np

from ._api import spectrum as _spectrum, _simulate

PROFILE_NAMES = {
    1: 'Tropical',
    2: 'Midlatitude summer',
    3: 'Midlatitude winter',
    4: 'Subarctic summer',
    5: 'Subarctic winter',
    6: 'US Standard Atmosphere 1976',
}
AEROSOL_NAMES = {
    0: 'No aerosols',
    1: 'Rural (default visibility 23 km)',
    2: 'Rural (default visibility 5 km)',
    4: 'Maritime (default visibility 23 km)',
    5: 'Urban (default visibility 5 km)',
    6: 'Tropospheric (default visibility 50 km)',
    8: 'Advection fog (default visibility 0.2 km)',
    9: 'Radiation fog (default visibility 0.5 km)',
}


def _planck_wavelength(wavelength_um, temperature_k):
    """Relative Planck spectral radiance per wavelength, sufficient for weighting."""
    lam = np.asarray(wavelength_um, dtype=np.float64)
    c2_um_k = 14387.768775039337
    return 1.0 / (lam**5 * np.expm1(c2_um_k / (lam * temperature_k)))


@dataclass(frozen=True)
class TransmissionResult:
    wavelength_um: np.ndarray
    spectral_transmission: np.ndarray
    integral_transmission: float
    distance_km: float
    background_temp_k: float


@dataclass(frozen=True)
class AtmosphericProfile:
    altitude_km: np.ndarray
    pressure_mbar: np.ndarray
    temperature_k: np.ndarray


@dataclass(frozen=True)
class Atmosphere:
    """Standard LOWTRAN atmosphere, with optional LOWTRAN boundary-layer aerosols.

    profile: 1..6, the standard MODEL number.
    aerosol: supported IHAZE values (not arbitrary integers).
    visibility_km: 0/None selects the IHAZE default; otherwise sets VIS.
    season: 0 automatic, 1 spring/summer, 2 autumn/winter (ISEASN).
    """
    profile: int = 2
    aerosol: int = 1
    visibility_km: Optional[float] = 30.0
    season: int = 0

    def __post_init__(self):
        if self.profile not in PROFILE_NAMES:
            raise ValueError(f'profile must be one of {list(PROFILE_NAMES)}')
        if self.aerosol not in AEROSOL_NAMES:
            raise ValueError(f'aerosol must be one of {list(AEROSOL_NAMES)}; other IHAZE modes require additional inputs')
        if self.season not in (0, 1, 2):
            raise ValueError('season must be 0, 1, or 2')
        if self.visibility_km is not None and (not np.isfinite(self.visibility_km) or self.visibility_km <= 0):
            raise ValueError('visibility_km must be positive, or None for the aerosol default')

    def _conditions(self):
        return dict(model=self.profile, ihaze=self.aerosol,
                    visibility_km=self.visibility_km or 0,
                    iseasn=self.season)

    @staticmethod
    def _geometry(distance_km, altitude_start_km, altitude_end_km):
        values = (distance_km, altitude_start_km, altitude_end_km)
        if not np.isfinite(values).all() or distance_km <= 0 or min(values[1:]) < 0:
            raise ValueError('Distance must be positive and altitudes nonnegative and finite')
        if distance_km < abs(altitude_end_km - altitude_start_km):
            raise ValueError('Slant range cannot be shorter than the altitude difference')
        if altitude_start_km == altitude_end_km:
            return dict(itype=1, h1=altitude_start_km, range_km=distance_km)
        return dict(itype=2, h1=altitude_start_km, h2=altitude_end_km,
                    range_km=distance_km, angle=0)

    def spectrum(self, *, distance_km, altitude_start_km=0, altitude_end_km=0,
                 wavelength_range=(3.0, 5.0), step_cm=20):
        """Native LOWTRAN spectrum on a uniform wavenumber grid."""
        low, high = wavelength_range
        if not 0.2 <= low < high:
            raise ValueError('Invalid wavelength_range in micrometres')
        return _spectrum(low, high, step_cm=step_cm,
                         **self._conditions(),
                         **self._geometry(distance_km, altitude_start_km, altitude_end_km))

    def spectrum_components(self, *, distance_km, altitude_start_km=0, altitude_end_km=0,
                            wavelength_range=(3.0, 5.0), step_cm=20):
        """Separately calculated spectral H2O, CO2, O3, aerosol etc. transmission.

        Note: for 3--5 um, the product of physical components reconstructs
        LOWTRAN total transmission (up to numerical roundoff).
        """
        from .components import components_spectrum
        low, high = wavelength_range
        return components_spectrum(low, high, step_cm=step_cm,
                                   **self._conditions(),
                                   **self._geometry(distance_km, altitude_start_km, altitude_end_km))

    def transmittance(self, *, distance_km, altitude_start_km=0, altitude_end_km=0,
                      wavelength_range=(3.0, 5.0), background_temp_k=283.0,
                      step_cm=20):
        """Planck-weighted band transmission, with S(lambda)=1.

        Values at exact wavelength endpoints are linearly interpolated from
        the LOWTRAN output grid. A detector-specific response is not included.
        """
        if not np.isfinite(background_temp_k) or background_temp_k <= 0:
            raise ValueError('background_temp_k must be positive')
        sp = self.spectrum(distance_km=distance_km,
                           altitude_start_km=altitude_start_km,
                           altitude_end_km=altitude_end_km,
                           wavelength_range=wavelength_range, step_cm=step_cm)
        order = np.argsort(sp.wavelength_um)
        w = np.asarray(sp.wavelength_um[order], dtype=np.float64)
        tau = np.asarray(sp.transmission[order], dtype=np.float64)
        lo, hi = wavelength_range
        # LOWTRAN may round the first/last spectral sample beyond the requested band.
        # Request one extra margin in spectral calculations to ensure interpolation
        # is bracketed on both sides; otherwise reject unbracketed boundaries.
        if w[0] > lo + 1e-7 or w[-1] < hi - 1e-7:
            raise ValueError('LOWTRAN output does not bracket the requested band endpoints')
        interior = (w > lo) & (w < hi)
        ww = np.r_[lo, w[interior], hi]
        tt = np.r_[np.interp(lo, w, tau), tau[interior], np.interp(hi, w, tau)]
        weights = _planck_wavelength(ww, background_temp_k)
        integrated = float(np.trapezoid(tt * weights, ww) / np.trapezoid(weights, ww))
        return TransmissionResult(w, tau, integrated, float(distance_km), background_temp_k)

    def atmospheric_profile(self):
        """Return actual standard temperature and pressure arrays used by LOWTRAN."""
        (_, state) = _simulate(2000, 2020, model=self.profile,
                               itype=1, h1=0.0, range_km=1.0,
                               ihaze=self.aerosol,
                               visibility_km=self.visibility_km or 0,
                               iseasn=self.season, _return_state=True)
        levels = int(state.view(245616, '<i4')[0])
        if not 2 <= levels <= 33:
            raise RuntimeError(f'Invalid number of LOWTRAN atmospheric levels: {levels}')
        return AtmosphericProfile(
            state.view(231904, '<f4')[:levels].copy(),
            state.view(232040, '<f4')[:levels].copy(),
            state.view(232176, '<f4')[:levels].copy(),
        )

    def plot_profile(self, *, max_altitude_km=30, axes=None):
        """Plot actual standard pressure and temperature vs height."""
        import matplotlib.pyplot as plt
        data = self.atmospheric_profile()
        mask = data.altitude_km <= max_altitude_km
        if axes is None:
            fig, axes = plt.subplots(1, 2, figsize=(9, 5), sharey=True)
        else:
            fig = axes[0].figure
        axes[0].plot(data.temperature_k[mask] - 273.15, data.altitude_km[mask])
        axes[0].set(xlabel='Temperature (°C)', ylabel='Altitude (km)', title='Temperature')
        axes[1].plot(data.pressure_mbar[mask], data.altitude_km[mask])
        axes[1].set(xlabel='Pressure (mbar)', title='Pressure')
        axes[1].set_xscale('log')
        for ax in axes:
            ax.grid(True, alpha=.25)
        fig.tight_layout()
        return fig, axes

    def plot_transmittance(self, distances_km, *, altitude_start_km=0,
                           altitude_end_km=0, background_temp_k=283,
                           wavelength_range=(3, 5), step_cm=20, ax=None):
        """Plot Planck-weighted integrated transmittance vs slant range."""
        import matplotlib.pyplot as plt
        distances = np.asarray(distances_km, dtype=float)
        if distances.ndim != 1 or len(distances) == 0:
            raise ValueError('distances_km must be a nonempty 1D sequence')
        taus = [self.transmittance(
            distance_km=float(d), altitude_start_km=altitude_start_km,
            altitude_end_km=altitude_end_km,
            background_temp_k=background_temp_k,
            wavelength_range=wavelength_range, step_cm=step_cm,
        ).integral_transmission for d in distances]
        if ax is None:
            fig, ax = plt.subplots(figsize=(7, 4))
        else:
            fig = ax.figure
        ax.plot(distances, taus, marker='o', markersize=3)
        ax.set(xlabel='Slant range (km)', ylabel='Integrated transmission',
               title=f'LOWTRAN 7, MODEL={self.profile}, IHAZE={self.aerosol}')
        ax.set_ylim(bottom=0)
        ax.grid(True, alpha=.25)
        fig.tight_layout()
        return fig, ax

    def plot_spectrum(self, *, distance_km, altitude_start_km=0,
                      altitude_end_km=0, wavelength_range=(3, 5), ax=None):
        import matplotlib.pyplot as plt
        sp = self.spectrum(distance_km=distance_km,
                           altitude_start_km=altitude_start_km,
                           altitude_end_km=altitude_end_km,
                           wavelength_range=wavelength_range)
        if ax is None:
            fig, ax = plt.subplots(figsize=(7, 4))
        else:
            fig = ax.figure
        ix = np.argsort(sp.wavelength_um)
        ax.plot(sp.wavelength_um[ix], sp.transmission[ix])
        ax.set(xlabel='Wavelength (µm)', ylabel='Spectral transmission',
               title=f'LOWTRAN 7, range={distance_km:g} km', ylim=(0, 1))
        ax.grid(True, alpha=.25)
        fig.tight_layout()
        return fig, ax
