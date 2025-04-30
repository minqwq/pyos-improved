import random
import time
start = time.time()
line1 = random.randint(1, 4)
line2 = random.randint(1, 4)
line3 = random.randint(1, 4)
line4 = random.randint(1, 4)
chance = 3
space = 0
while True:
    slctl1 = input("Select a line of line 1 > ")
        if slctl1 == line1:
            print("Its correct, next.")
        else:
            awa1 = 1
            chance - awa1
            print("Wrong line! " + str(chance) + " chances remain.")
        if time.time() - start >= 60:
            print("Time over! you died.")
            break
        elif time.time() - start >= 50:
            print("10 Seconds remain!")
        elif time.time() - start >= 30:
            print("30 Seconds remain.")
        elif time.time() - start >= 15:
            print("45 Seconds remain.")
