f = open('password.txt', 'r')
passwd = open("password.txt", "r")
readpasswd = passwd.read()
print(readpasswd)
passwordInput = input("Password: ")
if passwordInput == readpasswd:
    print("pass!")
else:
    print("wrong!")
