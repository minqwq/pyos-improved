PY OS Improved ~ The Ultimate *fake* Operating System written in Python 3

0. - Requirements
  0.1 - Hardware and Software
1. - Install
  1.1 - Use install.py or install_zhcn.py
  1.2 - Manually install
2. - Configuration
  2.1 - The config file

0.1 - Requirements/Hardware and Software
Operating System:FreeBSD(if you use i486 or Pentium) or Any Linux Distro with Python 3 Support(this require pentium ii or above)
CPU:i486SX 40MHz(Pentium I 100MHz+ Recommended)
GPU:Any VGA Comptiable
RAM:48MB
Disk Space:150MiB Remain(200MiB Remain Recommended)
Sound Card:PC Speaker(Buzzer)(SB16 or AC97 or above Recommended)
Screen:Not text printer(without virtual tty)

1. - Install
1.1 - Use install.py or install_zhcn.py
* Follow the tips and install, this is easy so i dont need to write anything.

1.2 - Manually install
First, install modules using pip, type "pip install -r requirements.txt"(in Linux Distro you may need to create a venv)
if still crash, please install more modules(traceback will tell you what missed)
ok its end, next you need to configure.

2.1 - The config file
"config/config.json" is a config of PY OS Improved, when you first using, you need to modify it(little changes)
Open it, and find a line with "isWindows", if you found, replace "" to "false" or "true"(this by your os type)
if you have venv you can configure "venvEnable" and "venvPath", the example is showed on the config.

Congrats! now type "python(and 3 if you are windows) pyosimproved.py" to run
still issues? open issue or email me:minqwq723897@outlook.com