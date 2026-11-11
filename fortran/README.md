# Experimental geometry fix for LOWTRAN 7 (Fortran)

Files:

- `lowtran7_stable_beta.f`: complete LOWTRAN 7 Fortran source with one local numerical change.
- `lowtran7_stable_beta.patch`: unified diff relative to `lowtran7.f` from the `space-physics/lowtran` source snapshot used for testing.
- `test_driver.f90`: small example using the `LWTRN7` call interface.

The original Fortran expression in `GEOINP` (CASE 2C, given H1/H2/RANGE) computes `BETA = PHI + ANGLE - 180.` with single-precision cancellation for short slant paths. The patch calculates the same geometric central angle from the chord length with double-precision intermediate arithmetic:

`beta_rad = 2 * asin(sqrt(max(0, (D**2-(H2-H1)**2)/(4*(R_earth+H1)*(R_earth+H2)))))`

**Important:** This is a *local experimental fix*, not a fully validated correction for every geometry/mode. Refraction iteration remains unchanged. We did not modify the atmospheric absorption coefficients or physical model.

Fortran compiler: gfortran (legacy fixed-form source). In an environment with gfortran:

```sh
gfortran -std=legacy -ffixed-line-length-none -c lowtran7_stable_beta.f
```

For standalone sample comparison with the provided driver:

```sh
gfortran -std=legacy -ffixed-line-length-none lowtran7_stable_beta.f test_driver.f90 -o lowtran_sample
```

The driver writes a spectral CSV and is **not** an exhaustive regression suite. Additional input cards / file paths may be required by other execution modes.

Upstream code reference: https://github.com/space-physics/lowtran . The `space-physics/lowtran` repository includes licensing / attribution for its LOWTRAN distribution. Original LOWTRAN credits are preserved in the Fortran source.
