@echo off
        cd /d "%~dp0"
        echo Requesting administrator privileges...
        echo.
        :: Run Python script with elevated privileges
        powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c python script.py'"

        