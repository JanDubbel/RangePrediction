import numpy as np
import pytest

from lowtran import Atmosphere, spectrum


def test_legacy_spectrum_unchanged_when_aerosols_off():
    args = dict(model=2, itype=1, h1=0, range_km=3)
    default = spectrum(3, 5, **args)
    explicit_off = spectrum(3, 5, ihaze=0, visibility_km=0, **args)
    np.testing.assert_array_equal(default.transmission, explicit_off.transmission)


def test_aerosol_extinction_increases_for_rural_case():
    no = Atmosphere(profile=2, aerosol=0).transmittance(distance_km=3)
    yes = Atmosphere(profile=2, aerosol=1, visibility_km=30).transmittance(distance_km=3)
    assert 0 <= yes.integral_transmission < no.integral_transmission <= 1


def test_profile_is_from_kernel():
    p = Atmosphere(profile=2, aerosol=1).atmospheric_profile()
    assert len(p.altitude_km) >= 20
    np.testing.assert_allclose(p.altitude_km[:4], [0, 1, 2, 3])
    assert 280 < p.temperature_k[0] < 310
    assert 900 < p.pressure_mbar[0] < 1100


def test_slant_and_error_checks():
    result = Atmosphere(profile=2, aerosol=1).transmittance(
        distance_km=10, altitude_start_km=0, altitude_end_km=3)
    assert 0 <= result.integral_transmission <= 1
    with pytest.raises(ValueError):
        Atmosphere(profile=2, aerosol=7)
    with pytest.raises(ValueError):
        Atmosphere().transmittance(distance_km=1, altitude_end_km=3)
