# DONT CHANGE ANY IMPORTED MODULES NAME, IM SERIOUS
#
# PY OS Improved -- Open-source "Operating System(OS)" written using Python 3
# Make sure you have Python 3.9 or higher, lower version is not tested
# Project creator:minqwq / LR Studio 2024
# 
# For our developer:
# After you write code finished, please add comment(s) in your code nearby, you maybe know why.

# How to add a quick jump for vim?:
# add comment with some special word(like uw1 uw2 ..)
# Press esc and type /uw1 to quick jump.

# (Chinese)
# 为什么我不想像那样重构:我懒。
# 所以我想出了一个办法，它基于编辑器的搜索功能
# 只需在某个地方加上注释，然后输入一些字(不要和已有的注释同名即可)
# 之后你只需使用搜索功能搜索这个注释你就可以快速定位了
# --minqwq | 2024-10-05
#
# 在需要显示反斜杠到屏幕的情况下，请输入两个反斜杠，这是一个兼容性问题
# --minqwq | 2024-10-07
import argparse
from python_goto import goto # Goto a line
import json # Read json file(config file need this)
conf = open("./config/conf.json", "r", encoding="utf-8")
jsonRead = json.load(conf)
parser = argparse.ArgumentParser( prog='PY OS Improved', description='Ultimate fake operating system!', epilog='If you have issues, go to our official github repo.')
parser.add_argument("-v", "--version", action="version", version=jsonRead["system_version"])
import time as tm # Time
import getpass # Password?
import calendar # Calendar
import os # Communicate to your system
import sys # idk
import datetime
import colorama
import time # Time
# import socket
# import struct
# import select
import random # Random tools
import uuid # Generate uuid
from os import path # Path control
# import rich.spinner # idk
# sys.path.append("./")
import platform
# import rich
import requests # Get file from server
import pretty_errors # Crash screen replace
import base64 # Encode and decode
# import tqdm # Progress bar
import traceback
import logging # Log.
import profile # Maybe useless?
import re
print("\033[?25l")
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
    no = color.red + "[X]" + color.reset
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
class style_cur:
    hide = "\033[?25l"
    show = "\033[?25h"
class override:
    errorexpection = "teto:ErrorExpection"
    tongue = "teto:a-------"
def echo(string):
    print(string)
pretty_errors.configure(
    postfix               = '!!! FALLBACK CRASH SCREEN !!!\nPY OS Improved has been crashed.\nRestart command:python pyosimproved.py\nReport this error!:https://github.com/minqwq/pyos-improved/issues',
    separator_character   = '#',
    line_color            = colorama.Fore.LIGHTBLUE_EX + 'Here > ' + color.reset,
)
print("config updated for pretty-errors")
try:
    os.remove("output.log")
except FileNotFoundError:
    pass
