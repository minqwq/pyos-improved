import os
import sys
l = True
print("Type '__exit__' to exit, other string to start application.")
while l == True:
    cmd = input("==> ")
    if cmd == "":
        print("No string provided.")
    elif cmd == "__exit__":
        sys.exit()
    else:
        os.system("python extprog/" + cmd + ".py")
