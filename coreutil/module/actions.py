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
    print("ScarletKernel / CoreUtil:Actions / 1.4.5")
def dotLoader(howMany, howSlow):
    for dotLoader_time in range(howMany):
        sys.stdout.write(".")
        sys.stdout.flush()
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
def filesearch(keyword, directory='.', search_subdirs=True):
    """
    Search for files and directories containing the keyword in their names
    
    :param keyword: Keyword to search for (case insensitive)
    :param directory: Directory to search in (default: current directory)
    :param search_subdirs: Whether to search subdirectories (default: True)
    :return: None (prints results directly)
    """
    # ANSI color codes
    COLOR_RESET = "\033[0m"
    COLOR_KEYWORD = "\033[1;33m"  # Bright yellow
    COLOR_FILE = "\033[0m"        # Reset (normal text)
    COLOR_DIR = "\033[1;34m"      # Bright blue
    COLOR_PATH = "\033[0;36m"     # Cyan (for paths)
    COLOR_TYPE = "\033[0;90m"     # Gray (for type indicators)

    print(f"\nSearching for '{COLOR_KEYWORD}{keyword}{COLOR_RESET}' in {COLOR_PATH}{os.path.abspath(directory)}{COLOR_RESET}\n")
    
    matches_found = False

    try:
        for root, dirs, files in os.walk(directory if search_subdirs else (directory,)):
            # Search directories first
            for dir_name in dirs:
                if keyword.lower() in dir_name.lower():
                    rel_path = os.path.relpath(root, directory)
                    display_name = dir_name.replace(
                        keyword, f"{COLOR_KEYWORD}{keyword}{COLOR_DIR}"
                    )
                    location = f"./{rel_path}" if rel_path != "." else "."
                    print(f"  {COLOR_DIR}{display_name}/{COLOR_RESET}  {COLOR_TYPE}(dir) {COLOR_PATH}({location}){COLOR_RESET}")
                    matches_found = True
            
            # Then search files
            for file_name in files:
                if keyword.lower() in file_name.lower():
                    rel_path = os.path.relpath(root, directory)
                    display_name = file_name.replace(
                        keyword, f"{COLOR_KEYWORD}{keyword}{COLOR_RESET}"
                    )
                    location = f"./{rel_path}" if rel_path != "." else "."
                    print(f"  {COLOR_FILE}{display_name}{COLOR_RESET}  {COLOR_TYPE}(file){COLOR_PATH}({location}){COLOR_RESET}")
                    matches_found = True

        if not matches_found:
            print(f"  No files or directories containing '{COLOR_KEYWORD}{keyword}{COLOR_RESET}' were found")
    
    except FileNotFoundError:
        print(f"  Error: Directory {COLOR_PATH}{directory}{COLOR_RESET} does not exist")
    except PermissionError:
        print(f"  Error: No permission to access {COLOR_PATH}{directory}{COLOR_RESET}")
def coresh():
    pprint.pprint(dict(globals()))
    while True:
        cmd = input("initramfs >_ $ ")
        if cmd == "about":
            sk_act_about()
            print("initramfs input v1.0.1")
        elif cmd == "exit":
            sys.exit()
        elif cmd.startswith("dlt"):
            dotLoader(50, 0.01)
        else:
            print("command not found in scarlet kernel.")
