import os
import sys
while True:
    program = input("Program name(without .py) --> ")
    if program == "__exit__":
        print("exiting")
        sys.exit()
    else:
        os.system("python extprog/" + program + ".py")
