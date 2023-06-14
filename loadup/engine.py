import speech_recognition as sr
import threading
import re
import pyttsx3
from modules.lib import CommandWeb

class CommandProcessor:
    def __init__(self, trigger_name):
        self.trigger_name = trigger_name

    def process_command(self, command):
        if re.search(r'\b' + self.trigger_name + r'\b', command):
            command = re.sub(r'\b' + self.trigger_name + r'\b', '', command)
            response = CommandWeb(command).execute_command()
            self.talk(response) 

    def talk(self, text):
        try:
            engine = pyttsx3.init()
            voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
            engine.setProperty('voice', voice_id)
            
            engine.setProperty('rate', 170)
            engine.setProperty('volume', 1.0)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error: {e}")



class Engine:
    def __init__(self, trigger_name):
        self.ear = sr.Recognizer()
        self.is_listening = False
        self.trigger_name = trigger_name

    def set_microphone_threshold(self):
        try:
            with sr.Microphone() as mic:
                print("\r" + " " * 50, end="")
                print("Adjusting microphone for noise,please wait ✋")
                self.ear.adjust_for_ambient_noise(mic, duration=1)
        except Exception as e:
            print(f"Error: {e}")

    def take_command(self):
        try:
            with sr.Microphone() as mic:
                print("\r" + " " * 50, end="")  
                print("\rListening...👂", end="")
                self.ear.dynamic_energy_adjustment_ratio = 1.7  # Adjust this ratio to control dynamic energy adjustment
                voice = self.ear.listen(mic)
                command = self.ear.recognize_google(voice)
                command = command.lower()
                return command
        except sr.RequestError:
            print("\r" + " " * 50, end="")  
            print("\rGoogle Speech Recognition service is unavailable.")
        except sr.UnknownValueError:
            print("\r" + " " * 50, end="")  
            print("\rUnable to understand audio.")
        except Exception as e:
            print("\r" + " " * 50, end="")  
            print(f"\rError: {e}")
        return ''


    def listening_loop(self, command_processor):
        while self.is_listening:
            command = self.take_command()
            if command:
                command_processor.process_command(command)

    def run_maya(self):
        self.set_microphone_threshold()
        self.is_listening = True
        command_processor = CommandProcessor(self.trigger_name)
        listening_thread = threading.Thread(target=self.listening_loop, args=(command_processor,))
        listening_thread.start()
        self.talk("Maya is ready.")

    def talk(self, text):
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # Adjust the speech rate as needed
            engine.setProperty('volume', 1.0)  # Adjust the volume as needed
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error: {e}")



engine = Engine(trigger_name='maya')
engine.run_maya()
