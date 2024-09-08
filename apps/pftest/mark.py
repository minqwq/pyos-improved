import time
print("1:1000000\n2:2000000\n3:4000000\n4:8000000\n5:16000000\n6:32000000\n7:64000000\n8:100000000")
diffChoice = input("Choose difficulty for your CPU: ")
if diffChoice == "1":
    max = 1000000
elif diffChoice == "2":
    max = 2000000
elif diffChoice == "3":
    max = 4000000
elif diffChoice == "4":
    max = 8000000
elif diffChoice == "5":
    max = 16000000
elif diffChoice == "6":
    max = 32000000
elif diffChoice == "7":
    max = 64000000
elif diffChoice == "8":
    max = 100000000
print("Test start.\nIf not responding, please wait or press Ctrl+C to force close.")
startTestTime = time.time()
empty = ""
for min in range(max):
    print(empty, end="")
endStartTestTime = time.time()
timeResult = endStartTestTime - startTestTime
score = 1000000 - timeResult * 54188
if score > 980000:
    print("Grade:X")
elif score > 900000:
    print("Grade:S")
elif score > 700000:
    print("Grade:A")
elif score > 550000:
    print("Grade:B")
elif score > 300000:
    print("Grade:C")
elif score > 100000:
    print("Grade:D")
print("\nScore: " + str(score))
print("\nTesting took " + str(timeResult) + "s")
