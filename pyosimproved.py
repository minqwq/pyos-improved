import time as tm
import getpass
import datetime
import calendar
import os
import sys
import time
import socket
import struct
import select
import random
import uuid
import psutil
from os import path
# Preload classes
#
# How to use these color:
# green for example
# use this trick:
# (color.green + "text here" + color.reset)
# if you want use other color, change "green" to any below name on class color
# color.<color>
class color: # Text colors
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[34m"
    yellow = "\033[33m"
    purple = "\033[35m"
    cyan = "\033[36m"
    grey = "\033[37m"
    reset = "\033[0m"
class text: # TIcons
    error = color.red + "[!] " + color.reset
    success = color.green + "[O] " + color.reset
    loading = color.yellow + "[...] " + color.reset
class textmoji: # Textmojis
    ciallo = "(∠・ω< )⌒☆"
    omg0 = "₍•Д•)"
    hahaha = "ꉂ(ˊᗜˋ*)"
    owo_neko = " ฅ( ̳• ◡ • ̳)ฅ"
    owo = "(´･ω･`)"
    uhmm = "(*/ω＼*)"
pyosimprovedtips = ['Did you know random tools? its so useful!', 'You can shutdown system using shutdown command.', 'Wanna see current hardware performance? type perf.', 'Official github repository:https://github.com/minqwq/pyos-improved', 'Ciallo～(∠・ω< )⌒☆', 'Star this project if you love ღゝ◡╹)ノ♡ https://github.com/minqwq/pyos-improved', 'za~ko~♡za~ko~♡', 'Kernel panic! ...Just kidding its not real ( ˝ᗢ̈˝ )', 'Did you know cheating is illegal? i ve just called police, just wait and go in', 'amogus', 'ღゝ◡╹)ノ♡', 'Coding using vim 8.2', 'My github profile:https://github.com/minqwq', 'so...', 'Who want a stylus!?', 'Also try Sabbat of the witch(Sanoba witch)!']
# BIOS Animation
print("cleaning screen...") # Clean screen first
i = os.system("cls")
i = os.system("clear")
time.sleep(0.5)
print("Press F1 for BIOS Setup")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
print("Press F1 for BIOS Setup.")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
print("Press F1 for BIOS Setup..")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
print("Press F1 for BIOS Setup...")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
i = os.system("mpg123 -q ./beep.mp3") # *beep*
print("Access BIOS v8.2")
print("bios.mcpestudio.com/release/8/2/0/index.html")
time.sleep(0.3)
print(color.yellow + "Testing Memory..." + color.reset)
time.sleep(0.5)
print(color.green + "262144KB OK" + color.reset)
time.sleep(0.1)
print(color.yellow + "Booting From Hard Disk..." + color.reset)
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
# Startup screen
print(color.blue + "  ______   __     ___  ____  ")
print(" |  _ \ \ / /    / _ \/ ___| ")
print(" | |_) \ V /    | | | \___ \ ")
print(color.cyan + " |  __/ | |     | |_| |___) |")
print(" |_|    |_|      \___/|____/ " + color.reset)
print(color.purple + "      --- Improved ---       " + color.reset)
print(" ")
print(random.sample(pyosimprovedtips, 1))
print(" ")
print(text.error + color.red + "Under development, may be unstable")
print("\033[31mPY\033[0m \033[33mOS\033[0m \033[34mImproved\033[0m | Version 1.0(Beta 3 | Build 36)")
print("Original by AMDISYES | Improved Version by minqwq ヽ(✿ﾟ▽ﾟ)ノ")
print("This screen will show 5 second")
print(" ")
print("Make sure always are latest version!")
print("Update trick:shutdown PY OS Improved and type 'git pull' on pyos-improved folder to update system")
print(" ")
print("Current source code lines:533")
time.sleep(5)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
print(color.grey + "[INFO] Begin of logging" + color.reset) # System loader screen
time.sleep(0.05)
print(color.yellow + "[...] Waking up system-process..." + color.reset)
time.sleep(0.25)
print(color.green + "[O] system-process is waked up" + color.reset)
time.sleep(0.1)
print(color.yellow + "[...] Detecting hardwares..." + color.reset)
time.sleep(0.5)
print(color.green + "[O] Hardware list updated" + color.reset)
time.sleep(0.05)
print(color.yellow + "[...] Waking up user-manager" + color.reset)
time.sleep(0.1)
print(color.yellow + "[...] Waking up login-manager" + color.reset)
time.sleep(0.2)
print(color.green + "[O] user-manager is waked up" + color.reset)
time.sleep(0.1)
print(color.green + "[O] login manager is waked up" + color.reset)
time.sleep(0.3)
print("[INFO] End of logging(Deleted log cache)")
time.sleep(0.5)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
i = os.system("mpg123 -q ./startup.mp3")
print(color.green + "Hi~ o(*￣▽￣*)ブ My master~ Welcome back to PY OS Improved~" + color.reset) # Login screen
now = datetime.datetime.now()
other_StyleTime = now.strftime("%b %a %d %H:%M:%S %Y")
print("Current time:" + other_StyleTime)
count = 0
stpasswd = "45450721"
while count < 3:
    user = input("Account login: ")
    if user == "root":
        i = os.system("mpg123 -q ./beep.mp3")
        print(color.yellow + "This account has been protected by password, please type password(45450721)" + color.reset)
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
                i = os.system("mpg123 -q beep.mp3")
                tm.sleep(1.5)
                while count < 3:
                    cmd = input(color.cyan + "U" + color.reset + ":root " + color.cyan + "H" + color.reset + ":127.0.0.1 " + color.cyan + "HN" + color.reset + ":Kawaii_System " + color.cyan + "P" + color.reset + ":" + color.red + "Unknown " + color.green + "$ " + color.reset) # Shell style(redesigned by minqwq)
                    if cmd == "ls": # Path
                        print(text.error + color.red + "Path not found" + color.reset)
                    elif cmd == "neofetch": # a Fake neofetch
                        print(color.blue + "  ______   __     ___  ____  ")
                        print(" |  _ \ \ / /    / _ \/ ___| ")
                        print(color.cyan + " | |_) \ V /    | | | \___ \ ")
                        print(" |  __/ | |     | |_| |___) |")
                        print(" |_|    |_|      \___/|____/ " + color.reset)
                        print(color.purple + "      --- Improved ---       " + color.reset)
                        time.sleep(0.1)
                        print("System:PY OS Improved 1.0 b3 b36")
                        time.sleep(0.1)
                        print("CPU:Intel Pentium 4@1400MHz")
                        time.sleep(0.1)
                        print("GPU:Cirrus Logic GD 5446(4MB)")
                        time.sleep(0.1)
                        print("Memory:262144KB(256MB) DDR C:133MHz W:266MHz")
                        time.sleep(0.1)
                        print("Sound Card:Sound Blaster 16")
                        time.sleep(0.1)
                        print(text.error + color.red + "Ethernet Card:Not found" + color.reset)
                        time.sleep(0.1)
                        print("Disk:HDD1=30GB, HDD2=55GB")
                    elif cmd == "ping": # Ping tool
                        print(text.error + color.red + "Unavailable for now" + color.reset)
                    elif cmd == "sudo": # sudo not sudo
                        print("This system is not based on linux, so sudo is not on here")
                    elif cmd == "about": # About system
                        print("---------------| About |---------------")
                        print(color.blue + "PY OS Improved 1.0 b3(Build 36)" + color.reset)
                        print(color.grey + "(C) 0x1c Studio 2022--2023 | (C) LR Studio 2024" + color.reset)
                    elif cmd == "shutdown": # Shutdown
                        i = os.system("mpg123 -q ./shutdown.mp3")
                        print(color.yellow + "[...] Killing all process..." + color.reset)
                        time.sleep(1)
                        i = os.system("clear")
                        i = os.system("cls")
                        sys.exit()
                    elif cmd == "musicplayer": # Music player
                        print("How to play:musicplayer <filename>" + color.cyan + " *Enter*" + color.reset)
                        print("musicplayer playable songs list:")
                        print("Space Debris(space_debris.mod)")
                        print(" ")
                        print("Play custom audio file:Put your audio file to <PY OS Improved>/music/custom/<filetype>")
                        print("and start PY OS Improved")
                        print("and type musicplayer custom-<filetype>" + color.cyan + " *Enter*" + color.reset)
                        print("to play custom audio file")
                        print("ex:musicplayer custom-mpeg")
                        print("* Module music types(xm, mod, s3m)=custom-module, not custom-xm, custom-mod, custom-s3m")
                    elif cmd == "musicplayer space_debris.mod": # Music player internal music
                        print("Press Q to quit player")
                        print("Space Debris -- Unknown")
                        i = os.system("openmpt123 --quiet ./music/modulemusic/space_debris.mod")
                    elif cmd == "musicplayer custom-mpeg": # Music player external mpeg music
                        print("Press Q to quit player")
                        print("Custom mpeg audio -- User's choice")
                        i = os.system("mpg123 -q ./music/custom/mpeg/*")
                    elif cmd == "musicplayer custom-module":
                        print("Press Q to quit player")
                        print("Custom module -- User's choice")
                        i = os.system("openmpt123 --quiet ./music/custom/module/*")
                    elif cmd == "random": # Random tools
                        print("Random v1.0, by minqwq")
                        print(" ")
                        print("number:Generate a random number")
                        print("answer:Randomly choose a answer(from 1 to 4)")
                        print("uuid <mode>:Generate a random uuid")
                    elif cmd == "random number": # Random tools / Random number
                        random_number = random.random()
                        print(random_number)
                    elif cmd == "random answer": # Random tools / Random answer
                        print(random.randint(0,4))
                    elif cmd == "random uuid": # Random tools / Random uuid generator(Not set mode)
                        print(text.error + color.red + "Please set a mode...(ex:random uuid 1)" + color.reset)
                    elif cmd == "random uuid 1": # Random tools / Random uuid generator
                        print(uuid.uuid1())
                    elif cmd == "random uuid 2":
                        print(text.error + color.red + "UUID: No uuid2" + color.reset)
                    elif cmd == "random uuid 3":
                        print(text.error + color.red + "Sorry, this mode is unavailable for now" + color.reset)
                    elif cmd == "random uuid 4":
                        print(uuid.uuid4())
                    elif cmd == "random uuid 5":
                        print(text.error + color.red + "Sorry, thos mode is unable for now" + color.reset)
                    elif cmd == "random ccdomain":
                        ccdomainrdmnum = "https://" + str(random.randint(1000, 9999)) + ".cc"
                        print(ccdomainrdmnum)
                    elif cmd == "converter": # converter but cant select file
                        print("File Convert\nConvert .lpap/.lpcu/.bbc to .umm")
                        input("Input file's path:\n")
                        for i in range(1, 101):
                            print("\r", end="")
                            print("Progress: {}%: ".format(i), "=" * (i // 2), end="")
                            sys.stdout.flush()
                            tm.sleep(0.05)
                        print("\nConvert Complete")
                    elif cmd == "time": # Show current time
                        now = datetime.datetime.now()
                        other_StyleTime = now.strftime("%b %a %d %H:%M:%S %Y")
                        print(other_StyleTime)
                    elif cmd == "time --no-date":
                        now = datetime.datetime.now()
                        other_StyleTimeNoYMD = now.strftime("%H:%M:%S")
                        print(other_StyleTimeNoYMD)
                    elif cmd == "time --no-clk":
                        now = datetime.datetime.now()
                        other_StyleTimeNoHMS = now.strftime("%Y-%m-%d")
                        print(other_StyleTimeNoHMS)
                    elif cmd == "perf": # Performance tools
                        print("Performance v1.0 by ★minqwq★")
                        print(" ")
                        print("cpu:Show the cpu's all performance")
                        print("  percent:Show percent")
                        print("mem:Show the memory")
                        print("uptime:Show system uptime")
                        print("swapmem:Show the swap memory's info")
                    elif cmd == "perf cpu": # Performance tools / cpu all
                        print(psutil.cpu_times())
                    elif cmd == "perf cpu percent": # Performance tools / cpupercent
                        print(psutil.cpu_percent(interval=1))
                    elif cmd == "perf mem": # Performance tools / mem all
                        print(psutil.virtual_memory())
                    elif cmd == "perf mem total":
                        print(psutil.virtual_memory().total)
                    elif cmd == "perf uptime": # Performance tools / uptime
                        print(psutil.boot_time())
                    elif cmd == "perf swapmem": # Performance tools / Swap
                        print(psutil.swap_memory())
                    elif cmd == "notepad":
                        file_path = input("\nCreate file (please enter the path to file): ")
                        
                        if path.exists(file_path):
                            print("\n\tFile already exists!")
                            ans = input("\nDo you want to use this file? (y/n)\n-> ")
                        
                            if ans == 'y' or ans == 'Y':
                                file = open(file_path, "a")
                                ans = input("\nDo you want to erase all content? (y/n)\n-> ")
                        
                                if ans == 'y' or ans == 'Y':
                                    print("\n\tErasing...\n")
                                    file.seek(0)
                                    file.truncate()
                        
                                else:
                                    pass
                        
                            else:
                                exit()
                        
                        else:
                            print("\n\tCreating new file...\n")
                            file = open(file_path, "a")
                        
                        print("\nPress RETURN to start a new line.\nPress Ctrl + C to save and close.\n\n")
                        
                        line_count = 1
                        
                        while line_count > 0:
                            try:
                                line = input("\t" + str(line_count) + " ")
                                file.write(line)
                                file.write('\n')
                                line_count += 1
                            except KeyboardInterrupt:
                                print("\n\n\tClosing...")
                                break
                        
                        file.close()
                    elif cmd == "passwd": # Change password(for this session)
                        stpasswd = input("Input new password of this account: ")
                    elif cmd == "calendar": # Calendar
                        yy = int(input("Year: "))
                        mm = int(input("Month: "))
                        print(color.green + "PY OS Calendar\n" + color.reset + calendar.month(yy, mm))
                    elif cmd == "help": # Command list
                        print("Command List:")
                        print(color.cyan + "ls             View the path")
                        print("about          Show the system's information")
                        print("converter      A tool to convert .lpap/.lpcu/.bbc to .umm")
                        print("time           Show the time and date")
                        print("calendar       Show a calendar")
                        print("calc           A simple calculator")
                        print("clear          Clean the screen")
                        print("passwd         Change your password")
                        print("exit           Log out")
                        print("shutdown       Shutdown system")
                        print("neofetch       List all hardware and system version")
                        print("sudo           Nothing")
                        print("ping           Ping tool python version(Unavailable)")
                        print("random         Random tools")
                        print("perf           Performance tools")
                        print("notepad        a Text editor, very simple")
                        print("musicplayer    Play music")
                    elif cmd == "time --help": # time command help
                        print("Time command options:")
                        print("--help         Show this help")
                        print("--no-date      Print time without date")
                        print("--no-clk       Print time without time")
                    elif cmd == "calc": # Calculator
                        try:
                            formula = input("Enter the formula to be calculated(example:1+1):\n")
                            print(formula + "=", eval(formula))
                        except Exception as e:
                            print("Input error.")
                    elif cmd == "": # what is this??? --minqwq at 2024-06-12 19:32
                        space = "0"
                    elif cmd == "clear": # Clear screen using real system command
                        i = os.system("cls")
                        i = os.system("clear")
                    elif cmd == "exit": # Logout
                        break
                    else: # Wrong command
                        print(text.error + color.red + "Shell:Command not found." + color.reset)
            else: # Wrong password
                print(color.red + "Password Incorrect, please try again..." + color.reset)
    else: # Wrong user name
        print(color.red + "User not found, try another..." + color.reset)
