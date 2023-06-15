import json,os,sys
import requests
import pywhatkit

class CommandWeb:
    def __init__(self, command):
        self.command = command

    def execute_command(self):
        if 'play' in self.command:
            self.command = self.command.replace('play', 'playing')
            song = self.command + ''
            print(song)
            pywhatkit.playonyt(song)
            return song
        elif any(keyword in self.command for keyword in ['who are u', 'introduce yourself', 'what are u', 'explain yourself']):
            response = "Hey! My name is Maya, Version 1.5.0, I am your digital assistant designed to automate and help you in your daily tasks with the help of various Machine Learning models and basic data mining techniques. I am the first of second-generation digital assistants of the Ada Project."
            return response
        elif any(keyword in self.command for keyword in ['show weather report', 'what is the weather today', 'what is the sky upto', 'show weather']):
            return self.get_weather_report()
        else:
            return "Sorry, I couldn't understand your command."

    def get_weather_report():
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
        report += f"The temperature is {temperature}°C, humidity is {humidity}%, and wind speed is {wind_speed} m/s."
        return report
