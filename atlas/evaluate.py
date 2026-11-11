"""Load the empirical Weibull atlas and evaluate an existing fitted curve.

This does not interpolate across meteorological conditions or fix historic
LOWTRAN 7 slant-path geometry artifacts. See README.md.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

TABLE = Path(__file__).with_name("weibull_profiles.csv")


def load_profiles(path: Path = TABLE) -> list[dict]:
    """Return the table as dictionaries (numeric fields converted to float)."""
    with path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    return [
        {
            key: (float(val) if key not in ("profile", "aerosol", "bad_at_2p5") else int(val))
            for key, val in row.items()
        }
        for row in rows
    ]


def transmittance(distance_km: float, alpha: float, beta: float) -> float:
    if distance_km < 0 or alpha < 0 or beta <= 0:
        raise ValueError("Expect distance >= 0, alpha >= 0, beta > 0")
    return math.exp(-alpha * distance_km**beta)


if __name__ == "__main__":
    atlas = load_profiles()
    print(f"Loaded {len(atlas)} fitted curves")
    row = atlas[0]
    print("First curve at D=10 km:", transmittance(10, row["alpha_clean"], row["beta_clean"]))
