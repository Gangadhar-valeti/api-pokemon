import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(audio):
    """Function to speak the given audio text."""
    engine.say(audio)
    engine.runAndWait()

def get_voices(voice):
    """Function to set the voice based on user input."""
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)  # Male voice
    elif voice == 2:
        engine.setProperty('voice', voices[1].id)  # Female voice
    else:
        print("Invalid choice. Please select 1 for male or 2 for female.")
        return
    time.sleep(0.5)  # Small delay to ensure the engine is ready
    speak("Hello, this is Gangadhar.")

while True:
    try:
        voice = int(input("Press 1 for male and 2 for female: "))
        get_voices(voice)
    except ValueError:
        print("Please enter a valid number.")
