import os

def is_termux():
    # Termux通常会在环境变量中设置TERMUX_VERSION
    return 'TERMUX_VERSION' in os.environ

if is_termux():
    print("程序正在Termux中运行")
else:
    print("程序未在Termux中运行")
