# DONT CHANGE ANY IMPORTED MODULES NAME, IM SERIOUS
#
# PY OS Improved -- Open-source "Operating System(OS)" written using Python 3
# Make sure you have Python 3.9 or higher, lower version is not tested
# Project creator:minqwq / LR Studio 2024
# 
# For our developer:
# After you write code finished, please add comment(s) in your code nearby, you maybe know why.
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
import requests # Get file from server
import pretty_errors # Crash screen replace
from dialog import Dialog # Dialog
from python_goto import goto # Goto a line
import base256 # Encode and decode
import tqdm # Progress bar
import traceback
print(colorama.Fore.LIGHTGREEN_EX + "All modules-1 loaded!" + "\033[0m")
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
    nya0 = "(ฅ>ω<*ฅ)"
    nya1 = "ヽ(=ˆ･ω･ˆ=)丿"
    nah0 = "╮(‵▽′)╭"
print("Added class 'textmoji'")
class override:
    errorexpection = "teto:ErrorExpection"
    tongue = "teto:a-------"
def echo(string):
    print(string)
pretty_errors.configure(
    postfix               = '\nPY OS Improved has been crashed.\nRestart command:python3 pyosimproved.py\nReport this error!:https://github.com/minqwq/pyos-improved/issues',
    separator_character   = '#',
    line_color            = colorama.Fore.LIGHTBLUE_EX + 'Here > ' + color.reset,
)
print("config updated for pretty-errors")
pyosimprovedtips = ['Did you know random tools? its so useful!', 'You can shutdown system using shutdown command.', 'Wanna see current hardware performance? type perf.', 'Official github repository:https://github.com/minqwq/pyos-improved', 'Ciallo～(∠・ω< )⌒☆', 'Star this project if you love ღゝ◡╹)ノ♡ https://github.com/minqwq/pyos-improved', 'za~ko~♡za~ko~♡', 'Kernel panic! ...Just kidding its not real ( ˝ᗢ̈˝ )', 'Did you know cheating is illegal? i ve just called police, just wait and go in', 'amogus', 'ღゝ◡╹)ノ♡', 'Coding using vim 8.2', 'My github profile:https://github.com/minqwq', 'so...', 'Who want a stylus!?', 'Also try Sabbat of the witch(Sanoba witch)!', 'im thinking miku miku oo ee oo', 'Discuss about this system:https://minqwq.666forum.com/f1-py-os-improved', 'Wanna contribute our development? call me via email:minqwq723897@outlook.com', 'bababoy', 'monday left me broken', '。', 'Also try original PY OS! https://github.com/AMDISYES/pyos_core', 'Nobody care you? lets be a friend.', 'mystery chinese words:你说的对，但是PY OS Improved是minqwq自主研发的次世代操作系统，中间忘了，这就是PY OS Improved带给我的自信', 'View our official site!:https://www.minqwq.us.kg/pyosimproved']
print("Tips loaded success")
os.system("alias cls=clear")
system_version = "1.2.2_R2 Release"
system_build = "Build 198"
# BIOS Animation
print("cleaning screen...") # Clean screen first
os.system("clear")
if sys.platform.startswith("win"):
    print("Warning! you are running this program on Windows, some command may not work.")
    os.system("alias clear=cls")
    print("Setted clear command = cls")
    print("Continue run after 3s...")
    time.sleep(3)
    os.system("clear")
print("Press any key to continue...")
while True:
    debugMode = input("\n")
    if debugMode == "d":
        now = datetime.datetime.now()
        startingtime_t = "???"
        end_startingtime = "???"
        startingtime = "???"
        import pygame
        pygame.mixer.init()
        d = Dialog(dialog="dialog")
        print("You are now in debug mode.")
        print("If crash, dont report ANY error.")
        goto(line=214)
    elif debugMode == "v":
        print(system_version + " " + system_build)
        sys.exit()
    elif debugMode == "h":
        print("d / Enable debug mode")
        print("v / Show version and exit")
        print("h / Manual help")
    else:
        break
