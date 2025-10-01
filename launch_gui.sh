#!/bin/bash

# FIDE Data Extractor GUI Launcher

cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

# Launch GUI
python fide_gui.py


