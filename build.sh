#!/bin/bash
# This is a script to pack the app into a single executable file located in ./dist and copy there related configuration files
pyinstaller --onefile ./run.py
cp ./cameraControls.tsv ./dist/
