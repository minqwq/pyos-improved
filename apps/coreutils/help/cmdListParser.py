from helptest import CommandParser
import os

abspath = os.path.dirname(os.path.abspath(__file__))
# 初始化
help_parser = CommandParser(abspath + "/helplist.json")

# 显示所有命令
help_parser.show_help()
