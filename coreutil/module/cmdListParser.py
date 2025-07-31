from helptest import CommandParser

def helplist_parser(jsonfile):
    # 初始化
    help_parser = CommandParser(jsonfile)
    
    # 显示所有命令
    help_parser.show_help()
