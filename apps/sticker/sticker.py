import os
while True:
    print("Sticker v1.0 by minqwq")
    content = input("Input some text below...\nWhen you finish, press enter to show and press again to exit\n\n> ")
    i = os.system("clear")
    print(content)
    print("\nEXIT:exit, RESTART:any key")
    waiting = input("\n> ")
    if waiting == "exit":
        break
