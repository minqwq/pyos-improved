import sys
import shutil
import curses
from time import sleep

def safe_addstr(stdscr, y, x, text, attr=None):
    """安全地在指定位置添加文本，防止越界错误"""
    height, width = stdscr.getmaxyx()
    if y < 0 or y >= height or x < 0 or x >= width:
        return False
    if x + len(text) > width:
        text = text[:width - x]
    try:
        if attr is not None:
            stdscr.addstr(y, x, text, attr)
        else:
            stdscr.addstr(y, x, text)
        return True
    except:
        return False

def draw_test_screen(stdscr):
    # 初始化curses
    curses.start_color()
    curses.use_default_colors()
    stdscr.clear()
    stdscr.refresh()
    
    # 定义16种颜色对
    for i in range(1, 8):
        curses.init_pair(i, i - 1, -1)
    
    try:
        while True:
            # 清屏
            stdscr.clear()
            
            # 获取当前终端尺寸（可能在运行时改变）
            height, width = stdscr.getmaxyx()
            
            # 顶部四个角的0
            safe_addstr(stdscr, 0, 0, '0')
            safe_addstr(stdscr, 0, width - 1, '0')
            
            # 底部四个角的0
            safe_addstr(stdscr, height - 1, 0, '0')
            safe_addstr(stdscr, height - 1, width - 1, '0')
            
            # 中间提示文字
            msg = "Press Ctrl+C to Quit screen test"
            safe_addstr(stdscr, height // 2, (width - len(msg)) // 2, msg)
            
            # 底部显示终端尺寸 (width x height)
            size_info = f"{width} x {height}"
            safe_addstr(stdscr, height - 1, (width - len(size_info)) // 2, size_info)
            
            # 顶部中间显示16种颜色的0（现在在第1行）
            if height >= 1 and width >= 16:  # 修改条件为height >= 1
                start_x = (width - 16) // 2
                for i in range(8):
                    safe_addstr(stdscr, 0, start_x + i, '0', curses.color_pair(i + 1))
            
            # 显示所有ASCII字符 (从32到126)
            ascii_chars = ''.join(chr(i) for i in range(32, 127))
            rows = (len(ascii_chars) + width - 1) // width  # 计算需要多少行
            
            start_line = 2  # 从第2行开始显示（因为颜色行现在是第0行）
            for i in range(rows):
                line_start = i * width
                line_end = line_start + width
                line = ascii_chars[line_start:line_end]
                if start_line + i < height - 2:  # 确保不覆盖底部信息
                    safe_addstr(stdscr, start_line + i, 0, line)
            
            stdscr.refresh()
            sleep(0.1)
            
    except KeyboardInterrupt:
        pass

def main():
    # 使用curses.wrapper处理异常和初始化/清理
    curses.wrapper(draw_test_screen)
    
    # 退出时显示消息
    print("\nScreen test exited. Terminal size was:", shutil.get_terminal_size())

if __name__ == "__main__":
    main()
