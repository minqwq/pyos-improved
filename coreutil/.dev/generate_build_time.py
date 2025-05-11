import time
import datetime
import os
import platform
import curses

dt = datetime.datetime.now()
writeme = open("../buildtime_styled.txt", "w+", encoding="utf-8")
writeme.write("SYSBUILD "+
              str(dt.strftime("%A, %d. %B %Y %H:%M:%S"))+
              ", "+
              platform.machine()+
              " "+
              platform.system()+
              " "+
              platform.release())
curses.initscr()
curses.flash()
curses.endwin()
