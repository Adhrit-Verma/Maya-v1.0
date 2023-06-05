import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Print available voices
for voice in voices:
    print(voice.id)

# Set the desired voice ID
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_id)

# Test the voice
engine.say("Hello, this is a sample text.")
engine.runAndWait()
