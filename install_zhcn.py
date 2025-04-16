# ScarletInstaller 1.0.1
# License:minqwq's License 1.0
# by Flandre Studio aka minqwq

import os

program_name = "PY OS Improved"
print("Scarlet Software Installer | by Flandre Studio")
print("欢迎使用 " + program_name + " 安装程序!")
print("本安装程序将引导您正确安装 " + program_name + " 。")

print("第一步: " + "安装 Python 模块")
choice01 = input("普通安装:按下回车\n(危险选项) 使用 --break-system-packages:B\n添加自定义参数:C\n使用 venv:V\n[None/B/C/V]")
if choice01 == "":
    os.system("pip install -r requirements.txt")
elif choice01 == "B" or choice01 == "b":
    os.system("pip install -r requirements.txt " + "--break-system-packages")
elif choice01 == "V" or choice01 == "v":
    choice02 = input("请键入venv的文件目录(示例:~/pyvenv/bin/pip): ")
    os.system(choice02 + " install -r requirements.txt")
elif choice01 == "C" or choice01 == "c":
    while True:
        para01 = input("自定义参数: ")
        print("接下来将运行以下命令，如果您确认没有问题请输入y，否则请输入n重输。:")
        print("pip install -r requirements.txt " + para01)
        yorn01 = input("Continue?[Y/N]")
        if yorn01 == "Y" or yorn01 == "y":
            os.system("pip install -r requirements.txt " + para01)
            break
        elif yorn == "N" or yorn01 == "n":
            pass
print("请在安装完成后查看 afterinstall.txt （如果您看得懂英文！）")
print("如果 pip 返回了红色的错误, 那么请重新运行这个脚本，或者检查一下您是否安装了 pip 。")
print("安装完毕，输入\"<venvPath>/python/python3 pyosimproved.py \"")
