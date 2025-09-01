import pyttsx3
engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices=engine.getProperty('voices')
   # print(voices[1].id)    
    if voice==1:
        engine.setProperty('voice',voices[0].id)
    if voice==2:
        engine.setProperty('voice',voices[1].id)    
    speak("hello this is gangadhar")
while True:
    voice=int(input("press 1 for male and 2 foer female"))    

    getvoices(voice)           