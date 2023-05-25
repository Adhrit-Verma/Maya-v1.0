import speech_recognition as sr
import pyttsx3
import pywhatkit

ear=sr.Recognizer()
mouth=pyttsx3.init()
rate=mouth.getProperty('rate')
mouth.setProperty('rate',rate-17)

def talk(text):
    mouth.say(text)
    mouth.runAndWait()


def take_command():
    command=""
    try:
        with sr.Microphone() as mic:
            print('\nListening...\n')
            voice= ear.listen(mic)
            command=ear.recognize_google(voice)
            command=command.lower()
    except:
        pass
    return command

def run_ada():
    command=take_command()
    print(command)
    if 'jimmy' in command:
        command=command.replace('jimmy','')
        if 'play' in command:
            command=command.replace('play','playing')
            song=command + ''
            talk(song)
            pywhatkit.playonyt(song)
        elif 'who are you' in command:
            print('Hey!,My name is Jimmy,I am an Artificial Intelligence designed by Kafy Dier aka Adhrit Verma, I am the very first build of his 1st generation versions of full fleged AIs')
            talk('Hey!,My name is Jimmy,I am an Artificial Intelligence designed by Kafy Dier aka Adhrit Verma, I am the very first build of his 1st generation versions of full fleged A-aiees')
run_ada()