d = Dialog(dialog="dialog")
d.set_background_title("R:1024x768 | CD:256 | Screen 0")
d.infobox("No Singal", width=0, height=0, title="Error")
time.sleep(2)
os.system("clear")
print("_")
time.sleep(0.5)
os.system("clear")
print(" ")
time.sleep(0.5)
os.system("clear")
print("_")
time.sleep(0.5)
os.system("clear")
import pygame
pygame.mixer.init()
pygame.mixer.music.load("./audio/se/success.mp3")
pygame.mixer.music.play()
print("Cirnosoft 1964--2024 No rights reserved")
print("Funky BIOS v9.9_baka")
print("reimuhttp://bios.cirnosoft.9/versions/9dot9/updatelog")
time.sleep(0.15)
totalmem = psutil.virtual_memory().total
print(color.green + str(totalmem) + " Bytes OK" + color.reset)
time.sleep(0.05)
print(color.yellow + "Booting default operating system..." + color.reset)
time.sleep(0.1)
print(color.green + "PY OS Improved " + system_version + " /unk /stack /uwu" + color.reset)
time.sleep(1)
os.system("clear")
time.sleep(0.1)
# Boot manager
bootManagerLoopRun = True
print(colorama.Fore.LIGHTCYAN_EX + "PY OS Improved Boot manager" + color.reset)
print("If you dont know which to choose, choose 1.")
print("\n1:PY OS Improved " + system_version + "\n2:Reboot\n3:Shutdown\n4:PY OS Improved Pre-Alpha 1")
while bootManagerLoopRun == True:
    bootChoice = input("> ")
    if bootChoice == "1":
        print("...")
        break
    elif bootChoice == "2":
        os.execv(sys.executable, ['python'] + sys.argv)
    elif bootChoice == "3":
        sys.exit()
    elif bootChoice == "4":
        os.system("clear")
        print("If you want exit, press Ctrl+C to shutdown")
        os.system("python3 ./.earlysystem/pyosimproved.py")
         
        sys.exit()
    elif bootChoice == "5":
        os.system("clear")
        print("If you want exit, press Ctrl+C to shutdown")
        os.system("python3 ./.earlysystem/bbcos-full.py")
        sys.exit()
    else:
        print(color.red + "ERR" + color.reset)
