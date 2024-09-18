import tqdm
import time
import pygame
pygame.mixer.init()
print("1:timer\n2:timer(rev)\n3:current time\n4:exit")
choice = input("Option?: ")
if choice == "1":
    timerStart = time.time()
    timerController = input("Press enter to stop")
    if timerController == "":
        timerEnd = time.time()
        print(timerEnd - timerStart, end="")
        print(" Second")
elif choice == "2":
    setRevTimerEndTime = input("Set range(second): ")
    if setRevTimerEndTime == "":
        print("Range is none.")
    else:
        for revtimer in tqdm.tqdm(range(int(setRevTimerEndTime))):
            pygame.mixer.music.load("./audio/se/info.mp3")
            pygame.mixer.music.play()
            time.sleep(1)
        pygame.mixer.music.load("./audio/se/success_long.mp3")
        pygame.mixer.music.play()
        input("Press any key to exit")
