import os
import sys
l = True
while l == True:
    cmd = input("==> ")
    if cmd == "":
        print("No string provided.")
    elif cmd == "__exit__":
        sys.exit()
    else:
        os.system("python extprog/" + cmd + ".py")
