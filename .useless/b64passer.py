import base64
password_pre = b"aWxvdmVtaW8="
password = base64.b64decode(password_pre)
print(password)
inputpass = bytes(input(), encoding="utf-8")
if inputpass == password:
    print("pass")
# base64.b64decode(passwd.read()).decode("utf-8")
