def option():
    while True:
        print("Caesar tools v1.0 code from CSDN")
        print("Type a option...")
        print("e:Encode\nd:Decode\nq:Quit")
        mode=input("> ").lower()
        if mode in "e d q".split():
            return mode
        else:
            print("Incorrect option")

def getKey(mode):
    key=0
    while key<=0 or key>=26:
        try:
            key=int(input("Please type a key code...(from 1 to 26):"))
        except:
            print("Illegal key code")
    if mode=="d":
        key=-key
    return key

def getMessage(key):
    text=input("Please type encoded text:")  
    message=""
    for i in text:
        num=ord(i)
        num=num+key
        if i.isupper():
            if num>ord("Z"):
                num=num-26
            elif num<ord("A"):
                num=num+26
        elif i.islower():
            if num>ord("z"):
                num=num-26
            elif num<ord("a"):
                num=num+26
        message += chr(num)
    return message

mode = option()
if mode == "q":
    print("Welcome to you use this tool again!")
elif mode == "e":
    key=getKey(mode)
    str1=getMessage(key)
    print("Encode result:\n\n",str1)
elif mode == "d":
    key=getKey(mode)
    str2=getMessage(key)
    print("Decode result is:\n\n",str2)