import json
import os
import sys
import geocoder

class SystemInfo:
    def __init__(self):
        self.current_path = os.path.abspath(sys.argv[0])
        self.drive = os.path.splitdrive(self.current_path)[0]
        self.json_file_path = rf'{self.drive}\A.D.A\A.D.A\loadup\utils\system_info.json'
        
    def load_system_info(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, 'r') as file:
                data = json.load(file)
            return data
        else:
            return None

    def get_system_info(self, requested_info=None):
        data = self.load_system_info()
        if data:
            info_string = ""
            info_string += f"OS Name: {data['os_name']}\n"
            info_string += f"OS Version: {data['os_version']}\n\n"

            info_string += f"Hostname: {data['hostname']}\n\n"

            cpu_info = data['cpu_info']
            info_string += f"CPU Count: {cpu_info['cpu_count']}\n"
            info_string += f"CPU Threads: {cpu_info['cpu_threads']}\n"
            info_string += f"CPU Usage: {cpu_info['cpu_usage']}\n\n"

            memory_info = data['memory_info']
            total_memory = memory_info.get('total_memory(MB)', 'Unknown')
            available_memory = memory_info.get('available_memory(MB)', 'Unknown')
            info_string += f"Total Memory (MB): {total_memory}\n"
            info_string += f"Available Memory (MB): {available_memory}\n\n"

            disk_info = data['disk_info']
            total_space = disk_info.get('total_space(MB)', 'Unknown')
            free_space = disk_info.get('free_space(MB)', 'Unknown')
            info_string += f"Total Space (MB): {total_space}\n"
            info_string += f"Free Space (MB): {free_space}\n\n"

            drive_info = data['drive_info']
            info_string += f"Number of Drives: {drive_info['num_drives']}\n\n"

            pc_location = data['pc_location']
            latitude = pc_location.get('latitude')
            longitude = pc_location.get('longitude')
            if latitude and longitude:
                location = geocoder.osm([latitude, longitude], method='reverse')
                if location.ok:
                    info_string += f"Location: {location.city}, {location.state}, {location.country}\n[NOTE][!]: Location could be wrong due to device type & OS build\n\n"
                else:
                    info_string += "Location: Unknown\n"
            else:
                info_string += "Location: Unknown\n"

            is_connected = data.get('internet_info', {}).get('is_connected', False)
            info_string += f"Internet Connection: {'✓' if is_connected else '✗'}\n"

            mic_info = data.get('mic_info', {}).get('is_available', False)
            info_string += f"Mic Availability: {'✓' if mic_info else '✗'}\n"

            device_info = data.get('device_info', {})
            device_type = device_info.get('device_type')
            device_category = device_info.get('device_category')

            if device_type and device_category:
                info_string += f"Device Type: {device_type}\n"
                info_string += f"Device Category: {device_category}\n"
            else:
                info_string += "Device Type: Unknown\n"
                info_string += "Device Category: Unknown\n"

            if requested_info:
                if requested_info == 'device':
                    return f"Device Type: {device_type}\nDevice Category: {device_category}"
                elif requested_info == 'cpu':
                    return f"CPU Count: {cpu_info['cpu_count']}\nCPU Threads: {cpu_info['cpu_threads']}\nCPU Usage: {cpu_info['cpu_usage']}"
                elif requested_info == 'memory':
                    return f"Total Memory (MB): {total_memory}\nAvailable Memory (MB): {available_memory}"
                else:
                    return "Invalid requested information."
            else:
                print(info_string)
                return f"Here's the info of {data['hostname']}'s {device_category}"
        else:
            return "System info JSON file not found."


