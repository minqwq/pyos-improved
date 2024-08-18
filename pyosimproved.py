# DONT CHANGE ANY IMPORTED MODULES NAME, IM SERIOUS
#
# PY OS Improved -- Open-source "Operating System(OS)" written using Python 3
# Make sure you have Python 3.9 or higher, lower version is not tested
# Project creator:minqwq / LR Studio 2024
# 
# For our developer:
# After you write code finished, please add some annotate in your code nearby, you maybe know why.
# 
# I want change this project name to Aoruki OS
# Accept?
import time as tm # Time
import getpass # Password?
import datetime # Time?
import calendar # Calendar
import os # Communicate to your system
import sys # idk
import time # Time
# import socket
# import struct
# import select
import random # Random tools
import uuid # Generate uuid
import psutil # Get hardware status
from os import path # Path control
import colorama # Color
from colorama import Fore as fore # idk
from colorama import Back as back
# import rich.spinner # idk
# sys.path.append("./")
import platform
# import rich
import requests
import pretty_errors
print(colorama.Fore.LIGHTGREEN_EX + "All modules loaded!" + "\033[0m")
# Preload classes
#
# New color library imported, but legacy will never remove
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
print("Added class 'color'")
class text: # TIcons
    error = color.red + "[!] " + color.reset
    success = color.green + "[O] " + color.reset
    loading = color.yellow + "[...] " + color.reset
    doubt = color.grey + "[?] " + color.reset
print("Added class 'text'")
class textmoji: # Textmojis
    ciallo = "(∠・ω< )⌒☆"
    omg0 = "₍•Д•)"
    hahaha = "ꉂ(ˊᗜˋ*)"
    owo_neko = " ฅ( ̳• ◡ • ̳)ฅ"
    owo = "(´･ω･`)"
    uhmm = "(*/ω＼*)"
print("Added class 'textmoji'")
pyosimprovedtips = ['Did you know random tools? its so useful!', 'You can shutdown system using shutdown command.', 'Wanna see current hardware performance? type perf.', 'Official github repository:https://github.com/minqwq/pyos-improved', 'Ciallo～(∠・ω< )⌒☆', 'Star this project if you love ღゝ◡╹)ノ♡ https://github.com/minqwq/pyos-improved', 'za~ko~♡za~ko~♡', 'Kernel panic! ...Just kidding its not real ( ˝ᗢ̈˝ )', 'Did you know cheating is illegal? i ve just called police, just wait and go in', 'amogus', 'ღゝ◡╹)ノ♡', 'Coding using vim 8.2', 'My github profile:https://github.com/minqwq', 'so...', 'Who want a stylus!?', 'Also try Sabbat of the witch(Sanoba witch)!', 'im thinking miku miku oo ee oo', 'Discuss about this system:https://minqwq.666forum.com/f1-py-os-improved', 'Wanna contribute our development? call me via email:minqwq723897@outlook.com', 'bababoy', 'monday left me broken', '。', 'Also try original PY OS! https://github.com/AMDISYES/pyos_core', 'Nobody care you? lets be a friend.', 'mystery chinese words:你说的对，但是PY OS Improved是minqwq自主研发的次世代操作系统，中间忘了，这就是PY OS Improved带给我的自信', 'View our official site!:https://www.minqwq.us.kg/pyosimproved']
print("Tips loaded success")
i = os.system("alias cls=clear")
system_version = "1.0 Release"
system_build = "Build 94"
# BIOS Animation
print("cleaning screen...") # Clean screen first
i = os.system("clear")
time.sleep(0.5)
print("1024x768 VGA | 256C | Unknown")
print(colorama.Back.RED + "NO SINGAL" + color.reset)
time.sleep(1)
i = os.system("clear")
print("Press F1 for BIOS Setup")
time.sleep(1)
i = os.system("clear")
print("Press F1 for BIOS Setup.")
time.sleep(1)
i = os.system("clear")
print("Press F1 for BIOS Setup..")
time.sleep(1)
i = os.system("clear")
print("Press F1 for BIOS Setup...")
time.sleep(1)
i = os.system("clear")
i = os.system("mpg123 -q ./beep.mp3") # *beep*
print("Access BIOS v8.3")
print("bios.mcpestudio.com/release/8/3/index.html")
time.sleep(0.3)
print(color.yellow + "Testing Memory..." + color.reset)
time.sleep(0.5)
totalmem = psutil.virtual_memory().total
print(color.green + str(totalmem) + " Bytes OK" + color.reset)
time.sleep(0.1)
print(color.yellow + "Load system => HDD" + color.reset)
time.sleep(0.1)
print(color.green + "PY OS Improved " + system_version + " /unk /stack /uwu" + color.reset)
time.sleep(1)
i = os.system("clear")
time.sleep(0.1)
# Boot manager
print(colorama.Fore.LIGHTCYAN_EX + "PY OS Improved Boot manager" + color.reset)
print("\n1:PY OS Improved " + system_version + "\n2:Reboot\n3:Shutdown\n4:PY OS Improved Pre-Alpha 1")
bootChoice = input("> ")
if bootChoice == "2":
    os.execv(sys.executable, ['python'] + sys.argv)
