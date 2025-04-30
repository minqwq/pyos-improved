import random

print("Guess number v0.1R2 by minqwq and Copilot")
print("1: max20\n2: max60\n3: max100\n4: max200\n5: max400\n6: max800\n7: max1600")

diff = input("Select a difficulty: ")
if diff == "1":
    numRangeMax = 20
elif diff == "2":
    numRangeMax = 60
elif diff == "3":
    numRangeMax = 100
elif diff == "4":
    numRangeMax = 200
elif diff == "5":
    numRangeMax = 400
elif diff == "6":
    numRangeMax = 800
elif diff == "7":
    numRangeMax = 1600
else:
    exit()

randomResult = random.randint(0, numRangeMax)
looping = True

print("HELP:\nexit:exit\nType some number to guess")

while looping:
    correctNum = randomResult
    guessing = int(input("INPUT AREA > "))  # Convert input to an integer
    if guessing > correctNum:
        print("Number too high")
    elif guessing < correctNum:
        print("Number too low")
    elif guessing == correctNum:
        print("You win~")
        exit()
    elif guessing == "exit":
        exit()
