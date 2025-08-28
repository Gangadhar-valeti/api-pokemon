import pygame
import time
import datetime

def setalarm(alaramtime):
    print(f"alaram set for {alaramtime}")
    
if __name__=="__main__":
    alaramtime=input("enter the alaram to want(HH:MM:SS)=") 
    setalaram=alaramtime
    soundfile="patalu.mp3"
    isrunning=True
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    while isrunning:
        currenttime=datetime.datetime.now().strftime("%H:%M:%S")
        print(currenttime)
        
        if currenttime==alaramtime:
            print(f"wake up the time is {currenttime} ☀️😎")
            pygame.mixer.music.load(soundfile)
            
            # Play the music in a loop
            pygame.mixer.music.play(loops=-1)  # -1 for infinite loop
            
            # Wait for user to press ENTER to stop
            print("Press ENTER to stop the alarm...")
            input()
            
            # Stop the music and exit
            pygame.mixer.music.stop()
            isrunning=False
        
        time.sleep(1)

