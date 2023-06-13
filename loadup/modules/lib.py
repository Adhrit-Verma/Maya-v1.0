import geocoder
import json
import pywhatkit

class WebClass:
    def __init__(self, command):
        self.command = command

    def execute_command(self):
        if 'play' in self.command:
            self.command = self.command.replace('play', 'playing')
            song = self.command + ''
            pywhatkit.playonyt(song)
            return f"Playing {song}"
        elif 'weather' in self.command:
            location = self.command.replace('weather', '').strip()
            weather_info = self.get_weather_info(location)
            return f"The weather in {location} is {weather_info}"
        else:
            return "Sorry, I couldn't understand the command"

    def get_weather_info(self, location):
        try:
            with open('system_info.json') as f:
                data = json.load(f)
            
            latitude = data['pc_location']['latitude']
            longitude = data['pc_location']['longitude']
            
            g = geocoder.osm([latitude, longitude], method='reverse')
            
            if g.ok:
                address = g.address
                weather_info = self.retrieve_weather_info(address)
                return weather_info
            else:
                return "Error: Unable to retrieve location information"
        except FileNotFoundError:
            return "Error: System information file not found"
        except KeyError:
            return "Error: Invalid system information file format"
        except Exception as e:
            return f"Error: {e}"
        
    def retrieve_weather_info(self, address):
        # Code to retrieve weather information using the address or location
        # Replace this with your implementation or use a weather API
        
        return f"Weather information for {address}"
