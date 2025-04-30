import psutil
import os
import sys
import time
import platform
import datetime
import colorama
import plyer
import socket
import pprint

loadtime = 0

def sk_act_about():
    print("ScarletKernel / CoreUtil:Actions / 1.4.2_r6")
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
            print(colorama.Fore.LIGHTYELLOW_EX + "[Low battery(" + str(psutil.sensors_battery().percent) + "%)]", end="")
        elif psutil.sensors_battery().percent > 11:
            print(colorama.Fore.YELLOW + "[Low battery(" + str(psutil.sensors_battery().percent) + "%)]", end="")
        elif psutil.sensors_battery().percent > 6:
            print(colorama.Fore.LIGHTRED_EX + "[Very low battery(" + str(psutil.sensors_battery().percent) + "%)]", end="")
        else:
            print("[" + str(psutil.sensors_battery().percent) + "]", end="")
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
    try:
        tmp_catcore = open(file, "r", encoding="utf-8")
        for content in tmp_catcore:
            print(content, end="")
            time.sleep(0.01)
        print("")
    except FileNotFoundError:
        print("ERROR: file not found: " + file)
    except Exception:
        print("Unexcepted Error")
def cat_bugged(file):
    tmp_catcore = open(file, "r", encoding="utf-8")
    for content in tmp_catcore:
        print(content, end="")
        time.sleep(0.01)
    print("")
def cat_code(file):
    hlcode = highlight.highlight(file)
    print(hlcode)
def showNotify(title, message):
    plyer.notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10,
    )
def netcheck(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return True
    except OSError:
        return False
def loading_spinner(string, tm):
    for i in range(tm * 2):
        print(string + "/", end="\r")
        time.sleep(0.125)
        print(string + "-", end="\r")
        time.sleep(0.125)
        print(string + "\\", end="\r")
        time.sleep(0.125)
        print(string + "|", end="\r")
        time.sleep(0.125)
def coresh():
    pprint.pprint(dict(globals()))
    while True:
        cmd = input("initramfs nouser at void >_ $ ")
        if cmd == "about":
            sk_act_about()
            print("initramfs input v1.0")
        elif cmd == "q":
            sys.exit()
