# ScarletInstaller 1.0.1
# License:minqwq's License 1.0
# by Flandre Studio aka minqwq

import os,time,sys,subprocess,platform,json

print("="*20)
print("PY OS Improved Installer")
print("="*20)
print("Choose Language/选择语言/選擇語言")
print("------------------------")
print("1. English（US & UK）")
print("2. 简体中文（中国大陆）")
print("3. 繁体中文（港/澳/台）")
print("------------------------")
lang = input("> ")
while True:
    try:
        if lang == "1":
            print("Welcome to PY OS Improved Installer!\n")
            break
        elif lang == "2":
            print("欢迎使用PY OS Improved安装程序！\n")
            break
        elif lang == "3":
            print("歡迎使用PY OS Improved安裝程式！\n")
            break
        else:
            print("Invalid input./无效输入。/無效輸入。\n")
            continue
    except:
        print("Invalid input./无效输入。/無效輸入。\n")
        continue

# Different Languages Resources

program_name = "PY OS Improved"

if lang == "1":
    input_error = "Invalid input, Please retry."
    text_01 = "Scarlet Software Installer | by Flandre Studio"
    text_02 = "Welcome to " + program_name + " Installer!"
    text_03 = "This program can help you install " + program_name + " completely."
    text_04 = "Step 1: Install Python modules"
    text_05 = "[1]Normally install > *Press enter*\n[2](DANGEROUS) Add --break-system-packages > *B*\n[3]Add custom parameter > *C*\n[4]Use venv > *V*\n[None/B/C/V]"
    text_06 = "Please input the path to pip in your venv(example:~/pyvenv/bin/pip): "
    text_07 = "Please input your custom parameter:\n"
    text_08 = "Press ENTER will run this command and enter the next step, Press N and enter to cancel:"
    text_09 = "Step 2: Check module installation"
    text_10 = "Step 3: Configure PY OS Improved"
    text_11 = "Detect your operating system is Windows, is it correct? Yes = Enter, No = Any character and Enter"
    text_12 = "Detect your operating system is Linux/macOS (non-Windows), is it correct? Yes = Enter, No = Any character and Enter"
    step2_1 = "Missing modules:"
    step2_2 = "All modules are installed."
    step2_3 = 'Failed to install some modules, you can manually enter "pip install module_name" in terminal or re-run this installer'
    step2_4 = "(Assuming you have already installed pip)"
    step3_1 = "Completed PY OS Improved configuration for Windows operating system."
    step3_2 = "Non-Windows operating system, not modified PY OS Improved configuration for Windows operating system."
    step3_3 = "Completed PY OS Improved configuration for non-Windows operating system."
    step3_4 = "Windows operating system, modified PY OS Improved configuration for Windows operating system."
    after_install = "Tips:\n[1] If you are using Windows, It's best to use cmd or PowerShell to run PY OS Improved.\n[2] If you are using Linux/macOS, you just need to use terminal to run PY OS Improved.\n[3] If you are using Android, you can use Termux to run PY OS Improved."
    end_text = "More information can be found in 'afterinstall.txt' file.\nInstallation completed, this program will exit in 10 seconds."
