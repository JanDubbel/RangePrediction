"""Safeguards for LOWTRAN component-spectrum export."""
import numpy as np
import pytest
from lowtran import Atmosphere

@pytest.mark.parametrize('profile,h1,h2',[(2,0,0),(2,0,3),(2,3,3),(3,0,0),(3,0,3),(3,3,3)])
def test_components_reconstruct_total(profile,h1,h2):
    atm=Atmosphere(profile=profile,aerosol=1,visibility_km=30)
    r=atm.spectrum_components(distance_km=20,altitude_start_km=h1,altitude_end_km=h2)
    original=atm.spectrum(distance_km=20,altitude_start_km=h1,altitude_end_km=h2)
    np.testing.assert_array_equal(r.wavelength_um, original.wavelength_um)
    np.testing.assert_allclose(r.total,original.transmission,atol=0,rtol=0)
    assert r.closure_error < 2e-7
    assert np.ptp(r.components['h2o_lines'])>0.1

def test_aerosol_switch_off():
    r=Atmosphere(profile=2,aerosol=0,visibility_km=30).spectrum_components(distance_km=20)
    np.testing.assert_allclose(r.components['aerosol_including_cirrus'],1.0)
