# Filename : test.py 
# author by : www.runoob.com 
# 用户输入字符 
mode = input("Modes list:\n1:Text to code\n2:Code to text\n> ")
if mode == "1":
    e = input("Input a text: ") # 用户输入ASCII码，并将输入的数字转为整型 
    c = e[:1]
    print( c + ":", ord(c))
elif mode == "2":
    b = int(input("Input code: "))
    a = b
    print( a , ":", chr(a))
else:
    print("Bad mode")
