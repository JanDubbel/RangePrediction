@echo off
cd /d "%~dp0"
python lowtran_overnight_atlas.py --smoke %*
pause
