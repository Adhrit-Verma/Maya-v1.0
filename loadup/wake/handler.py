import os
import time
import sys
import subprocess

class handler:

    def __init__(self):
        current_path = os.path.abspath(sys.argv[0])
        drive = os.path.splitdrive(current_path)[0]
        bat_content=f'''@echo off
        cd /d "%~dp0"
        echo Requesting administrator privileges...
        echo.
        :: Run Python script with elevated privileges
        powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c python script.py'"

        '''
        bat_file_path = rf'{drive}\A.D.A\A.D.A\loadup\wake\privilege.bat'
        self.write_bat_file(bat_file_path, bat_content)
        self.open_file(bat_file_path)

        self.load_cNd()

    """def temp_path(self):
        current_path = os.path.abspath(sys.argv[0])
        drive = os.path.splitdrive(current_path)[0]
        bat_content=f'''
        @echo off
        pause
        setx PATH "%PATH%;{drive}\A.D.A\A.D.A"
        pause
        handler.py
        '''
        bat_file_path = rf'{drive}\A.D.A\A.D.A\loadup\wake\set.bat'
        self.write_bat_file(bat_file_path, bat_content)
        self.open_file(bat_file_path)"""


    def write_bat_file(self,file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    def open_file(self,file_path):
        try:    
            subprocess.run(file_path, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the file: {e}")
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")
    
    def load_cNd(self):
        current_path = os.path.abspath(sys.argv[0])
        self.drive = os.path.splitdrive(current_path)[0]
        self.cmds=(f"{self.drive}/A.D.A/A.D.A/loadup/wake/art.bat","")
        self.execute()

    def execute(self):
        timeout_sec=10
        t=time.time()
        print(t)
        for item in self.cmds:
            (c)=item
            if "art.bat" in c:
                t=t-time.time()
                if t>=timeout_sec:
                    self.open_file(f"{self.drive}/A.D.A/A.D.A/loadup/wake/terminate.bat")
                    break
                else:
                    self.open_file(c)
            else:
                break

control=handler()