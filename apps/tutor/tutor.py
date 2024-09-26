import os
import sys
print("Welcome to PY OS Improved help document for new")
print("Input 'tutor_00' to view from first page.")
print("For exit, type 'exit'")
while True:
    choice0 = input("> ")
    if choice0 == "tutor_00":
        os.system("cat ../../docs/tutor/tutor_00.txt")
    elif choice0 == "exit":
        break
        sys.exit()
    else:
        print("Page not found")
