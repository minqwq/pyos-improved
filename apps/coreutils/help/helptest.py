import json
from typing import Dict, Any

# ANSI颜色代码
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m'
}

class CommandParser:
    def __init__(self, json_file: str):
        """初始化命令解析器
        
        Args:
            json_file: 包含命令定义的JSON文件路径
        """
        self.json_file = json_file
        self.command_data = {}
        self._load_commands()
    
    def _get_color(self, color_name: str) -> str:
        """获取ANSI颜色代码"""
        return COLORS.get(color_name.lower(), COLORS['reset'])
    
    def _load_commands(self) -> None:
        """加载并验证命令JSON文件"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if not all(key in data for key in ['meta', 'categories']):
                raise ValueError("Invalid JSON structure")
                
            self.command_data = data
            
        except FileNotFoundError:
            print(f"[错误] 文件未找到: {self.json_file}")
        except json.JSONDecodeError:
            print(f"[错误] 无效的JSON文件: {self.json_file}")
        except ValueError as e:
            print(f"[错误] 配置文件错误: {str(e)}")
    
    def show_help(self, category_filter: str = None) -> None:
        """显示帮助信息
        
        Args:
            category_filter: 可选，只显示特定类别的命令
        """
        if not self.command_data:
            print("[错误] 未加载命令数据")
            return
            
        meta = self.command_data.get('meta', {})
        categories = self.command_data.get('categories', {})
        color_settings = meta.get('colors', {})
        
        # 获取颜色配置
        title_color = self._get_color(color_settings.get('title', 'cyan'))
        category_color = self._get_color(color_settings.get('category', 'yellow'))
        command_color = self._get_color(color_settings.get('command', 'green'))
        reset_color = COLORS['reset']
        
        # 打印标题
        title = meta.get('title', 'Command List')
        subtitle = meta.get('subtitle', '')
        version = meta.get('version', '')
        
        print(f"\n{title_color}{title} - {subtitle}{reset_color}")
        if version:
            print(f"Help Interpreter Version: {version}")
        print("=" * 40)
        
        # 按类别打印命令
        for category, commands in categories.items():
            if category_filter and category.lower() != category_filter.lower():
                continue
                
            print(f"\n{category_color}[{category}]{reset_color}")
            for cmd, desc in commands.items():
                print(f"  {command_color}{cmd}{reset_color} - {desc}")
        
        # print("\n提示: 使用 'help <类别>' 可以筛选特定类别的命令")
    
    def update_command(self, category: str, command: str, description: str) -> bool:
        """添加或更新命令
        
        Args:
            category: 命令类别
            command: 命令名称
            description: 命令描述
            
        Returns:
            bool: 是否成功更新
        """
        try:
            if category not in self.command_data['categories']:
                self.command_data['categories'][category] = {}
                
            self.command_data['categories'][category][command] = description
            
            # 保存回文件
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(self.command_data, f, indent=4, ensure_ascii=False)
            return True
            
        except Exception as e:
            print(f"[错误] 更新命令失败: {str(e)}")
            return False