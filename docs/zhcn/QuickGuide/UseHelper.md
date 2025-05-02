# PY OS Improved 快速入门指南

# 目录

- [1. 安装 PY OS Improved](#1-安装-py-os-improved)
  - [1.1 安装 Python](#11-安装-python)
  - [1.2 安装 PY OS Improved](#12-安装-py-os-improved)
  - [1.3 运行 PY OS Improved](#13-运行-py-os-improved)
- [2. 基本操作](#2-基本操作)
  - [2.1 开机启动](#21-开机启动)
  - [2.2 命令帮助](#22-命令帮助)
  - [2.3 蜂鸣声含义](#23-蜂鸣声含义)
- [3. 第三方软件](#3-第三方软件)
  - [3.1 安装第三方软件](#31-安装第三方软件)
  - [3.2 卸载第三方软件](#32-卸载第三方软件)
- [4. 加入开发者团队](#4-加入开发者团队)

## 1. 安装 PY OS Improved

### 1.1 安装 Python

请确保您的电脑上已经安装了 Python 3.8 或以上版本。

如果没有安装 Python，请使用以下方式安装：

**For Windows**

前往 [Python 官网](https://www.python.org/downloads/) 或 [阿里云镜像源](https://mirrors.aliyun.com/python-release/) 下载安装包。

下载完成后直接安装即可。

> 注意：安装界面中，请勾选 `Add Python 3.x to PATH` 选项。

**For macOS**

使用 Homebrew 安装 Python：

``` bash
brew install python 
```

**For Linux**

请根据您的发行版的包管理器安装 Python。

Debian/Ubuntu：

``` bash
sudo apt-get install python3
```

CentOS/Fedora：

``` bash
sudo dnf install python3
```

Arch Linux：

``` bash
sudo pacman -S python
```

### 1.2 安装 PY OS Improved

1. 下载 PY OS Improved Release：

    前往 [PY OS Improved Release](https://github.com/minqwq/pyos-improved/releases) 页面下载最新版本的 PY OS Improved。

2. 解压 PY OS Improved：

    > Tips：请确保解压到一个安全的位置，避免被恶意修改，并且目录名尽量只包含英文、数字和下划线。

3. 部署 PY OS Improved：

    打开终端，使用 `cd` 命令进入到 PY OS Improved 解压后的目录，例如：

    ``` bash
    # Linux/macOS
    cd "~/Downloads/pyos-improved-1.5.1/"

    # Windows
    cd "D:\Downloads\pyos-improved-1.5.1/"
    ```

    然后再 `cd` 到 `INSTALL` 目录：

    ``` bash
    cd INSTALL
    ```

    执行 `installer_v2.0.py` 安装程序：

    ``` bash
    # Linux/macOS
    python3 installer_v2.0.py

    # Windows
    python installer_v2.0.py
    ```

    按照提示安装依赖模块，即可完成安装。

### 1.3 运行 PY OS Improved

打开终端，使用 `cd` 命令进入到 PY OS Improved 解压后的PYOSI目录，例如：

``` bash
# Linux/macOS
cd ~/Documents/pyos-improved/PYOSI/

# Windows
cd "E:\Documents\pyos-improved\PYOSI\"
```

然后执行 `python3 pyosimproved.py` 命令：

``` bash
# Linux/macOS
python3 pyosimproved.py

# Windows
python pyosimproved.py
```

即可成功运行 PY OS Improved。

## 2. 基本操作

### 2.1 开机启动

当您启动 PY OS Improved 时，只需要按下回车。

然后会进入到 PY OS Improved 的版本选择界面，输入1~5选择版本，按下回车即可进入系统。

> 如果你不清楚应该使用哪个版本，按下 1 并回车即可。

接下来会进入登录界面，输入您的用户名即可登录进入系统。

### 2.2 命令帮助

在 PY OS Improved 运行时，输入 `help` 即可查看命令帮助。

``` bash
> help

# 输出：
"""
Larine Shell manual help:
(System)
ls                        View the path
about [-c | -s]           Show the system's information
pyosver                   Show system version
converter                 A tool to convert .lpap/.lpcu/.bbc to .umm
time                      Show the time and date(Deteled in this version)
calendar                  Show a calendar
clear                     Clear the screen
(DEL)passwd <str>         Change password for this session
power [shutdown | reboot] Power manager
exit                      Lock system
hostname [-c]             Show hostname
echo <str>                Print text to screen
flan <dir>                Remove file
......
"""
```

### 2.3 蜂鸣声含义（如果有）

#### 登录系统前：
- 1声蜂鸣：一切正常
- 2声蜂鸣：内核崩溃（Kernel Panic）

#### 登录系统后：
- 1声蜂鸣：任务完成、登录成功、任务错误、警告等...
- 3声蜂鸣：系统软件崩溃（System Software Panic）

## 3. 第三方软件

> [!TIP]
> 此部分详见 [第三方软件开发规范](../AppDev/DevStd.md)

PY OS Improved 提供了一个软件包管理器：`Shizuku`，通过Shizuku可以很方便的管理第三方软件。

### 3.1 安装第三方软件

首先找到一个第三方软件的安装包，例如：`example_v1.0.sap`（`example`是该软件的包名）

> [!TIP]
> `sap` 是PY OS Improved 第三方软件特有格式，即Shizuku Application Package 的缩写，详见 [第三方软件开发规范](../AppDev/DevStd.md)

在 PY OS Improved 运行时，输入 `shizuku install example_v1.0.sap`，

``` bash
shizuku install example_v1.0.sap
```

随后按照提示，即可完成安装。

### 3.2 卸载第三方软件

在 PY OS Improved 运行时，输入 `shizuku uninstall example`，

``` bash
shizuku uninstall example
```

即可完成卸载。

## 4. 加入开发者团队

1. 联系主开发者：minqwq
    - 邮箱：<EMAIL>minqwq723897@outlook.com</EMAIL>
    - QQ：3575824194
    
    > 你需要向主开发者表明你的开发意向，并提供你自己的 GitHub 账户，以便主开发者可以邀请你加入开发团队。
    
    > 与主开发者交谈时不必拘谨，主开发者欢迎您的加入，使 PY OS Improved 发展得更好！

2. 加入项目开发：
    - fork 此项目到自己的 GitHub 账户
    - clone 项目到本地
    - 创建分支，开发自己的功能
    - 提交 PR（Pull Request）
    - 等待主开发者审核，通过后合并到主分支

<hr>
<p align="center">—— PY OS Improved 项目组 ——</p>
<p align="center">—— 2025.05.01 ——</p>