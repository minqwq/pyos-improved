import time as tm
import getpass
import datetime
import calendar
import os
import sys
import time
# BIOS Animation
print("cleaning screen...")
i = os.system("cls")
i = os.system("clear")
time.sleep(0.5)
print("_")
i = os.system("cls")
i = os.system("clear")
time.sleep(0.5)
print(" ")
i = os.system("cls")
i = os.system("clear")
time.sleep(0.5)
print("_")
i = os.system("cls")
i = os.system("clear")
time.sleep(0.5)
print(" ")
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
i = os.system("mpg123 -q ./beep.mp3")
print("Access BIOS v8.1")
print("bios.mcpestudio.com/release/8/1/0/index.html")
time.sleep(0.3)
print("Testing Memory...")
time.sleep(0.5)
print("512MB OK")
time.sleep(0.1)
print("Booting From Hard Disk...")
time.sleep(1)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
# Startup screen
print("  ______   __     ___  ____  ")
print(" |  _ \ \ / /    / _ \/ ___| ")
print(" | |_) \ V /    | | | \___ \ ")
print(" |  __/ | |     | |_| |___) |")
print(" |_|    |_|      \___/|____/ ")
print("      --- Improved ---       ")
print(" ")
print("\033[31mPY\033[0m \033[33mOS\033[0m \033[34mImproved\033[0m | Version 1.0(Alpha 3 | Build 13)")
print("Original by AMDISYES | Improved Version by minqwq ヽ(✿ﾟ▽ﾟ)ノ")
print("This screen will show 5 second")
print(" ")
print("Make sure always are latest version!")
print("Update trick:shutdown PY OS Improved and type 'git pull' on pyos-improved folder to update system")
print(" ")
print("Current source code lines:162")
time.sleep(5)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
print("[INFO] Begin of logging")
time.sleep(0.05)
print("[...] Waking up system-process...")
time.sleep(0.25)
print("[O] system-process is waked up")
time.sleep(0.1)
print("[...] Detecting hardwares...")
time.sleep(0.5)
print("[O] Hardware list updated")
time.sleep(0.05)
print("[...] Waking up user-manager")
time.sleep(0.1)
print("[...] Waking up login-manager")
time.sleep(0.2)
print("[O] user-manager is waked up")
time.sleep(0.1)
print("[O] login manager is waked up")
time.sleep(0.5)
i = os.system("cls")
i = os.system("clear")
time.sleep(0.1)
i = os.system("mpg123 -q ./startup.mp3")
print("Hi~ o(*￣▽￣*)ブ My master~ Welcome back to PY OS Improved~") # Login screen
count = 0
stpasswd = "45450721"
while count < 3:
    user = input("Account login: ")
    if user == "root":
        i = os.system("mpg123 -q ./beep.mp3")
        print("This account has been protected by password, please type password(45450721)")
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
                i = os.system("mpg123 -q beep.mp3")
                tm.sleep(1.5)
                while count < 3:
                    cmd = input("root@pyosi ~ > ") # Standard commands
                    if cmd == "ls":
                        print("Downloads  Documents  Music  Pictures")
                    elif cmd == "neofetch":
                        print("  ______   __     ___  ____  ")
                        print(" |  _ \ \ / /    / _ \/ ___| ")
                        print(" | |_) \ V /    | | | \___ \ ")
                        print(" |  __/ | |     | |_| |___) |")
                        print(" |_|    |_|      \___/|____/ ")
                        print("      --- Improved ---       ")
                        time.sleep(0.1)
                        print("System:PY OS Improved 1.0 a3 b13")
                        time.sleep(0.1)
                        print("CPU:Intel Pentium 4@1400MHz")
                        time.sleep(0.1)
                        print("GPU:Cirrus Logic GD 5446(4MB)")
                        time.sleep(0.1)
                        print("Memory:512MB DDR2")
                        time.sleep(0.1)
                        print("Sound Card:Speaker")
                        time.sleep(0.1)
                        print("Ethernet Card:NE2K_PCI")
                        time.sleep(0.1)
                        print("Disk:HDD1=30GB, HDD2=55GB")
                    elif cmd == "sudo":
                        print("This system is not based on linux, so sudo is not on here")
                    elif cmd == "about":
                        print("---------------| About |---------------")
                        print("PY OS Improved 1.0 a3(Build 13")
                        print("(C) 0x1c Studio 2022--2023 | (C) LR Studio 2024")
                    elif cmd == "shutdown":
                        i = os.system("mpg123 -q ./shutdown.mp3")
                        print("[...] Killing all process...")
                        time.sleep(1)
                        sys.exit()
                    elif cmd == "converter":
                        print("File Convert\nConvert .lpap/.lpcu/.bbc to .umm")
                        input("Input file's path:\n")
                        for i in range(1, 101):
                            print("\r", end="")
                            print("Progress: {}%: ".format(i), "=" * (i // 2), end="")
                            sys.stdout.flush()
                            tm.sleep(0.05)
                        print("\nConvert Complete")
                    elif cmd == "time":
                        now = datetime.datetime.now()
                        other_StyleTime = now.strftime("\nCurrent time:%Y-%m-%d %H:%M:%S")
                        print(other_StyleTime)
                    elif cmd == "passwd":
                        stpasswd = input("Input new password of this account: ")
                    elif cmd == "calendar":
                        yy = int(input("Year: "))
                        mm = int(input("Month: "))
                        print(calendar.month(yy, mm))
                    elif cmd == "help":
                        print("Command List:")
                        print("ls             View the path")
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
                    elif cmd == "calc":
                        try:
                            formula = input("Enter the formula to be calculated:\n")
                            print(formula + "=", eval(formula))
                        except Exception as e:
                            print("Input error.")
                    elif cmd == "":
                        space = "0"
                    elif cmd == "clear":
                        i = os.system("cls")
                        i = os.system("clear")
                    elif cmd == "exit":
                        break
                    else:
                        print("Shell:Command not found.")
            else:
                print("Password Incorrect, please try again")
    else:
        print("User not found, try another")
