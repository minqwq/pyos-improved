import time as tm
import getpass
import datetime
import calendar
import os
import sys
import time
<<<<<<< HEAD
print("Access BIOS v8.1") # BIOS Animation
=======
print("Access BIOS v8.1")
>>>>>>> bb32b0dce7029dc932388504957085d212491adf
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
<<<<<<< HEAD
print("  ______   __     ___  ____  ") # Startup screen
=======
print("  ______   __     ___  ____  ")
>>>>>>> bb32b0dce7029dc932388504957085d212491adf
print(" |  _ \ \ / /    / _ \/ ___| ")
print(" | |_) \ V /    | | | \___ \ ")
print(" |  __/ | |     | |_| |___) |")
print(" |_|    |_|      \___/|____/ ")
print("      --- Improved ---       ")
print(" ")
<<<<<<< HEAD
print("\033[31mPY\033[0m \033[33mOS\033[0m \033[34mImproved\033[0m | Version 1.0(Alpha 1 | Build 8)")
print("Original by AMDISYES | Improved Version by minqwq ヽ(✿ﾟ▽ﾟ)ノ")
=======
print("\033[31mPY\033[0m \033[33mOS\033[0m \033[34mImproved\033[0m | Version 1.0(Alpha 1 | Build 7)")
print("Original by AMDISYES | Improved Version by minqwq")
>>>>>>> bb32b0dce7029dc932388504957085d212491adf
print("This screen will show 5 second")
print(" ")
print("Make sure always are latest version!")
print("Update trick:shutdown PY OS Improved and type 'git pull' on pyos-improved folder to update system")
time.sleep(5)
i = os.system("cls")
i = os.system("clear")
<<<<<<< HEAD
print("Hi~ o(*￣▽￣*)ブ Welcome back to PY OS Improved~") # Login screen
=======
>>>>>>> bb32b0dce7029dc932388504957085d212491adf
count = 0
stpasswd = "45450721"
while count < 3:
    user = input("Account login: ")
    if user == "root":
        print("This account has been protected by password, please type password(45450721)")
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
                tm.sleep(1.5)
                while count < 3:
                    cmd = input("root@pyosi ~ > ") # Standard commands
                    if cmd == "ls":
                        print("Downloads  Documents  Music  Pictures")
                    elif cmd == "hardwarelist":
                        print("CPU:Intel Pentium 4@1400MHz")
                        print("GPU:Cirrus Logic GD 5446(4MB)")
                        print("Memory:512MB DDR2")
                        print("Sound Card:Speaker")
                        print("Ethernet Card:NE2K_PCI")
                        print("Disk:HDD1=30GB, HDD2=55GB")
                    elif cmd == "sudo":
                        print("This system is not based on linux, so sudo is not on here")
                    elif cmd == "about":
                        print("---------------| About |---------------")
<<<<<<< HEAD
                        print("PY OS Improved 1.0 a1(Build 8)")
=======
                        print("PY OS Improved 1.0 a1(Build 7)")
>>>>>>> bb32b0dce7029dc932388504957085d212491adf
                        print("(C) 0x1c Studio 2022--2023 | (C) LR Studio 2024")
                    elif cmd == "shutdown":
                        print("Shutting down...")
                        time.sleep(3)
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
                        print("hardwarelist   List all hardware on this computer")
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
