@echo off
pause
setx PATH "%PATH%;%~dp0"
py %~dp0handler.py
        