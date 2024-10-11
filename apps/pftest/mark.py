import time
import os
import tqdm
print("TTYMark by minqwq\nIf you want use this program on your project, please dont delete this line\nIf you delete this line...Take care in tonight.")
print("1:1000000\n2:2000000\n3:4000000\n4:8000000\n5:16000000\n6:32000000\n7:64000000\n8:100000000\n9:200000000\n10:400000000\n11:800000000\n12:1600000000\n13:2147483647\nc:Custom")
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
elif diffChoice == "9":
    max = 200000000
elif diffChoice == "10":
    max = 400000000
elif diffChoice == "11":
    max = 800000000
elif diffChoice == "12":
    max = 1600000000
elif diffChoice == "13":
    max = 2147483647
elif diffChoice == "c":
    max = int(input("Input custom amount: "))
    if max == "":
        print("No value provided.")
startTestTime = time.time()
empty = ""
for min in tqdm.tqdm(range(max)):
    uwu = 0
endStartTestTime = time.time()
timeResult = endStartTestTime - startTestTime
score = 1000000 - timeResult * 45721
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
elif score > 50:
    print("Lower than zero!")
print("\nScore: " + str(score))
print("\nTesting took " + str(timeResult) + "s")