os.system("clear")
# Startup screen
startingtime = time.time()
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
print("Codename " + "\033[38;5;39m" + "baka9" + color.reset)
print("The Physical You(PY) OS logos is not are registered trademark, you can use it on anywhere.")
print("Original by AMDISYES | Improved Version by minqwq & bibimingming ヽ(✿ﾟ▽ﾟ)ノ")
print(" ")
print("PY OS Improved is a open source software and you can share it freedomly")
print("Under WTFPL 2.0 License")
print(colorama.Fore.LIGHTCYAN_EX + "Feel free to improve PY OS Improved!" + color.reset)
print(" ")
print("Make sure always are latest version!")
print("Update trick:shutdown PY OS Improved and type './update.sh' on pyos-improved folder to update system")
print("For check update:./checkupdate.sh")
print(" ")
print("(c) LR Studio & FCNM 2022--2024")
time.sleep(5)
os.system("clear")
time.sleep(0.1)
end_startingtime = time.time()
startingtime_t = end_startingtime - startingtime
pygame.mixer.music.load("./audio/se/welcome.mp3")
pygame.mixer.music.play()
print(colorama.Fore.LIGHTCYAN_EX + "Hewwwo wewcome back to PY OS Improved senpai >.<" + color.reset) # Login screen | For restart to login manager, please goto this line for work normally
print(colorama.Fore.LIGHTGREEN_EX + "Leave blank for shutdown" + color.reset)
now = datetime.datetime.now()
other_StyleTime = now.strftime("%b %a %d %H:%M:%S %Y")
print("Current time: " + colorama.Fore.LIGHTCYAN_EX + other_StyleTime + color.reset)
print("Startup system used " + str(startingtime_t) + "s.")
print("pwease, pweasew login to youw account >.< x3")
print("(You can type a custom name to continue, like 'meguru' after login will show 'meguru@tiramisu #')")
count = 0
stpasswd = "ciallo"
while count < 3:
    user = input("> ")
    if user == "gaster":
        os.execv(sys.executable, ['python'] + sys.argv)
    elif user == "":
        sys.exit()
    elif user == "bai9nine":
        print("nope.   --minqwq")
    elif user == "yukari2024":
        print(colorama.Back.LIGHTBLUE_EX + "PY OS Improved has been terminated.")
        print("and this is not a issue, its just a easter egg." + color.reset)
        sys.exit()
    elif user == "yukari":
        print(colorama.Back.LIGHTBLUE_EX + "nope bro")
        print("change her's second name and retry to login is useless." + color.reset)
        sys.exit()
    elif user == "koishi":
        for idk in range(100000):
            print(colorama.Fore.LIGHTRED_EX)
            print("die", end="")
        for idk2 in range(50000):
            print("look back ", end="")
        for idk3 in range(20):
            for idk4 in tqdm.tqdm(range(5114)):
                print(colorama.Fore.LIGHTRED_EX + "die!!!", end="")
            d.infobox("N? Si??a?", width=0, height=0, title="Er??r")
            time.sleep(random.random())
            os.system("clear")
        d.infobox("Look back~", width=0, height=0, title="From Koishi")
        time.sleep(0.1)
        os.system("clear")
        print("You have been kicked by Komeiji Koishi.\nPlease r???\nP??\nPlease re-lo??..gin.")
    else:
        while count < 3:
            try:
                os.system("clear")
                lshdate = now.strftime("%Y-%m-%d")
                lshtime = now.strftime("%H:%M:%S")
                lsh_hostname = "tiramisu"
                if user == "minqwq":
                    creatorVerifyPassword = "qwe115061"
                    creatorVerify = input("Verify required, please type password...\n> ")
                    if creatorVerify == creatorVerifyPassword:
                        print("The creator of PY OS Improved, welcome back.\n")
                    else:
                        print(color.red + "Access Denied." + color.reset)
                        sys.exit()
                print("h-hewwo there, my sweetie senpai x3")
                print("Welcome to PY OS Improved " + system_version + " >///<")
                print("* Visit our awesome website: https://www.minqwq.us.kg/pyosimproved")
                print("* Come join our telegram group: @pyosimproved")
                print("* IRC Chat: pyos-improved@irc.freenode.net:6667")
                time.sleep(0.05)
                print("\nIf you need some help, pwease senpai, email me at minqwq723897@outlook.com, i w-will gladly help you uwu")
                print("If you have any issues, pwease open an issue h-here: https://github.com/minqwq/pyos-improved/issues")
                print("Powered by PyOS(Previously known as BBC OS)")
                print("Wanna try PyOS? link here:https://github.com/AMDISYES/pyos_core")
                print("Help document for new:input " + colorama.Fore.LIGHTGREEN_EX + "tutor" + color.reset + " and will show help for first using people.")
                time.sleep(0.05)
                print("\nH-hi thewe " + color.cyan + user + color.reset + " >///<, I-I missed you a-a lot.")
                print("Today is " + colorama.Fore.LIGHTCYAN_EX + lshdate + color.reset + " and time is " + colorama.Fore.LIGHTCYAN_EX + lshtime + color.reset + ".\nWeather is not bad.\n")
                os.system("python3 autoexec.py")
                print("\nLarine SHell (lsh) version 1.6 >///<\nit's a wittwe user non-fwiendwy shell...")
                while count < 3:
                  # Line 246 is a critical process, dont change it   --minqwq
                    lsh_time_prepare = datetime.datetime.now()
                    lsh_time = lsh_time_prepare.strftime("%H:%M:%S")
                    print(colorama.Fore.LIGHTYELLOW_EX + "[" + lsh_time + "]" + color.reset, end=" ")
                  # lsh_username = os.system("whoami")
                    cmd = input(colorama.Fore.LIGHTBLUE_EX + user + color.grey + ":" + colorama.Fore.LIGHTCYAN_EX + lsh_hostname + colorama.Fore.LIGHTGREEN_EX + " > " + color.reset) # Shell style(redesigned by minqwq)
                    if user == "d":
                        cmd = input("DEBUG_SHELL > ")
                    if cmd == "ls": # Path
                        print("root path:")
                        os.system("ls ./")
                        print("programs path:")
                        os.system("ls ./apps/")
                        print("music path:")
                        os.system("ls ./music/")
                    elif cmd == "uwufetch": # a Fake neofetch
                        currentUptime = time.time()
                        currentUptimeII = currentUptime - end_startingtime
                        print(color.blue + "  ______   __     ___  ____  ")
                        print(" |  _ \ \ / /    / _ \/ ___| ")
                        print(color.cyan + " | |_) \ V /    | | | \___ \ ")
                        print(" |  __/ | |     | |_| |___) |")
                        print(" |_|    |_|      \___/|____/ " + color.reset)
                        print(color.purple + "      --- Improved ---       " + color.reset)
                        print(user + " " + lsh_hostname)
                        print("System:PY OS Improved " + system_version + " " + system_build)
                        print("Architecture:" + str(platform.machine()))
                        print("Python version:" + str(platform.python_version()))
                        print("Terminal:tty1")
                        print("Uptime:" + str(currentUptimeII) + "min")
                        print("Host:" + lsh_hostname)
                        print("CPU:Intel Pentium(133MHz)")
                        print("GPU:Cirrus Logic GD 5446(4MB)")
                        print("Memory: " + str(totalmem) + " Bytes")
                        print("Sound Card:GUS")
                        print("Ethernet Card:?")
                        print("Disk:HDD1=30GB, HDD2=55GB")
                    elif cmd == "uwufetch colotest256":
                        os.system("python3 ./apps/color256/color256.py")
                    elif cmd == "rss":
                        os.system("python3 ./apps/rss/main.py")
                    elif cmd == "crash":
                        badstring = uwu
                        anotherbadstring = "owo"
                        print(badstring + anotherbadstring)
                    elif cmd.startswith("echo "):
                        string = cmd[5:]
                        if string == "":
                            print("No string provided...")
                        else:
                            print(string)
                    elif cmd == "clock":
                        os.system("python3 ./apps/clock/clock.py")
                    elif cmd == "ttt":
                        os.system("python3 ./apps/tictactoe/tictactoe.py")
                    elif cmd == "paint":
                        paintWidthAndHeight = input("Input width and height(example:50 50): ")
                        os.system("cd ./savedfile && python3 ../apps/paint/paint.py " + paintWidthAndHeight + " && cd ..")
                    elif cmd == "pftest":
                        print("CPU Performance Test by minqwq")
                        print("2024-09-07")
                        os.system("python3 ./apps/pftest/mark.py")
                    elif cmd == "nekochat":
                        nekochatConnectToIP = input("Input server IP: ")
                        nekochatConnectToPort = input("Input server Port: ")
                        nekochatUsername = input("What's your name?: ")
                        print("Welcome to NekoChat Client(Python Port) by Yukari2024")
                        os.system("python3 ./apps/nekochat/py/client.py --ip " + nekochatConnectToIP + " --port " + nekochatConnectToPort + " --name " + nekochatUsername)
                    elif cmd == "demine":
                        os.system("./apps/minesweeper/minesweeper")
                    elif cmd == "fileget":
                        os.system("cd ./download && python3 ../apps/fileget/fileget.py && cd ..")
                    elif cmd == "uptime":
                        currentUptime = time.time()
                        print(currentUptime - end_startingtime)
                    elif cmd == "guessnum":
                        os.system("python3 ./apps/guessnum/guessnum.py")
                    elif cmd == "ping": # Ping tool
                        pingToolIPInput = input("Input IP or Domain: ")
                        pingToolCountInput = input("Send how many packages: ")
                        os.system("ping -c " + pingToolCountInput + " " + pingToolIPInput)
                    elif cmd == "fm":
                        os.system("./apps/ranger/ranger.sh")
                    elif cmd == "hostname":
                        print("add option -c to change.\n\nHostname:\n" + lsh_hostname)
                    elif cmd == "hostname -c":
                        lsh_hostname = input("> ")
                        if lsh_hostname == "":
                            print("No string provided.")
                            lsh_hostname = "tiramisu"
                    elif cmd == "sudo": # sudo not sudo
                        print("This system is not based on linux, so sudo is not on here")
                    elif cmd == "sticker":
                        os.system("cd ./apps/sticker && python3 sticker.py && cd ../..")
                    elif cmd == "about": # About system
                        print("---------------| About |---------------")
                        print(color.blue + "PY OS Improved " + system_version + " " + system_build + color.reset)
                        print(color.grey + "(C) 0x1c Studio 2022--2023 | (C) LR Studio & FCNM & StarHikari Studios 2024" + color.reset)
                        print(" ")
                        print("add option -c for credits\nadd option -s for support")
                    elif cmd == "about -c" or cmd == "about --credits":
                        print(colorama.Fore.LIGHTCYAN_EX + "Credits" + color.reset)
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Developers" + color.reset)
                        print("minqwq | Interface Design, Coder, Project Creator, Document Editer")
                        print("bibimingming | Module Installer")
                        print("AMDISYES(Original PY OS) | Original Project Creator")
                        print("Yukari2024 | Installer")
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Early developing tester(not sorted)" + color.reset)
                        print("minqwq")
                        print("bibimingming")
                        print("Safari_Browse(Rongxuan2022)")
                        print("AMDISYES")
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Special Thanks for these projects" + color.reset)
                        print("https://github.com/shkolovy/tetris-terminal | Used for games")
                        print("https://github.com/pipeseroni/pipes.sh | Used for screensaver")
                        print("http://154.64.231.6:3000/Yukari/Minesweeper | Used for games")
                        print("https://github.com/erkankavas/python-rss-reader | RSS Reader")
                    elif cmd == "about -s" or cmd == "about --support":
                        print("minqwq's social accounts:")
                        print("QQ:1617195774")
                        print("WeChat:minqwq723897")
                        print("E-mail:minqwq723897@outlook.com")
                        print("Telegram:@minqwq723897")
                        print("IRC(Instant only):minqwq #pyos-improved irc.freenode.net:6667")
                    elif cmd == "power":
                        print("Power options:")
                        print("Shutdown:shutdown or without start by power, st")
                        print("Restart:reboot or without start by power, rbt")
                        print(" ")
                        print("ex:power reboot")
                    elif cmd == "power shutdown" or cmd == "st": # Shutdown
                        d.set_background_title("PY OS Improved " + system_version + " " + system_build)
                        d.infobox("Shutting down...", width=0, height=0, title="Power manager")
                        time.sleep(3)
                        os.system("clear")
                        sys.exit()
                    elif cmd == "power reboot" or cmd == "rbt":
                        d.set_background_title("PY OS Improved " + system_version + " " + system_build)
                        d.infobox("Restarting...", width=0, height=0, title="Power manager")
                        time.sleep(3)
                        os.system("clear")
                        os.execv(sys.executable, ['python'] + sys.argv)
                    elif cmd == "screensaver": # Screensaver
                        os.system("cd ./apps/_screensaver && python3 scrsv.py && cd ../..")
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
                        os.system("python3 ./apps/tetris/tetris.py")
                    elif cmd == "mp":
                        os.system("cd ./apps/musicplayer && python3 musicplayer.py && cd ../..")
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
                        print("Color depth require:8bit at least")
                        ciallo_img = os.system("timg ./image/example/ciallo.jpeg")
                    elif cmd == "caesar":
                        os.system("cd ./apps/caesartools && python3 caesar.py && cd ../..")
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
                        os.system(customCommand)
                    elif cmd == "news":
                        requestsUrl = "https://www.minqwq.us.kg/pyosimproved/news/latest.txt"
                        requestsResponse = requests.get(requestsUrl)
                        if requestsResponse.status_code == 200:
                            print(colorama.Fore.LIGHTGREEN_EX + "STATUS:200(Success)\n" + color.reset)
                            requestsText = requestsResponse.text
                            print(requestsText)
                        else:
                            print("STATUS:" + requestsResponse.status_code + "(Failed)")
                    elif cmd.startswith("passwd "): # Change password(for this session)
                        stpasswd = cmd[7:]
                        if stpasswd == "":
                            print("No string provided")
                        else:
                            print("Password set to " + stpasswd)
                    elif cmd == "calendar": # Calendar
                        yy = int(input("Year: "))
                        mm = int(input("Month: "))
                        print(color.green + "PY OS Calendar\n" + color.reset + calendar.month(yy, mm))
                    elif cmd == "calcurse":
                        os.system("calcurse")
                    elif cmd == "help": # Command list
                        print("Larine Shell manual help:")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE + "(System)" + color.reset)
                        print("ls             View the path")
                        print("about          Show the system's information")
                        print("converter      A tool to convert .lpap/.lpcu/.bbc to .umm")
                        print("time           Show the time and date(Deteled in this version)")
                        print("calendar       Show a calendar")
                        print("clear          Clear the screen")
                        print(color.red + "passwd <str>   Change password for this session" + color.reset)
                        print("power          Power manager")
                        print("exit           Lock system")
                        print("hostname       Show hostname")
                        print("echo <str>     Print text to screen ")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE + "(Tools)" + color.reset)
                        print("calc           A simple calculator")
                        print("uwufetch       List all hardware and system version")
                        print("random         Random tools")
                        print(color.red + "perf           Performance tools" + color.reset)
                        print("notepad        a Text editor, very simple")
                        print("caesar         Caesar encryption tools")
                        print("fm             Ranger file manager")
                        print("sticker        notepad but can't save content")
                        print("fileget        Get any file from internet")
                        print("paint          Paint(image maker app)")
                        print("clock          Timer and clock")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE + "(Relax)" + color.reset)
                        print("mp             Play music")
                        print("screensaver    Save your VGA screen, make your pc like a pro")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE + "(Games)" + color.reset)
                        print("tetris         Tetris game written using Python")
                        print("guessnum       Guess number game written using Python")
                        print("demine         Minesweeper game written using C")
                        print("ttt            tic-tac-toe game written using Python")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE + "(Networking)" + color.reset)
                        print("nekochat       Online chatting client and server by Yukari2024")
                        print("ping           Ping tool")
                        print("rss            RSS Reader by erkankavas")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE +  "(Other)" + color.reset)
                        print("cuscmd         Run custom command")
                        print(color.red + "news           Show latest news of PY OS Improved." + color.reset)
                        print("uptime         Show (this)system uptime")
                        print("pftest         CPU Performance Test")
                        print("tutor          Help document for new")
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
                    elif cmd == "tutor":
                        os.system("cd ./apps/tutor && python3 tutor.py && cd ../..")
                    elif cmd == "": # what is this??? --minqwq at 2024-06-12 19:32
                        space = "0"
                    elif cmd == "clear": # Clear screen using real system command
                        os.system("clear")
                    elif cmd == "exit": # Logout
                        os.system("clear")
                        systemIsLocked = True
                        print("PY OS Improved " + system_version + " (Locked.)")
                        print("Press u and press enter to login account...")
                        print("or...\ntime   | View current time")
                        print("st   | Shutdown")
                        while systemIsLocked == True:
                            unlockSystem = input("")
                            if unlockSystem == "u":
                                systemIsLocked = False
                                os.system("clear")
                            elif unlockSystem == "time":
                                now = datetime.datetime.now()
                                other_StyleTime = now.strftime("%b %a %d %H:%M:%S %Y")
                                print(other_StyleTime)
                            elif unlockSystem == "st":
                                os.system("clear")
                                sys.exit()
                        startingtime = "?"
                        end_startingtime = "?"
                        startingtime_t = "?"
                        goto(line=233)
                    else: # Wrong command
                        pygame.mixer.music.load("./audio/se/err.mp3")
                        pygame.mixer.music.play()
                        print(text.error + color.red + "i can't seem to find the command >.<" + color.reset)
                        print(color.red + "[Unknown command]" + color.reset, end=' ')
            except Exception as crashReason:
                print(colorama.Fore.LIGHTRED_EX + ":(\n\nPY OS Improved has been crashed!\n" + str(crashReason) + "\n" + str(traceback.print_exc()) + "\nSystem Information:\n" + system_version + " " + system_build + "\n")
                os.system("uname")
                input("[CRASH - Press any key to shutdown]" + color.reset)
                sys.exit()
