import os
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
        self.cmds=f"{self.drive}/A.D.A/A.D.A/loadup/wake/art.bat"
        self.execute()

    def execute(self):
        if "art.bat" in self.cmds:
            self.open_file(self.cmds)

control=handler()