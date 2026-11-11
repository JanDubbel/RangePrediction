#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
echo 'RangePrediction LOWTRAN 7: EXPLICIT FULL RUN'
python3 lowtran_overnight_atlas.py --full "$@"
