"""Archived reference spectra and pointwise comparisons with GNU Fortran."""
from pathlib import Path

import numpy as np
import pytest

from lowtran import spectrum
from lowtran._api import _simulate

DATA = Path(__file__).with_name('data')


def test_archived_vertical_spectrum():
    expected = np.loadtxt(DATA / 'testfort_trans.asc', skiprows=2)
    tx, _, wavelength, *_ = _simulate(8333, 33333, 500, model=5)
    np.testing.assert_allclose(wavelength * 1000, expected[:, 0], atol=0.051, rtol=0)
    np.testing.assert_allclose(tx[:, 8], expected[:, 1], atol=6e-6, rtol=0)


def test_archived_thermal_spectrum():
    expected = np.loadtxt(DATA / 'testfort_solarrad.asc', skiprows=2)
    tx, _, wavelength, _, _, _, _, radiance = _simulate(
        749.5, 1250, 13, model=0, itype=1, iemsct=1, im=1, ird1=1,
        h1=0.05, zmdl=0.05, range_km=0.05, p=949, t=283.8, wmol=[93.96] + [0] * 11,
    )
    np.testing.assert_allclose(wavelength * 1000, expected[:, 0], atol=0.052, rtol=0)
    np.testing.assert_allclose(tx[:, 8], expected[:, 1], atol=6e-6, rtol=0)
    np.testing.assert_allclose(radiance, expected[:, 2], atol=0, rtol=1e-3)


def _mwir_cases():
    with np.load(DATA / 'mwir_fortran.npz') as reference:
        wave = reference['wavenumber']
        for geometry, transmission in zip(reference['conditions'], reference['transmission']):
            model, itype, h1, h2, angle, distance = geometry
            label = f'model-{model:g}-type-{itype:g}-h1-{h1:g}-angle-{angle:g}'
            yield pytest.param(
                dict(model=int(model), itype=int(itype), h1=h1, h2=h2,
                     angle=angle, range_km=distance),
                wave, transmission, id=label,
            )


@pytest.mark.parametrize('conditions,wavenumber,expected', list(_mwir_cases()))
def test_mwir_against_fortran(conditions, wavenumber, expected):
    result = spectrum(3, 5, **conditions)
    np.testing.assert_array_equal(result.wavenumber_cm, wavenumber)
    range_geometry = conditions['itype'] == 2 and conditions['range_km'] and not conditions['angle']
    tolerance = 7e-5 if range_geometry else 3e-6
    np.testing.assert_allclose(result.transmission, expected, atol=tolerance, rtol=0)
