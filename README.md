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

## Geometry validation decision (2026-11-11)

The experimental stable-central-angle correction was compared across 270 original-Fortran, patched-Fortran, and patched-Python cases; the tested short slant-path non-monotonicities disappeared and the patched implementations agreed closely in integrated transmittance (reported maximum absolute difference approximately 1.5e-4).

For long slant paths around 60 km and above, the remaining difference between requested range and the ray-tracing output can reach a few hundred metres, partly associated with the refraction/geometry handling. For the intended engineering Weibull atlas this is **provisionally acceptable** as a range-scale approximation (roughly 0.3–0.5% for 200–300 m at 60 km); it is not a claim that the corresponding *transmittance* error is necessarily 0.3–0.5%, nor is it a validation of all LOWTRAN geometry modes. The long-range residual remains a documented limitation rather than a blocker for work on the atlas.

Do **not** overwrite the existing pre-fix atlas with patched-model values until the replacement dataset and fitting pipeline have been independently checked. The full overnight dataset rerun is **on hold pending explicit user authorization**.