elif lang == "2":
    input_error = "无效输入，请重试。"
    text_01 = "Scarlet 软件包安装程序 | Flandre Studio 出品"
    text_02 = "欢迎使用 " + program_name + " 安装程序！"
    text_03 = "这个程序可以让你完全安装 " + program_name + " 。"
    text_04 = "第一步：安装Python模块"
    text_05 = "[1]常规安装 > *按下回车*\n[2](危险选项) 使用 --break-system-packages > *B*\n[3]添加自定义参数 > *C*\n[4]使用 venv > *V*\n[回车/B/C/V]"
    text_06 = "请输入你的 venv 中的 pip 的路径(例如:~/pyvenv/bin/pip): "
    text_07 = "请输入你的自定义参数:\n"
    text_08 = "按下回车将运行这个命令并进入下一步，输入N并回车以取消："
    text_09 = "第二步，检查模块安装是否成功"
    text_10 = "第三步：配置PY OS Improved"
    text_11 = "检测到您的操作系统为Windows，是否正确？是 = 回车、否 = 输入任意字符并回车"
    text_12 = "检测到您的操作系统为Linux/macOS（非Windows），是否正确？是 = Enter、否 = 输入任意字符并Enter"
    step2_1 = "未安装的模块："
    step2_2 = "所有模块均已安装。"
    step2_3 = "安装失败的模块可手动终端输入“pip install 模块名”来安装，也可以重新运行一遍本安装程序"
    step2_4 = "(前提是确保你已经正确安装了pip)"
    step3_1 = "已完成应用于Windows操作系统的PY OS Improved配置项。"
    step3_2 = "非Windows操作系统，未修改针对于Windows操作系统的PY OS Improved配置项。"
    step3_3 = "已完成应用于非Windows操作系统的PY OS Improved配置项。"
    step3_4 = "Windows操作系统，已修改针对于Windows操作系统的PY OS Improved配置项。"
    after_install = "提示:\n[1] 如果您使用Windows，建议您使用cmd或PowerShell运行PY OS Improved。\n[2] 如果您使用Linux/macOS，只需要使用终端运行PY OS Improved。\n[3] 如果您使用Android，您可以使用Termux运行PY OS Improved。"
    end_text = "更多信息请查看‘afterinstall.txt’文件。\n安装完成，本程序将在10秒后退出。"
elif lang == "3":
    input_error = "無效輸入，請重試。"
    text_01 = "Scarlet 軟體安裝程式 | Flandre Studio 製造"
    text_02 = "歡迎使用 " + program_name + " 安裝程式！"
    text_03 = "這個程式可以讓你完全安裝 " + program_name + " 。"
    text_04 = "第一步：安裝Python模塊"
    text_05 = "[1]常規安裝 > *按下Enter*\n[2](危險選項) 使用 --break-system-packages > *B*\n[3]添加自定義參數 > *C*\n[4]使用 venv > *V*\n[Enter/B/C/V]"
    text_06 = "請輸入你的 venv 中的 pip 的路徑(例如:~/pyvenv/bin/pip): "
    text_07 = "請輸入你的自定義參數:\n"
    text_08 = "按下Enter將執行這個命令並進入下一步，輸入N並回车以取消："
    text_09 = "第二步，檢查模塊安裝是否成功"
    text_10 = "第三步：設定PY OS Improved"
    text_11 = "偵測到您的作業系統為Windows，是否正確？是 = Enter、否 = 輸入任意字符並Enter"
    text_12 = "偵測到您的作業系統為Linux/macOS（非Windows），是否正確？是 = Enter、否 = 輸入任意字符並Enter"
    step2_1 = "遺漏的模塊："
    step2_2 = "所有模塊均已安裝。"
    step2_3 = "安裝失敗的模塊可手動終端輸入“pip install 模塊名”來安裝，也可以重新執行本安裝程式"
    step2_4 = "(前提是確保你已經成功安裝了pip)"
    step3_1 = "已完成應用於Windows作業系統的PY OS Improved設定項。"
    step3_2 = "非Windows作業系統，未修改針對Windows作業系統的PY OS Improved設定項。"
    step3_3 = "已完成應用於非Windows作業系統的PY OS Improved設定項。"
    step3_4 = "Windows作業系統，已修改針對Windows作業系統的PY OS Improved設定項。"
    after_install = "提示:\n[1] 如果您使用Windows，建議您使用cmd或PowerShell執行PY OS Improved。\n[2] 如果您使用Linux/macOS，只需要使用終端執行PY OS Improved。\n[3] 如果您使用Android，您可以使用Termux執行PY OS Improved。"
    end_text = "更多資訊請查看‘afterinstall.txt’檔案。\n安裝完成，本程式將在10秒後退出。"

# Modules For Each Step

def custom_para(para01, para02):
    while True:
        try:
            if para02 == "":
                os.system("pip install -r requirements.txt " + para01)
                break
            elif para02 == "N" or para02 == "n":
                break
            else:
                print(input_error)
                continue
        except:
            print(input_error)
            continue

