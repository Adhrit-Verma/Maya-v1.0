import os
import sys
import subprocess
import platform
import socket
import psutil
import json
import threading
import geocoder


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

    def gather_system_info(self):
        system_info = {}

        # Get OS information
        system_info['os_name'] = platform.system()
        system_info['os_version'] = platform.release()

        # Get hostname
        system_info['hostname'] = socket.gethostname()

        # Get CPU information
        cpu_info = {}
        cpu_info['cpu_count'] = psutil.cpu_count(logical=False)
        cpu_info['cpu_threads'] = psutil.cpu_count(logical=True)
        cpu_info['cpu_usage'] = psutil.cpu_percent(interval=1)
        system_info['cpu_info'] = cpu_info

        # Get memory information
        memory_info = {}
        memory_info['total_memory'] = psutil.virtual_memory().total
        memory_info['available_memory'] = psutil.virtual_memory().available
        system_info['memory_info'] = memory_info

        # Get disk information
        disk_info = {}
        disk_usage = psutil.disk_usage('/')
        disk_info['total_space(MB)'] = disk_usage.total // (1024 * 1024)
        disk_info['free_space(MB)'] = disk_usage.free // (1024 * 1024)
        system_info['disk_info'] = disk_info

        # Get number of drives
        drive_info = {}
        drives = psutil.disk_partitions(all=True)
        drive_info['num_drives'] = len(drives)
        system_info['drive_info'] = drive_info

        # Get PC location
        pc_location = {}
        location = geocoder.ip('me').latlng
        pc_location['latitude'] = location[0] if location else 'Unknown'
        pc_location['longitude'] = location[1] if location else 'Unknown'
        system_info['pc_location'] = pc_location

        file_path = rf'{self.drive}\A.D.A\A.D.A\loadup\utils\system_info.json'
        with open(file_path, 'w') as file:
            json.dump(system_info, file, indent=4)

    
    def load_cNd(self):
        current_path = os.path.abspath(sys.argv[0])
        self.drive = os.path.splitdrive(current_path)[0]
        self.cmds = f"{self.drive}/A.D.A/A.D.A/loadup/wake/art.bat"

        gather_thread = threading.Thread(target=self.gather_system_info)
        execute_thread = threading.Thread(target=self.execute)

        gather_thread.start()
        execute_thread.start()

        gather_thread.join()
        execute_thread.join()

    def execute(self):
        if "art.bat" in self.cmds:
            self.open_file(self.cmds)

control=handler()