elif bootChoice == "3":
    sys.exit()
elif bootChoice == "4":
    i = os.system("clear")
    print("If you want exit, press Ctrl+C to shutdown")
    i = os.system("python3 ./.pyosimproved_prealpha_original_file/pyosimproved.py")
    sys.exit()
i = os.system("clear")
# Startup screen
print(color.blue + "    ______  __       ____  _____")
print("   / __ \ \/ /      / __ \/ ___/")
print("  / /_/ /\  /      / / / /\__ \ ")
print(color.cyan + " / ____/ / /      / /_/ /___/ / ")
print("/_/     /_/       \____//____/  " + color.reset)
print(colorama.Fore.BLACK + colorama.Back.LIGHTBLUE_EX + "      |---==Improved==---|      " + color.reset)
print(" ")
print(random.sample(pyosimprovedtips, 1))
print(" ")
print("\033[38;5;45m" + "PY " + "\033[38;5;81m" + "OS " + "\033[38;5;117m" + "Im" + "\033[38;5;153m" + "pr" + "\033[38;5;189m" + "ov" + "\033[38;5;225m" + "ed" + color.reset + " | " + system_version + " | " + system_build)
print("Codename " + colorama.Fore.LIGHTGREEN_EX + "Komeiji Koishi" + color.reset)
print("The Physical You(PY) OS logos is not are registered trademark, you can use it on anywhere.")
print("Original by AMDISYES | Improved Version by minqwq & bibimingming ヽ(✿ﾟ▽ﾟ)ノ")
print(" ")
print("PY OS Improved is a open source software")
print("Under CC-BY-NC-SA 4.0 License")
print(colorama.Fore.LIGHTCYAN_EX + "Feel free to improve PY OS Improved!" + color.reset)
print(" ")
print("Make sure always are latest version!")
print("Update trick:shutdown PY OS Improved and type './update.sh' on pyos-improved folder to update system")
print("For check update:./checkupdate.sh")
print(" ")
print("Current source code lines:569")
print(" ")
print("(c) LR Studio & FCNM 2022--2024")
time.sleep(5)
i = os.system("clear")
time.sleep(0.1)
print("Calling system-process ...", end=' ')
time.sleep(0.25)
print(color.green + "success" + color.reset)
time.sleep(0.1)
print("Detecting hardwares ...", end=' ')
time.sleep(0.5)
print(color.green + "updated" + color.reset)
time.sleep(0.05)
print("Starting user-manager ...", end=' ')
time.sleep(0.1)
print(color.green + "started" + color.reset)
time.sleep(0.2)
print("Starting login-manager ...", end=' ')
time.sleep(0.1)
print(color.green + "started" + color.reset)
time.sleep(0.3)
i = os.system("clear")
time.sleep(0.1)
i = os.system("mpg123 -q ./startup.mp3")
print(color.green + "h-hewwo! wewcome back to py os improved, senpai >///<. i-i missed you so much! x3" + color.reset) # Login screen
print(colorama.Fore.LIGHTGREEN_EX + "Leave blank for shutdown" + color.reset)
now = datetime.datetime.now()
other_StyleTime = now.strftime("%b %a %d %H:%M:%S %Y")
print("Current time: " + colorama.Fore.LIGHTCYAN_EX + other_StyleTime + color.reset)
print("pwease, pweasew login to youw account >.< x3")
count = 0
stpasswd = "ciallo"
while count < 3:
    user = input("> ")
    if user == "gaster":
        os.execv(sys.executable, ['python'] + sys.argv)
    if user == "":
        sys.exit()
    if user == "bai9nine":
        print("nope.   --minqwq")
    if user == "yukari2024":
        print(colorama.Back.LIGHTBLUE_EX + "PY OS Improved has been terminated.")
        print("and this is not a issue, its just a easter egg." + color.reset)
        sys.exit()
    if user == "yukari":
        print(colorama.Back.LIGHTBLUE_EX + "nope bro")
        print("change her's second name and retry to login is useless." + color.reset)
        sys.exit()
    if user == "root":
        i = os.system("mpg123 -q ./beep.mp3")
        print(colorama.Back.RED + colorama.Fore.WHITE + "This account has been protected by password, please type password(ciallo)" + color.reset)
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
                print("Last login: " + colorama.Fore.LIGHTCYAN_EX + other_StyleTime + color.reset)
                print("\nWelcome to Larine Shell(lsh) version 1.4.0\na User non-friendly shell")
                while count < 3:
                  # Line 39 is a critical process, dont change it   --minqwq
                  # lsh_time = now.strftime("%H:%M:%S")
                  # lsh_username = i = os.system("whoami")
                    cmd = input(colorama.Fore.LIGHTBLUE_EX + "root" + color.grey + "@" + colorama.Fore.LIGHTCYAN_EX + "tiramisu" + colorama.Fore.LIGHTGREEN_EX + " # " + color.reset) # Shell style(redesigned by minqwq)
                    if cmd == "ls": # Path
                        print("root path:")
                        i = os.system("ls ./")
                        print("programs path:")
                        i = os.system("ls ./apps/")
                        print("music path:")
                        i = os.system("ls ./music/")
                    elif cmd == "uwufetch": # a Fake neofetch
                        print(color.blue + "  ______   __     ___  ____  ")
                        print(" |  _ \ \ / /    / _ \/ ___| ")
                        print(color.cyan + " | |_) \ V /    | | | \___ \ ")
                        print(" |  __/ | |     | |_| |___) |")
                        print(" |_|    |_|      \___/|____/ " + color.reset)
                        print(color.purple + "      --- Improved ---       " + color.reset)
                        time.sleep(0.1)
                        print("System:PY OS Improved " + system_version + " " + system_build)
                        time.sleep(0.1)
                        print("CPU:Intel Pentium 4@1400MHz")
                        time.sleep(0.1)
                        print("GPU:Cirrus Logic GD 5446(4MB)")
                        time.sleep(0.1)
                        print("Memory: " + str(totalmem) + " Bytes")
                        time.sleep(0.1)
                        print("Sound Card:Sound Blaster 16")
                        time.sleep(0.1)
                        print(text.error + color.red + "Ethernet Card:Not found" + color.reset)
                        time.sleep(0.1)
                        print("Disk:HDD1=30GB, HDD2=55GB")
                    elif cmd == "ping": # Ping tool
                        pingToolIPInput = input("Input IP or Domain: ")
                        pingToolCountInput = input("Send how many packages: ")
                        i = os.system("ping -c " + pingToolCountInput + " " + pingToolIPInput)
                    elif cmd == "fm":
                        i = os.system("./apps/ranger/ranger.sh")
                    elif cmd == "sudo": # sudo not sudo
                        print("This system is not based on linux, so sudo is not on here")
                    elif cmd == "about": # About system
                        print("---------------| About |---------------")
                        print(color.blue + "PY OS Improved " + system_version + " " + system_build + color.reset)
                        print(color.grey + "(C) 0x1c Studio 2022--2023 | (C) LR Studio & FCNM 2024" + color.reset)
                        print(" ")
                        print("about -c for credits...")
                    elif cmd == "about -c":
                        print(colorama.Fore.LIGHTCYAN_EX + "Credits" + color.reset)
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Developers" + color.reset)
                        print("minqwq | Interface Design, Coder, Project Creator, Document Editer")
                        print("bibimingming | Module Installer")
                        print("AMDISYES(Original PY OS) | Original Project Creator")
                        print("Yukari2024 | Installer")
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Early developing tester(not sorted)" + color.reset)
                        print(colorama.Back.BLUE + "Currently early development is not ended, if you install and test, you can call me and i will add your name!" + color.reset)
                        print("minqwq")
                        print("bibimingming")
                        print("Safari_Browse(Rongxuan2022)")
                        print("AMDISYES")
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Special Thanks for these projects" + color.reset)
                        print("https://github.com/shkolovy/tetris-terminal | Used for games")
                        print("https://github.com/pipeseroni/pipes.sh | Used for screensaver")
                    elif cmd == "power":
                        print("Power options:")
                        print("Shutdown:shutdown")
                        print("Restart:reboot")
                        print(" ")
                        print("ex:power reboot")
                    elif cmd == "power shutdown": # Shutdown
                        i = os.system("mpg123 -q ./shutdown.mp3")
                        print(color.yellow + "[...] Killing all process..." + color.reset)
                        time.sleep(1)
                        i = os.system("clear")
                        sys.exit()
                    elif cmd == "power reboot":
                        print(color.cyan + "Restarting..." + color.reset)
                        time.sleep(1)
                        os.execv(sys.executable, ['python'] + sys.argv)
                    elif cmd == "screensaver": # Screensaver
                        print("Available screensavers:\npipes\nmatrix\n\nex:screensaver pipes")
                    elif cmd == "screensaver pipes":
                        i = os.system("cd ./apps/_screensaver/pipes.sh/ && ./pipes.sh && cd ../../../")
                        i = os.system("clear")
                    elif cmd == "screensaver matrix":
                        i = os.system("cd ./apps/_screensaver/cmatrix && ./cmatrix.sh && cd ../../../")
                    elif cmd == "tetris":
                        print("   #####   ####  #####   ###    #   ####")
                        print("     #     #       #     #  #      #")
                        print(" *   #     ###     #     # #    #   ###   *")
                        print("     #     #       #     #  #   #      #")
                        print("     #     ####    #     #   #  #  ####")
                        print(" ")
                        print("by shkolovy")
                        print("https://github.com/shkolovy/tetris-terminal")
                        time.sleep(3)
                        i = os.system("python3 ./apps/tetris/tetris.py")
                    elif cmd == "musicplayer": # Music player
                        print("v1.3")
                        print("How to play:musicplayer -t=<type> play" + color.cyan + " *Enter*" + color.reset)
                        print("Available type:module, sid, mpeg")
                        print("For internal musics list, type musicplayer -l to get a list")
                        print(" ")
                        print("Play custom audio file:Put your audio file to <PY OS Improved>/music/custom/<filetype>")
                        print("and start PY OS Improved")
                        print("and type musicplayer custom-<filetype>" + color.cyan + " *Enter*" + color.reset)
                        print("to play custom audio file")
                        print("ex:musicplayer custom-mpeg")
                        print("* Module music types(xm, mod, s3m)=custom-module, not custom-xm, custom-mod, custom-s3m")
                    elif cmd == "musicplayer -t=module play":
                        i = os.system("ls ./music/modulemusic")
                        mpModulePlay = input("Type a music filename: ")
                        i = os.system("openmpt123 --quiet ./music/modulemusic/" + mpModulePlay)
                    elif cmd == "musicplayer -t=sid play":
                        i = os.system("ls ./music/sid")
                        mpSIDPlay = input("Type a music filename: ")
                        i = os.system("sidplayfp -q ./music/sid/" + mpSIDPlay)
                    elif cmd == "musicplayer -t=mpeg play":
                        i = os.system("ls ./music/mpeg")
                        mpMPEGPlay = input("Type a music filename: ")
                        i = os.system("mpg123 -q ./music/mpeg/" + mpMPEGPlay)
                    elif cmd == "musicplayer -l":
                        print("musicname -t=type play filename")
                        print(colorama.Fore.BLACK + colorama.Back.WHITE + "Module(xm, mod, s3m)" + color.reset)
                        i = os.system("ls ./music/modulemusic/")
                        print(colorama.Fore.BLACK + colorama.Back.WHITE + "SID(Commodore 64/128)" + color.reset)
                        i = os.system("ls ./music/sid/")
                        print(colorama.Fore.BLACK + colorama.Back.WHITE + "MPEG" + color.reset)
                        i = os.system("ls ./music/mpeg/")
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
                    elif cmd == "uname":
                        print(os.uname())
                    elif cmd == "perf": # Performance tools
                        print("Performance v1.1 by ★minqwq★")
                        print(" ")
                        print("cpu:Show the cpu's all performance")
                        print("  percent:Show percent")
                        print("  cores:Show total cores")
                        print("  fq:Show frequency")
                        print("mem:Show the memory")
                        print("uptime:Show system uptime")
                        print("swapmem:Show the swap memory's info")
                        print("disk:Show disk's all performance")
                        print("  usage:Show usage")
                        print("")
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
                    elif cmd == "perf cpu cores": # Performance tools / cpu cores
                        print(psutil.cpu_count())
                    elif cmd == "perf cpu fq": # Performance tools / cpu freq
                        print(psutil.cpu_freq())
                    elif cmd == "perf disk": # Performance tools / disk
                        print(psutil.disk())
                    elif cmd == "perf disk usage": # Performance tools / disk usage
                        print(psutil.disk_usage('/'))
                    elif cmd == "imgview": # Image viewer
                        print(color.blue + "Image Viewer! 1.0 developed by minqwq" + color.reset)
                        print("\ncustom:Print user's custom image(<PY OS Improved>/image/custom)\nitnl:Print internal image(For list just manually type imgview itnl)")
                    elif cmd == "imgview itnl ciallo":
                        ciallo_img=img.open('./image/example/ciallo.jpeg')
                        img.show()
                    elif cmd == "caesar":
                        def option():
                            while True:
                                print("Caesar tools v1.0 code from CSDN")
                                print("Type a option...")
                                print("e:Encode\nd:Decode\nq:Quit")
                                mode=input("> ").lower()
                                if mode in "e d q".split():
                                    return mode
                                else:
                                    print("Incorrect option")
                        
                        def getKey(mode):
                            key=0
                            while key<=0 or key>=26:
                                try:
                                    key=int(input("Please type a key code...(from 1 to 26):"))
                                except:
                                    print("Illegal key code")
                            if mode=="d":
                                key=-key
                            return key
                        
                        def getMessage(key):
                            text=input("Please type encoded text:")  
                            message=""
                            for i in text:
                                num=ord(i)
                                num=num+key
                                if i.isupper():
                                    if num>ord("Z"):
                                        num=num-26
                                    elif num<ord("A"):
                                        num=num+26
                                elif i.islower():
                                    if num>ord("z"):
                                        num=num-26
                                    elif num<ord("a"):
                                        num=num+26
                                message += chr(num)
                            return message
                        
                        mode = option()
                        if mode == "q":
                            print("Welcome to you use this tool again!")
                        elif mode == "e":
                            key=getKey(mode)
                            str1=getMessage(key)
                            print("Encode result:\n\n",str1)
                        elif mode == "d":
                            key=getKey(mode)
                            str2=getMessage(key)
                            print("Decode result is:\n\n",str2)
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
                    elif cmd == "cuscmd":
                        print("Type custom command below...(ex:cat ciallo.txt)")
                        customCommand = input("")
                        i = os.system(customCommand)
                    elif cmd == "news":
                        requestsUrl = "https://www.minqwq.us.kg/pyosimproved/news/latest.txt"
                        requestsResponse = requests.get(requestsUrl)
                        if requestsResponse.status_code == 200:
                            print(colorama.Fore.LIGHTGREEN_EX + "STATUS:200(Success)\n" + color.reset)
                            requestsText = requestsResponse.text
                            print(requestsText)
                        else:
                            print("STATUS:" + requestsResponse.status_code + "(Failed)")
                    elif cmd == "passwd": # Change password(for this session)
                        stpasswd = input("Input new password of this session: ")
                    elif cmd == "calendar": # Calendar
                        yy = int(input("Year: "))
                        mm = int(input("Month: "))
                        print(color.green + "PY OS Calendar\n" + color.reset + calendar.month(yy, mm))
                    elif cmd == "calcurse":
                        i = os.system("calcurse")
                    elif cmd == "help": # Command list
                        print("Command List:")
                        print(colorama.Fore.LIGHTCYAN_EX + "ls             View the path")
                        print("about          Show the system's information")
                        print("converter      A tool to convert .lpap/.lpcu/.bbc to .umm")
                        print("time           Show the time and date")
                        print("calendar       Show a calendar")
                        print("calc           A simple calculator")
                        print("clear          Clean the screen")
                        print("passwd         Change your password")
                        print("exit           Log out")
                        print("power          Power options...")
                        print("uwufetch       List all hardware and system version")
                        print("sudo           Nothing")
                        print("ping           Ping tool python version(Unavailable)")
                        print("random         Random tools")
                        print("perf           Performance tools")
                        print("notepad        a Text editor, very simple")
                        print("musicplayer    Play music")
                        print("imgview        Debug only, dont use")
                        print("caesar         Caesar encryption tools")
                        print("uname          Show a information about your computer(Linux only)")
                        print("tetris         Tetris game written using Python 3")
                        print("fm             File manager(Are you installed ranger?)")
                        print("screensaver    Save your VGA screen, make your pc like a pro")
                        print("cuscmd         Run custom command")
                        print("news           Show latest news of PY OS Improved.")
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
                            print("Input error.\n" + str(e))
                    elif cmd == "": # what is this??? --minqwq at 2024-06-12 19:32
                        space = "0"
                    elif cmd == "clear": # Clear screen using real system command
                        i = os.system("clear")
                    elif cmd == "exit": # Logout
                        break
                    else: # Wrong command
                        print(text.error + color.red + "i can't seem to find the command >.<" + color.reset)
            else: # Wrong password
                print(color.red + "h-hewwo, i think your password is wrong >.< ple-please retry, senpai? x3" + color.reset)
    else:
        print(text.error + color.red + "s-sowwy, i can't seem to find this user, owo! >.<" + color.reset)
