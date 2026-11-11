"""Regression for the formerly non-monotonic 2.5 -> 3 km slant case."""

import numpy as np

from lowtran import Atmosphere


def test_short_slant_geometry_is_monotonic():
    atm = Atmosphere(profile=2, aerosol=1, visibility_km=30)
    distances = [2.0, 2.5, 3.0, 4.0]
    vals = [
        atm.transmittance(
            distance_km=d,
            altitude_start_km=0,
            altitude_end_km=1,
            wavelength_range=(3, 5),
            background_temp_k=283,
        ).integral_transmission
        for d in distances
    ]
    assert all(a > b for a, b in zip(vals, vals[1:])), vals
    np.testing.assert_allclose(vals, [0.4015086, 0.3624481, 0.3303447, 0.2803442], atol=1e-4, rtol=0)
