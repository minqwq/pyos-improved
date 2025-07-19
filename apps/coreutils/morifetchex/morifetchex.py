import os
import sys
import psutil
import json
import platform
from colorama import *
import time

def mori(user, hostname, curpath, configfile, devconfigfile, uptime):
    if curpath == "":
        path = os.getcwd()
    else:
        path = curpath
    
    conf = open(configfile, "r", encoding="utf-8")
    devconf = open(devconfigfile, "r", encoding="utf-8")
    cJsonRead = json.load(conf)
    cDevJsonRead = json.load(devconf)
    
    # CONFIG SET START
    system_version = cDevJsonRead["system_version"] # 版本号 / Version
    system_codename = cDevJsonRead["system_codename"] # Codename
    system_build = cDevJsonRead["system_build"] # 每做一个修改或增减内容，就加一个 Build / If changed a feature, build +=1
    system_is_beta = False # 是否为 Beta 版 / Beta version
    isWindows = cJsonRead["isWindows"] # 是否为 Windows / Are you windows?
    cmd_theme = cJsonRead["cmd_theme"] # 终端 Shell 主题 / Terminal shell theme
    isDev = False # 是否为 Dev 模式 / Dev mode
    enable_instant_show_time = cJsonRead["enable_instant_show_time"] # INstant show time before shell
    isUnregistered = cJsonRead["isUnregistered"] # Fake unregistered warning
    beep_when_finished = cJsonRead["beep_when_finished"] # When a command finished running, speaker will beep
    auto_boot_choice = cJsonRead["auto_boot_choice"] # When have a number, the boot manager will auto boot to selected operating system.
    enablePassword = cJsonRead["enablePassword"] # Enable password when login, string on the config.
    show_password_when_typing = cJsonRead["show_password_when_typing"] # Enable will not shown password when typing.
    pwdstring = cJsonRead["pwdstring"] # Password string
    allowShowNotify = cJsonRead["allowShowNotify"] # Enable to show notify in linux desktop or windows 10+
    dualBoot = cJsonRead["dualBoot"] # Allow you to boot another fake os written in any language
    dualBoot_startupCommand = cJsonRead["dualBoot_startupCommand"] # Dual boot startup command
    dualBoot_OSName = cJsonRead["dualBoot_OSName"] # Dual boot name(show in boot manager)
    venvEnable = cJsonRead["venvEnable"] # Enable python venv here
    if venvEnable == "true":
        venvPath = cJsonRead["venvPath"] # If you are linux distro, like me, you need this
    replace_python_command_to_python3 = cJsonRead["replace_python_command_to_python3"] # Replace python command to python3(when you using linux distro)
    disablePathShow = cJsonRead["disablePathShow"] # Disable path show on shell
    shorter_welcome = cJsonRead["shorter_welcome"] # Show shorter welcome text when logon
    faster_startup = cJsonRead["faster_startup"] # New version of startup screen
    rsyscmd_when_cnf = cJsonRead["rsyscmd_when_cnf"] # Run system command when command not found
    
    def final_prints():
        print(f"{Fore.LIGHTCYAN_EX}morifetch{Fore.LIGHTRED_EX}EX{Style.RESET_ALL} Version 0.01a Demo\n",
              f" {Fore.YELLOW}User & Hostname: {Style.RESET_ALL}{user} at {hostname}\n",
              f" {Fore.YELLOW}Uptime: {Style.RESET_ALL}{uptime} secs\n",
              f" {Fore.YELLOW}Version & Codename: {Style.RESET_ALL}{system_version} \"{system_codename}\"\n\n",
              f" {Fore.GREEN}Host System Release: {Style.RESET_ALL}{platform.system()} {platform.release()} {platform.version()}\n",
              f" {Fore.GREEN}Host Arch: {Style.RESET_ALL}{platform.machine()}\n\n",
              f" {Fore.CYAN}CPU: {Style.RESET_ALL}Failed to Fetch\n"
              f"  {Fore.CYAN}Native Memory: {Style.RESET_ALL}1024 KiB")
        formemcount = 0
        formemtotal = int(psutil.virtual_memory().total / 1024 / 1024)
        for i in range(formemtotal):
            formemcount += 1
            print(f"  {Fore.CYAN}Extended Memory: {Style.RESET_ALL}{formemcount} MiB", end="\r") 
            time.sleep(0.00001)
        print(f"  {Fore.CYAN}Extended Memory: {Style.RESET_ALL}{formemtotal} MiB")

    final_prints()
