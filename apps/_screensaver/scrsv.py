import os
import sys
print("1:pipes.sh\n2:hack\n3:loading")
select = input("> ")
if select == "1":
    os.system("./pipes.sh/pipes.sh")
    sys.exit()
elif select == "2":
    os.system("python3 ./hack/hack.py")
    sys.exit()
elif select == "3":
    os.system("python3 ./loading/loading.py")
    sys.exit()
else:
    print("?")