def step1(venv_path=None):
    while True:
        try:
            choice01 = input("> ")
            if choice01 == "":
                os.system("pip install -r requirements.txt")
                break
            elif choice01 == "B" or choice01 == "b":
                os.system("pip install -r requirements.txt --break-system-packages")
                break
            elif choice01 == "V" or choice01 == "v":
                while True:
                    try:
                        venv_path = input(text_06)
                        if os.path.exists(venv_path):
                            os.system(f"{venv_path} install -r requirements.txt")
                            break
                        else:
                            print(input_error)
                    except:
                        print(input_error)
                        continue
                break
            elif choice01 == "C" or choice01 == "c":
                para01 = input(text_07)
                para02 = input(text_08)
                custom_para(para01, para02)
                break
            else:
                print(input_error)
                continue
        except:
            print(input_error)
            continue

def venv_para(para01, para02, venv_path):
    while True:
        try:
            if para02 == "":
                os.system(venv_path + " install -r requirements.txt " + para01)
                break
            elif para02 == "N" or para02 == "n":
                break
            else:
                print(input_error)
                continue
        except:
            print(input_error)
            continue

def step2(requirements_file='requirements.txt'):
    with open(requirements_file) as f:
        requirements = f.readlines()

    installed_packages = subprocess.check_output([subprocess.sys.executable, '-m', 'pip', 'freeze']).decode('utf-8').split('\n')
    installed_packages = {pkg.split('==')[0].strip().lower() for pkg in installed_packages if pkg}

    missing_packages = []

    for req in requirements:
        req = req.strip()
        if req and not req.startswith('#'):  # 忽略注释
            package_name = req.split('==')[0] if '==' in req else req.split('>')[0] if '>' in req else req.split('<')[0] if '<' in req else req.split('>=')[0] if '>=' in req else req.split('<=')[0] if '<=' in req else req
            if package_name.lower() not in installed_packages:
                missing_packages.append(package_name)

    if missing_packages:
        print(step2_1)
        for package in missing_packages:
            print(package)
        time.sleep(1)
        print(step2_3)
        print(step2_4)
    else:
        print(step2_2)
    # 调用函数检查requirements.txt中的模块是否已安装

def step3():
    if platform.system() == "Windows":
        print(text_11)
        choose02 = input("> ")
        if choose02 == "":
            with open('config/config.json', 'r') as file:
                config = json.load(file)
            config['isWindows'] = "true"
            with open('config/config.json', 'w') as file:
                json.dump(config, file, indent=4)
            print(step3_1)
        else:
            with open('config/config.json', 'r') as file:
                config = json.load(file)
            config['isWindows'] = "false"
            with open('config/config.json', 'w') as file:
                json.dump(config, file, indent=4)
            print(step3_2)
    else:
        print(text_12)
        choose02 = input("> ")
        if choose02 == "":
            with open('config/config.json', 'r') as file:
                config = json.load(file)
            config['isWindows'] = "false"
            with open('config/config.json', 'w') as file:
                json.dump(config, file, indent=4)
            print(step3_3)
        else:
            with open('config/config.json', 'r') as file:
                config = json.load(file)
            config['isWindows'] = "true"
            with open('config/config.json', 'w') as file:
                json.dump(config, file, indent=4)
            print(step3_4)

time.sleep(1)
print(text_01)
print(text_02)
print(text_03)
time.sleep(1)
print("="*20)
print(text_04)
print(text_05)
step1()
print("="*20)
print(text_09)
time.sleep(1)
step2()
time.sleep(1)
print("="*20)
print(text_10)
step3()
time.sleep(1)
print("="*20)
print(after_install)
print("-"*20)
print(end_text)
time.sleep(10)
sys.exit()

# Modified by ElofHew on 2025/04/26

"""
@Website: http://www.drevan.xyz/
@Github: https://github.com/ElofHew/
@Bilibili: https://space.bilibili.com/642688364/
@Date: 2025/04/26
"""