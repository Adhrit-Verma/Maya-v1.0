@echo off

>nul chcp 65001
set "_spc=                    "
set "_bar=■■■■■■■■■■■■■■■■■■■■"

setlocal enabledelayedexpansion

for /f %%a in ('copy /Z "%~dpf0" nul') do for /f "skip=4" %%b in ('echo;prompt;$H^|cmd') do set "BS=%%~b" & set "CR=%%a"

set /a "total=20"
set /a "progress=0"

for /L %%L in (1,1,%total%) do (
    set /a "progress=%%L * 100 / %total%"
    <con: set /p "'=!CR!!BS!!CR![!_bar:~0,%%L!!_spc:~%total%,%total%!] " <nul
    call :updateProgress !progress!
    ping -n 2 127.0.0.1 >nul
    cls
)

endlocal & goto :eof

:updateProgress
echo %1%%%
exit /b
