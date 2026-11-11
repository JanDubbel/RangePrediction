# Pure-Python LOWTRAN 7 (patched geometry)

`lowtran/` is the Python numerical port with the component-resolved spectra and the same local stable-central-angle geometry change as `../fortran/`.

Dependencies: Python >= 3.10, NumPy, optional Matplotlib / pytest for plots and tests.

From inside `python/`:

```bash
python -m pip install -e .
python -m pytest -q tests
```

Example:

```python
from lowtran import Atmosphere
atm = Atmosphere(profile=2, aerosol=1, visibility_km=30)
result = atm.transmittance(
    distance_km=2.5, altitude_start_km=0, altitude_end_km=1,
    wavelength_range=(3, 5), background_temp_k=283)
print(result.integral_transmission)
```

The patch is in `lowtran/_core.py`, inside the generated routine `_ft_geoinp`. The source replacement uses double-precision `math.asin(math.sqrt(...))` before storing `float32`, like the Fortran fix. **Regenerating** `_core.py` from an unpatched Fortran file will erase the fix; regenerate from the *patched* Fortran source or port the same change again.

`lowtran/_tables.bin` is required by the numerical runtime and must be included. This fork is experimental and is not formally validated for every LOWTRAN geometry. Comparisons against original and patched Fortran have been performed for representative slant cases only.
