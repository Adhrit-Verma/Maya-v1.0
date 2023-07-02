
        @echo off
        set "usb_drive="
        set "set_bat_executed=0"

        :loop
        cls
        echo Detecting USB drives...

        for /f "tokens=1,2" %%A in ('powershell -Command "Get-WmiObject Win32_Volume | Where-Object {$_.DriveType -eq 2 -and $_.Label -eq 'MAYA'} | Select-Object -Property DriveLetter, Label | Format-Table -AutoSize -HideTableHeaders"') do (
            if not defined usb_drive (
                echo MAYA drive found: %%A
                set "usb_drive=%%A"
            )
        )

        if defined usb_drive (
            if %set_bat_executed% equ 0 (
                echo Changing current directory to %usb_drive%...
                cd /d %usb_drive%
                if not errorlevel 1 (
                    echo Current directory changed to %usb_drive% successfully.
                    echo Locating and running set.bat...
                    cd A.D.A\A.D.A\loadup\wake
                    if exist set.bat (
                        echo set.bat found. Running set.bat...
                        start "" /b set.bat
                        set "set_bat_executed=1"
                    ) else (
                        echo set.bat not found in the specified location.
                    )
                ) else (
                    echo Failed to change current directory to %usb_drive%.
                )
            ) else (
                echo set.bat has already been executed. Waiting for USB drive to be unplugged...
                if not exist %usb_drive%\ (
                    echo USB drive has been unplugged. Resetting...
                    set "usb_drive="
                    set "set_bat_executed=0"
                )
            )
        ) else (
            echo MAYA drive not found. Waiting for USB drive to be plugged in...
            set "set_bat_executed=0"
        )

        timeout /t 5 >nul
        goto loop
        