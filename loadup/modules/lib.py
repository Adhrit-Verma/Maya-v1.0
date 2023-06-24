import json
import os
import sys
import requests
import pywhatkit
import re
from modules.sys1 import SystemInfo


class CommandWeb:
    def __init__(self, command):
        self.command = command
        self.system_info = SystemInfo()

    def execute_command(self):
        if re.search(r'\bplay\b', self.command, re.IGNORECASE):
            song = re.sub(r"\b(play|song)\b","playing", self.command, flags=re.IGNORECASE)
            print(song)
            pywhatkit.playonyt(song)
            return song
        elif re.search(r"\b(what|weather)\b", self.command, re.IGNORECASE):
            return self.get_weather_report()
        elif re.search(r"\b(introduce.*yourself|who.*are.*you|what.*are.*you|explain.*yourself)\b", self.command, re.IGNORECASE):
            response = "Hey! My name is Maya, Version 1.5.0. I am your digital assistant designed to automate and help you in your daily tasks with the help of various Machine Learning models and basic data mining techniques. I am the first of second-generation digital assistants of the Ada Project."
            return response
        elif re.search(r"\b(progress|report)\b", self.command, re.IGNORECASE):
            response = "As Maya, your dedicated virtual assistant, I'm excited to share my progress with you! Currently, I can provide real-time weather updates and play music from YouTube for your entertainment. However, I'm continuously evolving to offer even more advanced features and functionalities.In the future, you can expect me to handle file management tasks like clearing junk files, creating folders, and scheduling drive defragmentation on your PC. I'm also expanding my capabilities to include online services such as searching for flights, trains, and buses, finding restaurants and hotels, and providing navigation based on your device's location. Rest assured that I'm committed to becoming your ultimate virtual companion in the A.D.A program. Stay tuned for further updates and enhancements as I strive to make your daily tasks easier and more convenient. Together, we'll achieve great things!" 
            return response
        elif re.search(r"\b(system|info)\b", self.command, re.IGNORECASE):
            if re.search(r"\b(device)\b", self.command, re.IGNORECASE):
                response = self.system_info.get_system_info('device')
            elif re.search(r"\b(cpu)\b", self.command, re.IGNORECASE):
                response = self.system_info.get_system_info('cpu')
            elif re.search(r"\b(memory)\b", self.command, re.IGNORECASE):
                response = self.system_info.get_system_info('memory')
            else:
                response = self.system_info.get_system_info()
            return response
        else:
            return "Sorry, I couldn't understand your command."

    def get_weather_report(self):
        # Load system info from the JSON file
        current_path = os.path.abspath(sys.argv[0])
        drive = os.path.splitdrive(current_path)[0]
        with open(rf"{drive}/A.D.A/A.D.A/loadup/utils/system_info.json") as file:
            system_info = json.load(file)

        # Get latitude and longitude from the system info
        latitude = system_info["pc_location"]["latitude"]
        longitude = system_info["pc_location"]["longitude"]

        # API endpoint and parameters
        api_key = "50892d97f2cfebd2c87f15a39aa34d21"
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

        # Send a GET request to the API
        response = requests.get(url)
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Create the climate report
        report = f"The current weather is {description}. "
        report += f"The temperature is {temperature}°C, humidity is {humidity}%, and wind speed is {wind_speed} meter per second."
        return report
