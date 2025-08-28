import pygame
import time
import datetime

def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time you want (HH:MM:SS): ")
    set_alarm(alarm_time)
    sound_file = "patalu.mp3"
    is_running = True

    # Initialize pygame mixer
    pygame.mixer.init()

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print(f"Wake up! The time is {current_time} ☀️😎")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play(loops=-1)  # Loop the music indefinitely
            
            print("Press any key to stop the alarm...")

            # Initialize pygame to capture events
            pygame.init()
            screen = pygame.display.set_mode((100, 100))  # Create a small window to capture events
            
            # Event loop to listen for key presses
            while pygame.mixer.music.get_busy():
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:  # Check for any key press
                        pygame.mixer.music.stop()  # Stop the music
                        print("Alarm stopped.")
                        is_running = False
                        break  # Exit the event loop

                time.sleep(0.1)  # Small delay to prevent high CPU usage

        time.sleep(1)
