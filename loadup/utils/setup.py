import winreg,shutil,getpass
import sys
import os
import subprocess

class ClientSetup:
    def __init__(self):
        current_path = os.path.abspath(sys.argv[0])
        drive = os.path.splitdrive(current_path)[0]
        bat_content ='''
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
        '''
            
        bat_file_path = rf'{drive}\A.D.A\A.D.A\loadup\utils\invoker.bat'
        self.write_bat_file(bat_file_path, bat_content)
        self.ask_to_run(bat_file_path)
        self.add_to_startup(bat_file_path)

    def write_bat_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    def ask_to_run(self, file_path):
        response = input("Do you want to start the file now? (Y/N): ")
        if response.upper() == 'Y':
            self.run_file(file_path)
            
        else:
            self.add_to_startup(file_path)
            self.exit()

    def run_file(self, file_path):
        try:
            subprocess.run(file_path, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the file: {e}")
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")

    def add_to_startup(self, file_path):
        username = getpass.getuser()
        startup_folder = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        target_path = os.path.join(startup_folder, 'invoker.bat')
        
        try:
            shutil.copy(file_path, target_path)
            print("Added invoker.bat to startup.")
        except Exception as e:
            print(f"Error adding invoker.bat to startup: {e}")

        """key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, "ADA Invoker", 0, winreg.REG_SZ, file_path)
        winreg.CloseKey(key)"""

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    cs = ClientSetup()
