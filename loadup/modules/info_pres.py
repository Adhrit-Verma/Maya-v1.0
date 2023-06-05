import json
import os
import sys
import geocoder

def present_data():
    current_path = os.path.abspath(sys.argv[0])
    drive = os.path.splitdrive(current_path)[0]
    json_file_path = rf'{drive}\A.D.A\A.D.A\loadup\utils\system_info.json'

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        print(f"OS Name: {data['os_name']}")
        print(f"OS Version: {data['os_version']}\n")

        print(f"Hostname: {data['hostname']}\n")

        cpu_info = data['cpu_info']
        print(f"CPU Count: {cpu_info['cpu_count']}")
        print(f"CPU Threads: {cpu_info['cpu_threads']}")
        print(f"CPU Usage: {cpu_info['cpu_usage']}\n")

        memory_info = data['memory_info']
        total_memory = memory_info.get('total_memory(MB)', 'Unknown')
        available_memory = memory_info.get('available_memory(MB)', 'Unknown')
        print(f"Total Memory (MB): {total_memory}")
        print(f"Available Memory (MB): {available_memory}\n")

        disk_info = data['disk_info']
        total_space = disk_info.get('total_space(MB)', 'Unknown')
        free_space = disk_info.get('free_space(MB)', 'Unknown')
        print(f"Total Space (MB): {total_space}")
        print(f"Free Space (MB): {free_space}\n")

        drive_info = data['drive_info']
        print(f"Number of Drives: {drive_info['num_drives']}\n")

        pc_location = data['pc_location']
        latitude = pc_location.get('latitude')
        longitude = pc_location.get('longitude')
        if latitude and longitude:
            location = geocoder.osm([latitude, longitude], method='reverse')
            if location.ok:
                print(f"Location: {location.city}, {location.state}, {location.country}\n[NOTE][!]: Location could be wrong due to device type & OS build\n")
            else:
                print("Location: Unknown")
        else:
            print("Location: Unknown")

        is_connected = data.get('internet_info', {}).get('is_connected', False)
        print(f"Internet Connection: {'✓' if is_connected else '✗'}")

        mic_info = data.get('mic_info', {}).get('is_available', False)
        print(f"Mic Availability: {'✓' if mic_info else '✗'}")

        device_info = data.get('device_info', {})
        device_type = device_info.get('device_type')
        device_category = device_info.get('device_category')

        if device_type and device_category:
            print(f"Device Type: {device_type}")
            print(f"Device Category: {device_category}")
        else:
            print("Device Type: Unknown")
            print("Device Category: Unknown")

    else:
        print("System info JSON file not found.")


present_data()
