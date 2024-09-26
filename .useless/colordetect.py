import os
termColorDepth = str(os.system("tput colors"))
if termColorDepth == "256":
    print("Your terminal is support 256 colors!")
elif termColorDepth == "88":
    print("Only 88 colors...")
elif termColorDepth == "16":
    print("Are you EGA?")
elif termColorDepth == "8":
    print("So ugly...")
else:
    print("B&W???")
