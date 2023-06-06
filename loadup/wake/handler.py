import geocoder
import json
import os
import platform
import psutil
import socket
import subprocess
import sys
import threading
import speech_recognition as sr


class SystemInfoGatherer:

    def __init__(self, drive):
        self.drive = drive

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
        memory_usage = psutil.virtual_memory()
        memory_info['total_memory(MB)'] = memory_usage.total // (1024 * 1024)
        memory_info['available_memory(MB)'] = memory_usage.available // (1024 * 1024)
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

        # Check internet connection
        internet_info = {}
        internet_info['is_connected'] = self.check_internet_connection()
        system_info['internet_info'] = internet_info

        # Check device
        device_info = {}
        device_type = platform.machine()
        device_info['device_type'] = device_type

        pc_machine_types = ['AMD64', 'x86_64']
        laptop_machine_types = ['i386', 'i686']

        if device_type in pc_machine_types:
            device_info['device_category'] = 'PC'
        elif device_type in laptop_machine_types:
            device_info['device_category'] = 'Laptop'
        else:
            device_info['device_category'] = 'Unknown'

        system_info['device_info'] = device_info


        # Check microphone availability
        mic_info = {}
        mic_info['is_available'] = self.check_microphone_availability()
        system_info['mic_info'] = mic_info

        file_path = rf'{self.drive}\A.D.A\A.D.A\loadup\utils\system_info.json'
        with open(file_path, 'w') as file:
            json.dump(system_info, file, indent=4)

    def check_internet_connection(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False

    def check_microphone_availability(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                r.adjust_for_ambient_noise(source)
                return True
            except sr.RequestError:
                return False


class handler:

    def __init__(self):
        current_path = os.path.abspath(sys.argv[0])
        drive = os.path.splitdrive(current_path)[0]
        bat_content = '''@echo off
        cd /d "%~dp0"
        echo Requesting administrator privileges...
        echo.
        :: Run Python script with elevated privileges
        powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c py "%~dp0..\engine.py"'"

        '''
        bat_file_path = rf'{drive}\A.D.A\A.D.A\loadup\wake\privilege.bat'
        self.write_bat_file(bat_file_path, bat_content)

        self.load_cNd()

    def write_bat_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    def Run_file(self, file_path):
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
        drive = os.path.splitdrive(current_path)[0]

        gatherer = SystemInfoGatherer(drive)
        gather_thread = threading.Thread(target=gatherer.gather_system_info)
        execute_thread = threading.Thread(target=self.execute)

        gather_thread.start()
        execute_thread.start()

        gather_thread.join()
        execute_thread.join()

    def execute(self):
        current_path = os.path.abspath(sys.argv[0])
        drive = os.path.splitdrive(current_path)[0]

        cmds = f"{drive}/A.D.A/A.D.A/loadup/wake/art.bat"
        self.Run_file(cmds)
        cmds = f"{drive}/A.D.A/A.D.A/loadup/wake/privilege.bat"
        self.Run_file(cmds)
        
        


control = handler()
