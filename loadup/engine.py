import speech_recognition as sr
import pywhatkit
import threading
import re
from gtts import gTTS
from playsound import playsound

class Engine:
    def __init__(self):
        self.ear = sr.Recognizer()
        self.is_listening = False
        self.trigger_name = 'maya'

    def talk(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('speech.mp3')
        playsound('speech.mp3')

    def set_microphone_threshold(self):
        with sr.Microphone() as mic:
            print('\nCalibrating microphone sensitivity...')
            self.ear.adjust_for_ambient_noise(mic, duration=1)
            print('Microphone sensitivity calibrated.')

    def take_command(self):
        try:
            with sr.Microphone() as mic:
                print('\nListening...\n')
                self.ear.dynamic_energy_adjustment_ratio = 1.5  # Adjust this ratio to control dynamic energy adjustment
                voice = self.ear.listen(mic)
                command = self.ear.recognize_google(voice)
                command = command.lower()
                return command
        except Exception as e:
            print(f"Error: {e}")
            return ''  # Return an empty string if an error occurs

    def process_command(self, command):
        if re.search(r'\b' + self.trigger_name + r'\b', command):
            command = re.sub(r'\b' + self.trigger_name + r'\b', '', command)
            if 'play' in command:
                command = command.replace('play', 'playing')
                song = command + ''
                self.talk(song)
                pywhatkit.playonyt(song)
            elif 'who are you' in command:
                print('Hey! My name is Maya. I am an Artificial Intelligence designed by Kafy Dier aka Adhrit Verma. '
                      'I am the very first build of his 1st generation versions of full-fledged AIs')
                self.talk('Hey! My name is Maya. I am an Artificial Intelligence designed by Kafy Dier aka Adhrit Verma. '
                          'I am the very first build of his 1st generation versions of full-fledged AIs')

    def listening_loop(self):
        while self.is_listening:
            command = self.take_command()
            if command:
                self.process_command(command)

    def run_maya(self):
        self.set_microphone_threshold()
        self.is_listening = True
        listening_thread = threading.Thread(target=self.listening_loop)
        listening_thread.start()
        self.talk("Maya is ready.")


engine = Engine()
engine.run_maya()
# Keep the main thread running to perform other tasks or use time.sleep() to pause execution
while True:
    pass
