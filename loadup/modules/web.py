import pywhatkit

class web:
    def __init__(self):
        pass

    def execute_command(self, command):
        if 'play' in command:
            return self.play_song(command)
        elif 'who are you' in command:
            return self.introduce()

    def play_song(self, command):
        command = command.replace('play', 'playing')
        song = command + ''
        response = song
        return response

    def introduce(self):
        response = 'Hey! My name is Maya. I am an Artificial Intelligence designed by Kafy Dier aka Adhrit Verma. ' \
                   'I am the very first build of his 1st generation versions of full-fledged AIs'
        return response
