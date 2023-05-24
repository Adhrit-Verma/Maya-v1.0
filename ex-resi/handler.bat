@echo off
setlocal enabledelayedexpansion
set /A count=1
:ifelse
if %count%==1  (
    start load.bat 
    ping localhost -n 10 >nul
    goto ada_art
)
if %count%==2(
    echo hello
    ping localhost -n 20 >nul
    start terminate.bat
    )
:ada_art
set /a count+=1
start ada_ascii_art.bat
goto ifelse

:exit
exit /b



