@echo off
cd /d "%~dp0"
echo RangePrediction LOWTRAN 7: EXPLICIT FULL RUN
python lowtran_overnight_atlas.py --full %*
if errorlevel 1 (
  echo.
  echo ERROR: see console output or worker_errors.log
  pause
)
