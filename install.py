# ScarletInstaller 1.0
# License:minqwq's License 1.0
# by Flandre Studio aka minqwq

import os

program_name = "PY OS Improved"
print("Scarlet Software Installer | by Flandre Studio")
print("Welcome to " + program_name + " Installer!")
print("This program let you install " + program_name + " completely.")

print("Step 1: " + "Install Python modules")
choice01 = input("Normally install:*Press enter*\nAdd --break-system-packages:B\nAdd custom parameter:C\n[None/B/C]")
if choice01 == "":
    os.system("pip install -r requirements.txt")
elif choice01 == "B" or choice01 == "b":
    os.system("pip install -r requirements.txt " + "--break-system-packages")
elif choice01 == "C" or choice01 == "c":
    while True:
        para01 = input("Custom parameter: ")
        print("Press enter will run this command and go to next step:")
        print("pip install -r requirements.txt " + para01)
        yorn01 = input("Continue?[Y/N]")
        if yorn01 == "Y" or yorn01 == "y":
            os.system("pip install -r requirements.txt " + para01)
            break
        elif yorn == "N" or yorn01 == "n":
            pass
print("If you need help, see afterinstall.txt")
print("If the pip return some error, re-run this program or check are you installed the pip.")
print("Install finished.")
