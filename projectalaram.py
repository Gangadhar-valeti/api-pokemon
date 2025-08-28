import pygame
import time
import datetime

def setalaram(alaramtime):
    print(f"alaram set for ={alaramtime}")
if __name__=="__main__":
    alaramtime=input("enter the alaram to want(HH:MM:SS)=")
    setalaram=alaramtime
    soundfile="patalu.mp3"
    isrunning=True
    while isrunning:    
        currenttime=datetime.datetime.now().strftime("%H:%M:%S")
        print(currenttime)
        if currenttime==alaramtime:
            print(f"wake up the time is {currenttime} ☀️😎")
            pygame.mixer.init( )
            pygame.mixer.music.load(soundfile)

            
            pygame.mixer.music.play(loops=-1)
            print("enter the to stop the alaram....")
            input()

            pygame.mixer.music.stop()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            isrunning=False
        
        time.sleep(1)