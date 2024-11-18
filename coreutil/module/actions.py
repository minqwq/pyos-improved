import psutil
import os
import time
import platform
def dotLoader(howMany, howSlow):
    for dotLoader_time in range(howMany):
        print(".", end="")
        time.sleep(howSlow)
def slowprint(text):
    for blyat in text:
        print(blyat, end="", flush=True)
        time.sleep(0.005)
    print("")
def dir_filecount(directory):
    count = 0
    for _, _, files in os.walk(directory):
        count += len(files)
        return count
def cbatteryperc():
    try:
        if psutil.sensors_battery().percent > 21:
            print("Warning: Battery percent is low now(20%), you may need to charge your battery")
        elif psutil.sensors_battery().percent > 11:
            print("Warning: Battery percent is very low now...(10%)")
        elif psutil.sensors_battery().percent > 6:
            print("Warning: Why not go to charge battery now?(5%)")
    except FileNotFoundError:
        pass
def linuxUtil_detectDistro():
    if platform.system() == "Linux":
        os.system("python ./apps/coreutils/tinythings/detectdistro_linux/distrodetect.py")
    else:
        platform.system()
