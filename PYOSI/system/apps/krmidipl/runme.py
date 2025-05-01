# import pygame --ai give me the wrong code, the pygame.midi is already removed at 2.0
import os
import time
import pprint
import sys
import rtmidi
import mido

version = "0.01a"
mid_in = rtmidi.MidiIn()
mid_ot = rtmidi.MidiOut()

def lsdir():
    for file in os.listdir(r"."):
        lsdir.append(file)
        pprint.pprint(lsdir)
        get_folder_size()

curoutport = 0
mid_ot.open_port(0)
print("Trying to use O port 0.")
input()

while True:
    os.system("cls")
    # lsdir() --not working.
    os.system("ls")
    print("\ncd <location>\nplay <file.mid>\nabout\nexit")
    cmd = input("> ")
    if cmd.startswith("cd"):
        if cmd[3:] == "":
            input("No location given.")
        else:
            os.chdir(cmd[3:])
    elif cmd.startswith("play"):
        if cmd[5:] == "":
            input("No filename given.")
        else:
            play_begintime = time.time() # 开始计时
            total_size = os.path.getsize(cmd[5:]) # 检查文件大小，一旦过大会发出警告
            if total_size > 200 * 1024:
                input("Size warning: may damage the cpu, press any key to continue playing.")
            playingfile = mido.MidiFile(cmd[5:]) # 文件加载和处理
            play_ttks = sum(playmsg_another.time for playmsg_another in playingfile) # midi总时长
            play_curticks = 0 # 当前tick
            for playmsg in playingfile.play(): # 有点耗性能的播放
                try:
                    if not playmsg.is_meta:
                        mid_ot.send_message(playmsg.bytes())
                        play_curticks += time.time()
                        play_time = time.time() - play_begintime
                        play_progress = (play_curticks / play_ttks) * 100
                        print(
                            f"Stop:Ctrl+C, Pause:i dont know | Kirisame MIDI Player {version}\n"
                            f"Playing: {cmd[5:]}" + 
                            f" | {play_time} / {play_ttks}"
                            f"\nMessage: {playmsg.type} {getattr(playmsg, 'note', '')}", end="\033[2J") # ai写的啥玩意我咋看不懂呢（算了，照抄吧...）
                except KeyboardInterrupt:
                    print("Music stopped.")
                    mid_ot.close_port()
                    break
    elif cmd == "chport":
        for tmp, port in enumerate(mid_in.get_ports()):
            print(f"- I {tmp}: {port}")
        for tmp, port in enumerate(mid_ot.get_ports()):
            print(f"- O {tmp}: {port}")
        selmidport = input("Which one to O not I?(ID) >>> ")
        mid_ot.close_port()
        print(f"Closed every port")
        mid_ot.open_port(int(selmidport))
        curoutport = int(selmidport)
        print(f"Out port {curoutport} set!")
        input()
    elif cmd == "about":
        input("Kirisame MIDI Player - Portable version"
            "\nby minqwq, version " + version +
            "\nuwu")
    elif cmd == "exit":
        sys.exit(0)