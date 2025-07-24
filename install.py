"""
@ Name: PY OS Improved Installer
@ License: minqwq's License 1.0
@ Author: ElofHew
@ Date: 2025/07/24
@ Version: 3.0
"""

# Import necessary modules
import os
import time
import sys
import subprocess
import platform
import json

def pip_ready():
    print("Preparation: Setting pip mirror source")  # Display preparation message
    print("-" * 20)  # Separator line
    while True:
        mirror = input("Do you want to use Tsinghua University mirror source? (y/n)\n> ").lower()
        if mirror == "y":
            update_pip()
            set_pip_mirror()
            break
        elif mirror == "n":
            break
        else:
            print("Invalid input. Please try again.")

def update_pip():
    print("Updating pip")
    subprocess.run(["python", "-m", "pip", "install", "-i", "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple", "--upgrade", "pip"])
    pip_result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
    print("Current pip version:", pip_result.stdout)

def set_pip_mirror():
    print("Switching pip mirror source...")
    subprocess.run(["pip", "config", "set", "global.index-url", "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple"])
    print("Switch pip mirror source to Tsinghua University mirror source successfully.")

def step1():
    while True:
        print("Step 1: Install Python modules")
        print("[1] General Install")
        print("[2] Use --break-system-packages (Dangerous Option)")
        print("[3] Add Custom Parameters")
        print("[4] Use venv")
        print("[0] Exit")
        install_option = input("> ")
        if install_option == "1":
            if not confirm_action("(Press Enter to continue, Press N to cancel) "):
                break
            subprocess.run(["pip", "install", "-r", "requirements.txt"])
            return
        elif install_option == "2":
            if not confirm_action("Press Enter to continue, Press N to cancel) "):
                break
            subprocess.run(["pip", "install", "-r", "requirements.txt", "--break-system-packages"])
            return
        elif install_option == "3":
            custom_args = input("Please enter your custom parameters:\n").split()
            try:
                subprocess.run(["pip", "install", "-r", "requirements.txt"] + custom_args)
                break
            except subprocess.CalledProcessError:
                print("Custom parameters are incorrect, please re-enter")
        elif install_option == "4":
            venv_path = input("Please enter your venv path (e.g. ~/pyvenv/bin/pip): ")
            if os.path.exists(venv_path):
                try:
                    subprocess.run([venv_path, "-m", "pip", "install", "-r", "requirements.txt"])
                    break
                except subprocess.CalledProcessError:
                    print("Failed to install modules, please check your venv path and try again")
            else:
                print("Invalid input. Please try again.")
        elif install_option == "0":
            print("Exiting PY OS Improved Installer...")
            sys.exit(0)
        else:
            print("Invalid input. Please try again.")

def confirm_action(prompt):
    return input(prompt).lower() != "n"

def step2(requirements_file='requirements.txt'):
    print("Step 2: Check module installation success")  # Display Step 2
    with open(requirements_file) as f:
        requirements = [req.strip().lower() for req in f if req.strip() and not req.startswith('#')]
    installed_packages = {pkg.split('==')[0].strip().lower() for pkg in subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8').split('\n') if pkg}
    missing_packages = [package for package in requirements if package not in installed_packages]
    if missing_packages:
        print("Uninstalled modules:")
        for package in missing_packages:
            print(package)
        time.sleep(1)
        print("Failed to install modules, you can manually enter “pip install module_name” to install them, or re-run this installer again")
        print("(Assuming you have correctly installed pip)")
    else:
        print("All modules have been installed.")

def step3():
    print("Step 3: Configure PY OS Improved")  # Display Step 3
    config_path = '.\\config\\config.json' if platform.system() == "Windows" else './config/config.json'
    with open(config_path, 'r') as file:
        config = json.load(file)
    config['isWindows'] = "true" if platform.system() == "Windows" else "false"
    with open(config_path, 'w') as file:
        json.dump(config, file, indent=4)
    print("Completed PY OS Improved configuration for {} operating system.".format(platform.system()))

def main():
    print("Scarlet Package Installer | Flandre Studio Production")  # Display title
    print("Welcome to PY OS Improved Installer!")  # Display welcome message
    print("This program can install PY OS Improved completely.")  # Display description
    print("=" * 20)  # Separator line
    pip_ready()  # Run preparation
    print("=" * 20)  # Separator line
    step1()  # Run Step 1
    print("=" * 20)  # Separator line
    step2()  # Run Step 2
    print("=" * 20)  # Separator line
    step3()  # Run Step 3
    print("=" * 20)  # Separator line
    print("Tips:\n[1] If you are using Windows, it is recommended to use cmd or PowerShell to run PY OS Improved.\n[2] If you are using Linux/macOS, you only need to use the terminal to run PY OS Improved.\n[3] If you are using Android, you can use Termux to run PY OS Improved.")  # Display tip information
    print("-" * 20)  # Separator line
    print("For more information, please check the ‘afterinstall.txt’ file.\nInstallation complete, this program will exit in 5 seconds.")  # Display end information
    time.sleep(5)  # Wait for 5 seconds before exit
    sys.exit()  # Exit program

if __name__ == '__main__':
    main()

# Edit by ElofHew on 2025/07/24
