"""
@ PY OS Improved
@ Shizuku Software Manager
@ Shizuku Application Package Installer Core Module
@ Author: ElofHew
@ Version: 1.0
@ Date: 2025.05.02
"""

import os       # 用于操作系统交互，如获取当前目录、创建目录和删除文件等
import sys      # 用于与Python解释器交互，如退出程序等
import subprocess # 用于在Python脚本中运行外部命令
import zipfile  # 用于处理ZIP文件的压缩和解压缩
import time     # 用于添加延迟
import json     # 用于处理JSON文件的读取和写入
import shutil   # 用于文件和目录的高级操作，如复制文件和删除文件夹等

def install(pkg_path):
    # 打印包路径
    print("path: " + pkg_path)
    # 循环提示用户是否要安装该包，直到输入有效选项
    while True:
        check = str(input("Do you want to install this package? (y/n): "))
        if check == "y" or check == "Y":
            # 如果用户输入 'y' 或 'Y'，则跳出循环继续安装
            break
        elif check == "n" or check == "N":
            # 如果用户输入 'n' 或 'N'，则取消操作并返回状态码
            print("Operation cancelled.")
            return 1
        else:
            # 如果用户输入无效选项，则提示重新输入
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
    # 提示开始安装包
    print("Installing package...")
    try:
        # 获取当前工作目录
        current_dir = os.getcwd()
        # 定义目标目录路径（data/local/tmp）
        destination_dir = os.path.join(current_dir, "data", "local", "tmp")
        
        # 检查目标目录是否存在，如果不存在则创建它
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        else:
            # 如果目标目录存在，清空目录中的所有文件和文件夹（但保留tmp文件夹本身）
            for filename in os.listdir(destination_dir):
                file_path = os.path.join(destination_dir, filename)
                if os.path.isfile(file_path):
                    # 对于文件，直接删除
                    os.remove(file_path)
                elif os.path.isdir(file_path) and filename != 'tmp':
                    # 对于文件夹且不是 'tmp' 文件夹，递归删除整个文件夹
                    shutil.rmtree(file_path)
        
        # 构建目标文件的完整路径（目标目录加上包的文件名）
        destination_path = os.path.join(destination_dir, os.path.basename(pkg_path))
        # 将包文件复制到目标目录
        shutil.copy(pkg_path, destination_path)
        print(f"Package successfully copied to {destination_path}")
        try:
            # 重命名文件为 .zip 扩展名
            new_name = os.path.splitext(os.path.basename(pkg_path))[0] + ".zip"
            os.rename(destination_path, os.path.join(destination_dir, new_name))
            print(f"Package successfully renamed to {new_name}")
            # 定义解压目录路径（data/apps 加上包名去掉 .zip 后缀）
            unzip_dir = os.path.join(current_dir, "data", "apps", new_name[:-4])  # 去掉 .zip 后缀
            # 使用 zipfile 模块解压文件到解压目录
            with zipfile.ZipFile(os.path.join(destination_dir, new_name), 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
            print(f"Package successfully extracted to {unzip_dir}")
            # 打开解压目录中的 info.json 文件以获取应用信息
            with open(os.path.join(unzip_dir, "info.json"), "r") as f:
                config = json.load(f)
            # 从 info.json 中读取应用名称和版本号
            app_name = config["name"]
            app_version = config["version"]
            print(f"Installing {app_name} {app_version}...")
            
            # 检查是否已经存在同名的应用目录
            existing_app_dir = os.path.join(current_dir, "data", "apps", app_name)
            if os.path.exists(existing_app_dir):
                # 打开已安装目录中的 info.json 文件以获取应用信息
                with open(os.path.join(existing_app_dir, "info.json"), "r") as f:
                    existing_config = json.load(f)
                # 从已安装的 info.json 中读取应用版本号
                existing_app_version = existing_config["version"]
                
                # 比较版本号
                if existing_app_version < app_version:
                    print(f"Found older version {existing_app_version} of {app_name}. Installing newer version {app_version}.")
                    # 删除已安装的软件包
                    shutil.rmtree(existing_app_dir)
                else:
                    print(f"{app_name} already installed with version {existing_app_version}. No need to install again.")
                    # 删除临时解压的文件夹
                    shutil.rmtree(os.path.join(destination_dir, new_name[:-4]))
                    return 0
            
            # 将解压目录重命名为应用名称
            os.rename(unzip_dir, os.path.join(current_dir, "data", "apps", app_name))
            new_path_app = os.path.join(current_dir, "data", "apps", app_name)
            # 将解压目录中的 main.py 文件重命名为应用名称.py
            os.rename(os.path.join(new_path_app, "main.py"), os.path.join(new_path_app, app_name + ".py"))
            print("Installing dependencies...")
            # 提示用户是否要更改 pip 的镜像为清华大学镜像
            mirror_change = str(input("Do you want to change the Tsinghua mirror of pip? (y/n): "))
            while True:
                if mirror_change == "y" or mirror_change == "Y":
                    # 如果用户输入 'y' 或 'Y'，则使用清华大学镜像安装 some-package
                    subprocess.run(["pip", "install", "-i", "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple", "some-package"], check=True)
                    break
                elif mirror_change == "n" or mirror_change == "N":
                    # 如果用户输入 'n' 或 'N'，则直接跳出循环，不更改镜像
                    break
                else:
                    # 如果用户输入无效选项，则提示重新输入
                    print("Invalid input. Please enter 'y' or 'n'.")
                    continue
            try:
                # 切换到应用目录
                os.chdir(new_path_app)
                # 安装 requirements.txt 中列出的所有依赖项
                subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
                print("Dependencies installed.")
                print(f"Package successfully installed to {new_path_app}")
                print("="*30)
                print("How to run the application:")
                print(f"! You can just input the command 'szk {app_name} in PY OS Improved.")
                print("="*30)
                # 添加延迟以便用户查看安装信息
                time.sleep(2)
                print(f"{app_name} {app_version} has been successfully installed.")
                # 再次添加延迟以便用户查看安装完成信息
                time.sleep(2)
                # 安装完成后返回状态码
                return 0
            except subprocess.CalledProcessError:
                # 如果 requirements.txt 文件不存在或命令执行失败，则提示相应信息
                print("No requirements.txt found.")
                # 删除临时解压的文件夹
                shutil.rmtree(os.path.join(destination_dir, new_name[:-4]))
                return 1
            except Exception as e:
                # 如果在安装依赖过程中发生其他异常，则打印异常信息
                print(f"An error occurred during installing dependencies: {e}")
                # 删除临时解压的文件夹
                shutil.rmtree(os.path.join(destination_dir, new_name[:-4]))
                return 1
        except Exception as e:
            # 如果在重命名或解压过程中发生异常，则打印异常信息
            print(f"An error occurred during renaming or extraction: {e}")
            # 删除临时解压的文件夹
            shutil.rmtree(os.path.join(destination_dir, new_name[:-4]))
            return 1
    except Exception as e:
        # 如果在安装过程中发生其他异常，则打印异常信息
        print(f"An error occurred: {e}")
        # 删除临时解压的文件夹
        if 'new_name' in locals():
            shutil.rmtree(os.path.join(destination_dir, new_name[:-4]))
        return 1

def remove(app_name):
    # 打印应用名称
    print(f"Removing package: {app_name}")
    # 循环提示用户是否要卸载该包，直到输入有效选项
    while True:
        check = str(input(f"Do you want to remove the package '{app_name}'? (y/n): "))
        if check == "y" or check == "Y":
            # 如果用户输入 'y' 或 'Y'，则跳出循环继续卸载
            break
        elif check == "n" or check == "N":
            # 如果用户输入 'n' 或 'N'，则取消操作并返回状态码
            print("Operation cancelled.")
            return 1
        else:
            # 如果用户输入无效选项，则提示重新输入
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
    
    # 获取当前工作目录
    current_dir = os.getcwd()
    # 定义应用目录路径
    app_dir = os.path.join(current_dir, "data", "apps", app_name)
    
    # 检查应用目录是否存在
    if not os.path.exists(app_dir):
        print(f"Package '{app_name}' not found. No need to remove.")
        return 1
    
    try:
        # 删除应用目录
        shutil.rmtree(app_dir)
        print(f"Package '{app_name}' has been successfully removed.")
        # 再次添加延迟以便用户查看卸载完成信息
        time.sleep(2)
        # 卸载完成后返回状态码
        return 0
    except Exception as e:
        # 如果在删除过程中发生异常，则打印异常信息
        print(f"An error occurred during removal: {e}")
        return 1
