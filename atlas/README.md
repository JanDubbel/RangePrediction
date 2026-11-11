# Weibull fit atlas (pre-geometry-fix)

`weibull_profiles.csv` contains 4,962 records. Each record describes a specific combination of:

- `profile`: LOWTRAN standard atmospheric model (1–6),
- `aerosol`: LOWTRAN aerosol setting (0/1/4/5/6),
- `visibility_km`: meteorological visibility (km),
- `h1_km`, `h2_km`: ends of the atmospheric path (km).

`alpha_clean`, `beta_clean` fit the weighted integral transmittance at 283 K (3–5 µm, unit detector response) via:

`tau(D_km) = exp(-alpha_clean * D_km ** beta_clean)`.

The word `clean` **does not mean these coefficients were fitted to corrected LOWTRAN**. It only means a suspicious 2.5 km slant-path point was excluded from that fitting stage. Other short-range geometry errors may persist, so these are **research coefficients only** until the affected samples are recomputed.

Extra columns include fit RMSE, short/long-range comparison, and an experimental three-term model `exp(-alpha_3term*D**beta_3term - linear_3term*D)`. `rmse_long5plus` measures the fit on D>=5 km.

No tests of interpolation between unseen atmospheric and height profiles are included here. The source database is *not* committed (hundreds of megabytes); this directory stores the compact fitted coefficients and analysis provenance.
