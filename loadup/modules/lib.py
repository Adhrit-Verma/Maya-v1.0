import geocoder
import json
import pywhatkit

class CommandWeb:
    def __init__(self, command):
        self.command = command

    def execute_command(self):
        if 'play' in self.command:
            self.command = self.command.replace('play', 'playing')
            song = self.command + ''
            pywhatkit.playonyt(song)
            return song
