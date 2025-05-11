@echo off
pushd %~dp0

call venv\Scripts\activate.bat
python browser_use_agent.py

pause
