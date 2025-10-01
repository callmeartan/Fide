@echo off
REM FIDE Data Extractor GUI Launcher for Windows

cd /d "%~dp0"

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Launch GUI
python fide_gui.py

pause


