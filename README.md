# RangePrediction — atmospheric transmission research

This repository stores three related, but separately maintained results:

- [`fortran/`](fortran/) — LOWTRAN 7 Fortran source with an experimental stable-geometry patch.
- [`python/`](python/) — pure-Python LOWTRAN 7 port with the corresponding experimental geometry patch and per-component spectra.
- [`atlas/`](atlas/) — 4,962 Weibull fits from the original overnight LOWTRAN run.

**Important:** The existing fitted atlas was calculated **before** the geometry correction. Its slant-path short-range coefficients must not be treated as validated against the patched code. In particular, the original LOWTRAN geometry has a non-monotonicity near 2.5–3 km on some slant paths. The `atlas/weibull_profiles.csv` table is retained as a historical/reference analysis, not a corrected production atlas.

This project is an engineering/research approximation, not a validated replacement for atmospheric radiative-transfer simulation. See each folder's README for provenance, formulas, build instructions, and limitations.

## Units and model scope

The atlas fits energy-weighted, 283 K, 3–5 µm atmospheric transmittance with a flat spectral response:

`tau(D) = exp(-alpha * D**beta)`, with `D` in **km**.

No spectrally resolved output, alternate temperatures, or arbitrary detector spectral response can be recovered from these two coefficients alone.
