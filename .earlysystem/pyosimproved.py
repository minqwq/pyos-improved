import time as tm
import getpass
import datetime
import calendar
import os
import sys
def rprint(string):
    print(string)
rprint("PY OS Improved | Version 1.0(Pre Alpha | Build 1)")
rprint("Original by AMDISYES | Improved Version by minqwq")
count = 0
stpasswd = "114514"
while count < 3:
    user = input("Account login: ")
    if user == "root":
        rprint("This account has been protected by password, please type password")
        while count < 3:
            passwd = getpass.getpass("Password: ")
            if passwd == stpasswd:
                tm.sleep(1.5)
                while count < 3:
                    cmd = input("root@pyosi ~ > ")
                    if cmd == "ls":
                        rprint("Downloads  Documents  Music  Pictures")
                    elif cmd == "about":
                        rprint("---------------| About |---------------\n")
                        rprint("PY OS Improved 1.0pre-a(Build 1)\n")
                        rprint("(C) 0x1c Studio 2022--2023 | (C) LR Studio 2024")
                    elif cmd == "converter":
                        rprint("File Convert\nConvert .lpap/.lpcu/.bbc to .umm")
                        input("Input file's path:\n")
                        for i in range(1, 101):
                            rprint("\r", end="")
                            rprint("Progress: {}%: ".format(i), "=" * (i // 2), end="")
                            sys.stdout.flush()
                            tm.sleep(0.05)
                        rprint("\nConvert Complete")
                    elif cmd == "time":
                        now = datetime.datetime.now()
                        other_StyleTime = now.strftime("\nCurrent time:%Y-%m-%d %H:%M:%S")
                        rprint(other_StyleTime)
                    elif cmd == "passwd":
                        stpasswd = input("Input new password of this account: ")
                    elif cmd == "calendar":
                        yy = int(input("Year: "))
                        mm = int(input("Month: "))
                        rprint(calendar.month(yy, mm))
                    elif cmd == "help":
                        rprint("ls          View the path")
                        rprint("version     Show the system's version")
                        rprint("coverter    A tool to covert .lpap/.lpcu/.bbc to .umm")
                        rprint("time        Show the time and date")
                        rprint("calendar    Show a calendar")
                        rprint("calc        A simple calculator")
                        rprint("clear       Clean the screen")
                        rprint("passwd      Change your password")
                        rprint("exit        Log out")
                    elif cmd == "calc":
                        try:
                            formula = input("Enter the formula to be calculated:\n")
                            rprint(formula + "=", eval(formula))
                        except Exception as e:
                            rprint("Input error.")
                    elif cmd == "":
                        space = "0"
                    elif cmd == "clear":
                        i = os.system("cls")
                    elif cmd == "exit":
                        break
                    else:
                        rprint("Shell:Command not found.")
            else:
                rprint("Password Incorrect, please try again")
    else:
        rprint("User not found, try another")
