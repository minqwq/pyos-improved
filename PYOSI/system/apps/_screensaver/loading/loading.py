import os
os.system("clear")
selectMode = input("Select screensaver mode: ")
if selectMode == "1":
    import tqdm
    import time
    import random
    while True:
        for ww in tqdm.tqdm(range(random.randint(0, random.randint(2, 15)))):
            time.sleep(random.random())
            print("\n")
elif selectMode == "2":
    import time
    import random
    while True:
        print("Loading...25%")
        time.sleep(random.random())
        print("Loading...47%")
        time.sleep(random.random())
        print("Loading...73%")
        time.sleep(random.random())
        print("Loading...98%")
        time.sleep(random.random())
        print("Loading...99%")
        time.sleep(random.random())
        print("FATAL ERROR:RESTARTING")
        os.system("clear")