LOG_FORMAT = '[%(levelname)s] %(asctime)s | %(message)s'
logging.basicConfig(filename='output.log', datefmt='%b %a %d %H:%M:%S %Y', level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.info("Logger started successfully.")
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
        elif psutol.sensors_battery().percent > 11:
            print("Warning: Battery percent is very low now...(10%)")
        elif psutil.sensors_battery().percent > 6:
            print("Warning: Why not go to charge battery now?(5%)")
    except FileNotFoundError:
        pass
pyosimprovedtips = ["Official forum:https://minqwq.proboards.com/board/10/py-os-improved", "awa", "Also try original PY OS! link available after login.", "No stay back gordon!", "sjsjsjnwnwjsosjq????"]
print("Tips loaded success")
os.system("alias cls=clear")

# CONFIG START

system_version = jsonRead["system_version"] # 版本号
system_codename = jsonRead["system_codename"]
system_build = jsonRead["system_build"] # 每做一个修改或增减内容，就加一个 Build
system_is_beta = True # 是否为 Beta 版
isWindows = jsonRead["isWindows"] # 是否为 Windows
cmd_theme = jsonRead["cmd_theme"] # 终端 Shell 主题
isDev = False # 是否为 Dev 模式

# CONFIG END

# BIOS Animation
# with open("./config/conf.json", "w", encoding="utf-8") as temp_writeConfig:
if jsonRead["isWindows"] == "":
    # print("Unknown OS type, please set one.\nfalse:Linux\ntrue:Windows")
    # conf_isWindows_write = input(">")
    if conf_isWindows_write == "false":
        pass
        # 这不会写，帮我写一下，就是把配置文件里的"isWindows"值改成"false"("isWindows": "false")
    elif conf_isWindows_write == "true":
        pass
        # 这里和上面一样，不过false改成true
    print("Please configure the 'isWindows' to false or true on config/conf.json\nIt's looks like this:\"isWindows\": \"\", Change it to:\n\"isWindows\": \"false\" If you are linux\n\"isWindows\": \"true\" If you are windows")
    print("Exiting...")
    sys.exit()
def clearScreen():
    if isWindows == "true":
        os.system("cls")
    elif isWindows == "false":
        os.system("clear")
def beep():
    print("\a", end="\r")
if sys.platform.startswith("linux") or sys.platform.startswith("posix"):
    print("If you dont have 'python' command, please set alias 'python=python3'")
temp_clock1 = time.time()
print("Press d to fastboot.\nElse, press enter" + style_cur.show)

if temp_clock1 < 2:
    goto(line=181)
debugMode = input("\n")
if debugMode == "d":
    now = datetime.datetime.now()
    startingtime_t = "???"
    end_startingtime = "???"
    startingtime = "???"
    print("You are now in debug mode.")
    print("If crash, dont report ANY error.")
    goto(line=250)
print(style_cur.hide)
import psutil
print("module import: psutil")
print(colorama.Back.LIGHTRED_EX + colorama.Fore.LIGHTYELLOW_EX + "E:NO SINGAL" + color.reset)
time.sleep(2)
clearScreen()
print("_")
time.sleep(0.5)
clearScreen()
print(" ")
time.sleep(0.5)
clearScreen()
print("_")
time.sleep(0.5)
clearScreen()
slowprint(colorama.Fore.LIGHTGREEN_EX + "minsoft 2011--2025 No lefts unserved")
slowprint("EveryBooter v1.0")
slowprint("Testing memory...")
time.sleep(0.15)
for memtest in range(int(psutil.virtual_memory().total / 1024 / 1024)):
    print(str(memtest), end="\r")
    time.sleep(0.0005)
beep()
print(str(round(int(psutil.virtual_memory().total / 1024 / 1024))) + "MB OK")
time.sleep(0.5)
profile.run("re.compile")
time.sleep(1.5)
clearScreen()
print(color.reset)
time.sleep(0.1)
# Boot manager
bootManagerLoopRun = True
logger.info("Start logging.")
logger.info("Starting PY OS Improved Boot manager.")
print(colorama.Fore.LIGHTCYAN_EX + "PY OS Improved Boot manager" + color.reset + style_cur.show)
print("If you dont know which to choose, choose 1.")
print("\n1:PY OS Improved " + system_version + "\n2:Reboot\n3:Shutdown\n4:PY OS Improved Pre-Alpha 1\n5:BBC OS 1.2.1")
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
        clearScreen()
        print("If you want exit, press Ctrl+C to shutdown")
        os.system("python ./.earlysystem/pyosimproved.py")
        sys.exit()
    elif bootChoice == "5":
        clearScreen()
        print("If you want exit, press Ctrl+C to shutdown")
        os.system("python ./.earlysystem/bbcos-full.py")
        sys.exit()
    else:
        clearScreen()
        goto(line=176)
clearScreen()
# Startup screen
logger.info("Starting main operating system...")
startingtime = time.time()
os.system("python apps/coreutils/startuplogo/animatedlogo.py")
print(" " + style_cur.hide)
print(random.sample(pyosimprovedtips, 1))
print(" ")
if system_is_beta == True: # If is beta version, show this warn
    print(text.error + colorama.Fore.LIGHTYELLOW_EX + "Beta version" + color.reset)
print(colorama.Fore.LIGHTRED_EX + "Flandre" + color.reset + "/" + "\033[38;5;45m" + "PY " + "\033[38;5;81m" + "OS " + "\033[38;5;117m" + "Im" + "\033[38;5;153m" + "pr" + "\033[38;5;189m" + "ov" + "\033[38;5;225m" + "ed" + color.reset + " | " + system_version + " | " + system_build)
print("Codename " + system_codename + color.reset)
print("The Physical You(PY) OS logos is not are registered trademark, you can use it on anywhere.")
print("Original by AMDISYES | Improved Version by minqwq & bibimingming ヽ(✿ﾟ▽ﾟ)ノ")
print(" ")
print("PY OS Improved is a open source software and you can share it freedomly")
print("Under \"minqwq's License\" 1.0 License.")
print(colorama.Fore.LIGHTCYAN_EX + "Feel free to improve PY OS Improved!" + color.reset)
print(" ")
print("(C) " + color.green + "0x1c Studio " + color.reset + "2022--2023 | (C) " + colorama.Fore.LIGHTRED_EX + "Flandre" + color.red + " Studio " + color.reset + "&" + color.grey + " FCNM " + color.reset + "&" + color.grey + " SnowMio Studios 2022--2025" + color.reset)
print("The PY OS Improved Project 2024/06/06--Today")
print(" ")
time.sleep(3)
clearScreen()
time.sleep(0.1)
end_startingtime = time.time()
startingtime_t = end_startingtime - startingtime
beep()
logger.info("Welcome to PY OS Improved!")
print(colorama.Fore.LIGHTCYAN_EX + "Hewwwo wewcome back to PY OS Improved senpai >.<" + color.reset + style_cur.show) # Login screen | For restart to login manager, please goto this line for work normally
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
        pass
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
            clearScreen()
        d.infobox("Look back~", width=0, height=0, title="From Koishi")
        time.sleep(0.1)
        clearScreen()
        print("You have been kicked by Komeiji Koishi.\nPlease r???\nP??\nPlease re-lo??..gin.")
    else:
        isCreatorAccount = False
        while count < 3:
            try:
                clearScreen()
                lshdate = now.strftime("%Y-%m-%d")
                lshtime = now.strftime("%H:%M:%S")
                lsh_hostname = "ayaya"
                if user == "minqwq":
                    # password_pre = b"aWxvdmVtaW8="
                    # password = base64.b64decode(password_pre)
                    # inputpass = bytes(input(), encoding="utf-8")
                    creatorVerifyPassword = base64.b64decode(b"cXdlMTE1MDYx")
                    creatorVerify = bytes(getpass.getpass("Verify required, please type password...\n> "), encoding="utf-8")
                    if creatorVerify == creatorVerifyPassword:
                        clearScreen()
                        print("The creator of PY OS Improved, welcome back.\n")
                        user = colorama.Fore.LIGHTBLUE_EX + "(CRTRACT) minqwq" + color.reset
                        isCreatorAccount = True
                    else:
                        print(color.red + "Access Denied." + color.reset)
                        sys.exit()
                elif user == "dev":
                    clearScreen()
                    print("You are trying to login dev account, please input the password below:")
                    deVerify = input("")
                    if deVerify == "ilovemio":
                        isDev = True
                    else:
                        clearScreen()
                        sys.exit()
                beep()
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
                os.system("python autoexec.py")
                if isDev == True:
                    print("Logged into dev account, some command may unlocked!")
                print("\nLarine SHell (lsh) version 1.6.1 >///<\nit's a wittwe user non-fwiendwy shell...")
                while count < 3:
                    if cmd_theme == "default":
                        cmd_pre = colorama.Fore.LIGHTBLUE_EX + user + color.grey + ":" + colorama.Fore.LIGHTCYAN_EX + lsh_hostname + colorama.Fore.LIGHTGREEN_EX + " > " + color.reset
                    elif cmd_theme == "lite":
                        cmd_pre = colorama.Fore.GREEN + user + colorama.Fore.LIGHTGREEN_EX + " : " + color.reset
                    elif cmd_theme == "debian_bash":
                        cmd_pre = colorama.Fore.LIGHTGREEN_EX + user + "@" + lsh_hostname + color.reset + ":" + colorama.Fore.LIGHTBLUE_EX + "~" + color.reset + "$ "
                    elif cmd_theme == "arch_bash":
                        cmd_pre = "[" + user + "@" + lsh_hostname + " ~ ] $ "
                    else:
                        print("Theme not found! falling to default.")
                        print("Available theme name:default, lite, debian_bash, arch_bash")
                        cmd_theme = "default"
                  # Line 246 is a critical process, dont change it   --minqwq
                    lsh_time_prepare = datetime.datetime.now()
                    lsh_time = lsh_time_prepare.strftime("%H:%M:%S")
                    print("[" + lsh_time + "]", end=" ")
                  # lsh_username = os.system("whoami")
                    cmd = input(cmd_pre)
                    logger.info("[Command] tty1/lsh: " + cmd)
                    cbatteryperc() # Check battery percent
                    if cmd == "ls": # Path
                        if isWindows == True:
                            print("root path:")
                            os.system("ls ./")
                            print("programs path:")
                            os.system("ls ./apps/")
                            print("music path:")
                            os.system("ls ./music/")
                        elif isWindows == False:
                            print("root path:")
                            os.system("dir .\\")
                            print("programs path:")
                            os.system("dir .\\apps")
                            print("music path:")
                            os.system("dir .\\music")
                    elif cmd == "uwufetch": # a Fake neofetch
                        currentUptime = time.time()
                        currentUptimeII = currentUptime - end_startingtime
                        print(color.blue + "  ______   __     ___  ____  ")
                        print(" |  _ \ \ / /    / _ \/ ___| ")
                        print(color.cyan + " | |_) \ V /    | | | \___ \ ")
                        print(" |  __/ | |     | |_| |___) |")
                        print(" |_|    |_|      \___/|____/ " + color.reset)
                        print(color.purple + "      --- Improved ---       " + color.reset)
                        print(user + "@" + lsh_hostname)
                        print("System:PY OS Improved " + system_version + " " + system_build)
                        print("Running on:", end="")
                        running_on = str(os.system("python ./apps/coreutils/tinythings/detectdistro_linux/distrodetect.py"))
                        print("Architecture:" + str(platform.machine()))
                        print("Python version:" + str(platform.python_version()))
                        print("External programs:" + str(dir_filecount("./extprog")) + "(extprog)")
                        print("Terminal:tty")
                        print("Uptime:" + str(round(int(currentUptimeII))) + " s")
                        print("Host:" + lsh_hostname)
                        print("CPU:Intel Pentium(133MHz)")
                        print("GPU:Cirrus Logic GD 5446(4MB)")
                        print("Memory: " + str(round(int(psutil.virtual_memory().total / 1024 / 1024))) + " MB")
                        print("Sound Card:?")
                        print("Ethernet Card:?")
                        print("Disk:HDD1=30GB, HDD2=55GB")
                    elif cmd == "uwufetch colotest256":
                        os.system("python ./apps/color256/color256.py")
                    elif cmd == "ed":
                        os.system("python ./apps/ed-editor/edit.py")
                    elif cmd.startswith("extprog"):
                        os.system("python ./extprog/__main__.py")
                    elif cmd.startswith("chthm"):
                        cmd_theme = cmd[6:]
                        logger.info("Shell theme changed to " + cmd[16:])
                        print("Successfully seted shell theme " + cmd[16:])
                    elif cmd == "conf":
                        print("Remaking")
                    elif cmd == "asciicvt":
                        os.system("python ./apps/asciicvt/asciiconverter.py")
                    elif cmd == "tasks":
                        os.system("cd ./savedfile/tasks && ../../apps/tasks/tasks && cd ../..")
                    elif cmd == "2048":
                        os.system("./apps/2048/2048-in-terminal")
                    elif cmd.startswith("rm"):
                        rmFile = cmd[3:]
                        if rmFile == "":
                            print("No string provided.")
                        else:
                            os.remove(rmFile)
                    elif cmd.startswith("rmdir"):
                        rmDir = cmd[6:]
                        if rmDir == "":
                            print("No string provided.")
                        else:
                            os.rmdir(rmDir)
                    elif cmd.startswith("su"):
                        user_preInput = cmd[3:]
                        if user_preInput == "":
                            print("Please type you want to login super user.")
                        elif user_preInput == "minqwq":
                            print("If you know the password, please reboot and try to login to this account.")
                        elif user_preInput == "minimalmio" or user_preInput == "MinimalMio" or user_preInput == "Minimal_Mio" or user_preInput == "minimal_mio":
                            print("Sorry, you dont have permission to login to this account, if you want, reboot to login manager.")
                        else:
                            user = user_preInput
                            print("Logged in as " + user)
                            logger.info("[Login manager] Switch user to " + user)
                    elif cmd == "rss":
                        os.system("python ./apps/rss/main.py")
                    elif cmd == "crash":
                        if user == "dev":
                            logger.warn("Congrats, you make the PY OS Improved crashed.")
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
                        os.system("python ./apps/clock/clock.py")
                    elif cmd == "ttt":
                        os.system("python ./apps/tictactoe/tictactoe.py")
                    elif cmd == "paint":
                        paintWidthAndHeight = input("Input width and height(example:50 50): ")
                        os.system("cd ./savedfile && python ../apps/paint/paint.py " + paintWidthAndHeight + " && cd ..")
                    elif cmd == "pftest":
                        print("CPU Performance Test by minqwq")
                        print("2024-09-07")
                        os.system("python ./apps/pftest/mark.py")
                    elif cmd == "nekochat":
                        nekochatConnectToIP = input("Input server IP: ")
                        nekochatConnectToPort = input("Input server Port: ")
                        nekochatUsername = input("What's your name?: ")
                        print("Welcome to NekoChat Client(Python Port) by Yukari2024")
                        os.system("python ./apps/nekochat/py/client.py --ip " + nekochatConnectToIP + " --port " + nekochatConnectToPort + " --name " + nekochatUsername)
                    elif cmd == "demine":
                        os.system("./apps/minesweeper/minesweeper")
                    elif cmd == "fileget":
                        os.system("cd ./download && python ../apps/fileget/fileget.py && cd ..")
                    elif cmd == "uptime":
                        currentUptime = time.time()
                        print(currentUptime - end_startingtime)
                    elif cmd == "guessnum":
                        os.system("python ./apps/guessnum/guessnum.py")
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
                        os.system("cd ./apps/sticker && python sticker.py && cd ../..")
                    elif cmd == "about": # About system
                        slowprint("---------------| About |---------------")
                        print(color.blue + "PY OS Improved " + system_version + " " + system_build + color.reset)
                        print("(C) " + color.green + "0x1c Studio " + color.reset + "2022--2023 | (C) " + colorama.Fore.LIGHTRED_EX + "Flandre" + color.red + " Studio " + color.reset + "&" + color.grey + " FCNM " + color.reset + "&" + color.grey + " SnowMio Studios 2022--2025" + color.reset)
                        print("The PY OS Improved Project 2024/06/06--Today")
                        print(" ")
                        print("add option -c for credits\nadd option -s for support")
                    elif cmd == "about -c" or cmd == "about --credits":
                        print(colorama.Fore.LIGHTCYAN_EX + "Credits" + color.reset)
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Developers" + color.reset)
                        print("minqwq | Interface Design, Coder, Project Creator, Document Editer")
                        print("bibimingming | Module Installer")
                        print("MeltedIde aka MeltedIce aka AMDISYES(Original PY OS) | Original Project Creator")
                        print("MinimalMio aka Yukari2024 | Installer")
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Early developing tester(not sorted)" + color.reset)
                        print("minqwq")
                        print("bibimingming")
                        print("Safari_Browse(Rongxuan2022)")
                        print("MeltedIce aka AMDISYES")
                        print(colorama.Back.WHITE + colorama.Fore.BLACK + "Special Thanks for these projects" + color.reset)
                        print("https://github.com/shkolovy/tetris-terminal | Used for games")
                        print("https://github.com/pipeseroni/pipes.sh | Used for screensaver")
                        print("http://154.64.231.6:3000/Yukari/Minesweeper | Used for games")
                        print("https://github.com/erkankavas/python-rss-reader | RSS Reader")
                        print("https://github.com/alewmoose/2048-in-terminal | Used for games")
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
                    elif cmd == "power shutdown" or cmd == "st" or cmd == ":q": # Shutdown
                        logger.info("Shutting down.")
                        clearScreen()
                        sys.exit()
                    elif cmd == "power reboot" or cmd == "rbt":
                        logger.info("Restarting.")
                        clearScreen()
                        os.execv(sys.executable, ['python'] + sys.argv)
                    elif cmd == "screensaver": # Screensaver
                        os.system("cd ./apps/_screensaver && python scrsv.py && cd ../..")
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
                        os.system("python ./apps/tetris/tetris.py")
                    elif cmd == "mp":
                        os.system("cd ./apps/musicplayer && python musicplayer.py && cd ../..")
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
                    elif cmd == "uname":
                        print(os.uname())
                    elif cmd == "caesar":
                        os.system("cd ./apps/caesartools && python caesar.py && cd ../..")
                    elif cmd == "cuscmd":
                        print("Type custom command below...(ex:cat ciallo.txt)")
                        customCommand = input("")
                        os.system(customCommand)
                    elif cmd == "news":
                        try:
                            requestsUrl = "https://www.minqwq.us.kg/pyosimproved/news/latest.txt"
                            requestsResponse = requests.get(requestsUrl)
                            if requestsResponse.status_code == 200:
                                print(colorama.Fore.LIGHTGREEN_EX + "STATUS:200(Success)\n" + color.reset)
                                requestsText = requestsResponse.text
                                print(requestsText)
                        except Exception:
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
                        print("rm <str>       Remove file")
                        print("rmdir <str>    Remove directory")
                        print("su <str>       Switch user")
                        print("rss            RSS Feed reader")
                        print("conf           Show the current config")
                        print("chthm <name>   Change theme of the shell")
                        print("extprog        Run external program")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE + "(Tools)" + color.reset)
                        print("calc           A simple calculator")
                        print("uwufetch       List all hardware and system version")
                        print("caesar         Caesar encryption tools")
                        print(color.red + "fm             Ranger file manager" + color.reset)
                        print("sticker        notepad but can't save content")
                        print("fileget        Get any file from internet")
                        print("paint          Paint(image maker app)")
                        print("clock          Timer and clock")
                        print("tasks          Critical tasks now will never forgot again.")
                        print("asciicvt       ASCII Converter")
                        print("ed             Line text editor")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE + "(Relax)" + color.reset)
                        print("mp             Play music")
                        print("screensaver    Save your VGA screen, make your pc like a pro")
                        print(colorama.Back.LIGHTBLUE_EX + colorama.Fore.WHITE + "(Games)" + color.reset)
                        print("tetris         Tetris game written using Python")
                        print("guessnum       Guess number game written using Python")
                        print("demine         Minesweeper game written using C")
                        print("ttt            tic-tac-toe game written using Python")
                        print("2048           2048 in Terminal")
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
                        os.system("cd ./apps/tutor && python tutor.py && cd ../..")
                    elif cmd == "": # what is this??? --minqwq at 2024-06-12 19:32
                        space = "0"
                    elif cmd == "clear": # Clear screen using real system command
                        clearScreen()
                    elif cmd == "exit": # Logout
                        clearScreen()
                        systemIsLocked = True
                        print("PY OS Improved " + system_version + " (Locked.)")
                        print("Press u and press enter to login account...")
                        print("or...\ntime   | View current time")
                        print("st   | Shutdown")
                        while systemIsLocked == True:
                            unlockSystem = input("")
                            if unlockSystem == "u":
                                systemIsLocked = False
                                clearScreen()
                            elif unlockSystem == "time":
                                now = datetime.datetime.now()
                                other_StyleTime = now.strftime("%b %a %d %H:%M:%S %Y")
                                print(other_StyleTime)
                            elif unlockSystem == "st":
                                clearScreen()
                                sys.exit()
                        startingtime = "?"
                        end_startingtime = "?"
                        startingtime_t = "?"
                        goto(line=244)
                    else: # Wrong command
                        beep()
                        print(text.error + color.red + "i can't seem to find the command >.<" + color.reset)
                        print(color.red + "[Unknown command]" + color.reset, end=' ')
                        logger.error("tty1/lsh: " + cmd + ": Command not found!")
            except KeyboardInterrupt: # Ctrl+C, "Ctrl+Alt+Del" like action
                try:
                    slowprint("\nPress 1 to restart\nPress other key to back\nor Press Ctrl+C again to shutdown...")
                    emergencyChoice = input()
                    if emergencyChoice == "1":
                        goto(line=157)
                except KeyboardInterrupt:
                    clearScreen()
                    sys.exit()
            except Exception as crashReason: # Crash
                print(colorama.Fore.LIGHTRED_EX + ":(\n\nPY OS Improved has been crashed!\n" + str(crashReason) + "\n" + str(traceback.print_exc()) + "\nSystem Information:\n" + system_version + " " + system_build + "\n")
                os.system("uname")
                traceback.print_exc(file="latestcrash.log")
                logger.critical("PY OS Improved has been crashed by some unexpected error o(╥﹏╥)o : な、何か予期しないエラーが発生しましたにゃ (⁄ ⁄•⁄ω⁄•⁄ ⁄)")
                input("[CRASH - Press any key to shutdown]" + color.reset)
                sys.exit()
