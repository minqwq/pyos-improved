import platform
import os
import subprocess
from typing import Dict

def get_system_info() -> Dict[str, str]:
    """获取跨平台的系统信息，键名根据系统类型动态选择"""
    info = {}
    is_windows = platform.system() == "Windows"
    is_linux = platform.system() == "Linux"
    is_mac = platform.system() == "Darwin"

    # 系统基本信息（固定键名）
    info["system_name"] = platform.system()
    info["system_version"] = platform.version()
    info["release"] = platform.release()
    
    # CPU信息（动态键名）
    cpu_key = "windows_cpu" if is_windows else "linux_cpu" if is_linux else "mac_cpu"
    info[cpu_key] = "Unknown"
    
    try:
        if is_windows:
            info[cpu_key] = platform.processor()
        elif is_linux:
            with open('/proc/cpuinfo') as f:
                for line in f:
                    if 'model name' in line:
                        info[cpu_key] = line.split(':')[1].strip()
        elif is_mac:
            cpu_info = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string']).decode().strip()
            info[cpu_key] = cpu_info if cpu_info else "Unknown"
    except Exception:
        pass

    # 内存信息（动态键名）
    mem_key = "windows_mem" if is_windows else "linux_mem" if is_linux else "mac_mem"
    info[mem_key] = "Unknown"
    
    try:
        if is_windows:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory.restype = ctypes.c_ulonglong
            mem_kb = kernel32.GetPhysicallyInstalledSystemMemory()
            info[mem_key] = f"{mem_kb // 1024} MB"
        elif is_linux:
            with open('/proc/meminfo') as f:
                for line in f:
                    if 'MemTotal' in line:
                        mem_kb = int(line.split()[1])
                        info[mem_key] = f"{mem_kb // 1024} MB"
                        break
        elif is_mac:
            mem_bytes = int(subprocess.check_output(['sysctl', '-n', 'hw.memsize']).decode().strip())
            info[mem_key] = f"{mem_bytes // (1024**3)} GB"
    except Exception:
        pass

    # 声卡信息（动态键名）
    sound_key = "windows_sound" if is_windows else "linux_sound" if is_linux else "mac_sound"
    info[sound_key] = "Unknown"
    
    try:
        if is_linux:
            sound_cards = subprocess.check_output(['aplay', '-l'], stderr=subprocess.DEVNULL).decode()
            if sound_cards:
                info[sound_key] = sound_cards.split('\n')[1].split(':')[1].strip()
        elif is_windows:
            try:
                import wmi
                c = wmi.WMI()
                for item in c.Win32_SoundDevice():
                    info[sound_key] = item.Name
                    break
            except ImportError:
                pass  # 没有安装pywin32
    except Exception:
        pass

    # 当前路径（固定键名）
    info["current_path"] = os.getcwd()
    
    return info

def format_panic_screen(info: Dict[str, str]) -> str:
    """格式化输出为panic界面样式"""
    border = "-" * 28
    is_windows = "windows_cpu" in info
    is_linux = "linux_cpu" in info
    is_mac = "mac_cpu" in info

    # 动态选择键名
    cpu_key = "windows_cpu" if is_windows else "linux_cpu" if is_linux else "mac_cpu"
    mem_key = "windows_mem" if is_windows else "linux_mem" if is_linux else "mac_mem"
    sound_key = "windows_sound" if is_windows else "linux_sound" if is_linux else "mac_sound"

    return f"""
System Software Panic!!
{border}
Host info:
- System name & version: {info["system_name"]} {info["release"]} ({info["system_version"]})
- CPU: {info.get(cpu_key, "Unknown")}, {info.get("cpu_mhz", "Unknown")}, {platform.machine()}
- Memory: {info.get(mem_key, "Unknown")}
- Sound Card: {info.get(sound_key, "Unknown")}
- Current Path: {info["current_path"]}
- Python version: {str(platform.python_version())}
{border}
"""

if __name__ == "__main__":
    system_info = get_system_info()
    panic_screen = format_panic_screen(system_info)
    print(panic_screen)
