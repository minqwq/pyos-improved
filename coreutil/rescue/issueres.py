import os
import sys

print("PY OS Improved ~ Rescue Mode ~")
print("Select your problem!\n1 - System wont boot up\n2 - Color disappeared and showing many ansi codes")
cmd = input("==> ")
if cmd == "1":
    input("System wont boot up:"+"\n"
          "Try reinstalling or open new issue;\n"+
          "We will help yoou before system fixed successfully.")
elif cmd == "2":
    input("Color disappeared and showing many ansi codes\n"+
          "Install a Graphic Adapter or run 'export TERM=<TERMTYPE>', or contact me.")
