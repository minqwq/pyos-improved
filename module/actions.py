import psutil
import os
import time
import platform
import datetime
def sk_act_about():
    print("ScarletKernel / CoreUtil:Actions / 1.3_R2")
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
    except Exception:
        pass
def linuxUtil_detectDistro():
    if platform.system() == "Linux":
        os.system("python ./apps/coreutils/tinythings/detectdistro_linux/distrodetect.py")
    else:
        platform.system()
def welcome_withDetectTime(username):
    dtn = datetime.datetime.now()
    if int(dtn.strftime("%H")) >= 6:
        print("Yo " + username + ", Good morning!")
    elif int(dtn.strftime("%H")) >= 12:
        print("It's noon " + username + ", go eat something...")
    elif int(dtn.strftime("%H")) >= 14:
        print("Good afternoon " + username + "!")
    elif int(dtn.strftime("%H")) >= 18:
        print("It's night now, still working, " + username + "?")
    elif int(dtn.strftime("%H")) >= 21:
        print("Time to sleep, " + username + ".")
    elif int(dtn.strftime("%H")) >= 0:
        print("It's overnight now, why not go to sleep " + username + "?")
def cat(file):
    tmp_catcore = open(file, "r", encoding="utf-8")
    for content in tmp_catcore:
        print(content, end="")
    print()
