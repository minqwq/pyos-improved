# PY OS Improved 第三方软件开发规范

## 目录

- [1. 第三方软件打包规范](#1-第三方软件打包规范)
  - [1.1 主程序文件名](#11-主程序文件名)
  - [1.2 程序依赖库（即需要的模块）](#12-程序依赖库即需要的模块)
  - [1.3 软件基本信息文件](#13-软件基本信息文件)
  - [1.4 第三方软件包名](#14-第三方软件包名)
  - [1.5 软件包文件目录结构](#15-软件包文件目录结构)
  - [1.6 软件包封装格式](#16-软件包封装格式)
  - [1.7 软件包兼容性](#17-软件包兼容性)
- [2. 第三方软件代码规范](#2-第三方软件代码规范)
  - [2.1 注释](#21-注释)
  - [2.2 报错](#22-报错)
  - [2.3 代码测试](#23-代码测试)
- [3. 第三方软件安装&卸载](#3-第三方软件安装卸载)
  - [3.1 使用Shizuku安装&卸载](#31-使用shizuku安装卸载)
  - [3.2 手动安装&卸载](#32-手动安装卸载)
- [4. 补充说明](#4-补充说明)

## 1. 第三方软件打包规范

### 1.1 主程序文件名

在被打包好的第三方软件包中，主程序文件名必须为`main.py`。

当用户在 PY OS Improved 终端中使用 shizuku 安装软件时，会读取该软件包中的`info.json`文件（下文将详细介绍），并根据`info.json`文件中`name`字段的值重命名释放出的主程序文件。

本地模块/配置文件等文件名不作规范要求，但请确保文件名不与其他软件包中的文件名重复。

### 1.2 程序依赖库（即需要的模块）

PY OS Improved 第三方软件在使用官方应用打包程序时，必须包含一个`requirements.txt`文件。

> 例如：`requirements.txt`文件内容如下：

``` txt
pygame
numpy
```

> 该文件中列出了该软件依赖的`pygame`和`numpy`库，在 PY OS Improved 终端中使用 shizuku 安装软件时，会自动调用 pip 安装这两个库。

如果您的应用不需要调用任何第三方库，也必须包含`requirements.txt`文件，但内容如下：

``` txt
# No such library needed
```

> 该文件内容为空，表示该软件不需要调用任何第三方库。shizuku会自动跳过安装依赖库的步骤。

### 1.3 软件基本信息文件

PY OS Improved 第三方软件包必须包含一个`info.json`文件，该文件中包含软件包的基本信息，包括软件包名、版本号、作者、描述、分类、标签等。

> 例如：`info.json`文件内容如下：

``` json
{
    "name": "example",
    "version": "1.0.0",
    "author": "developer",
    "description": "This is an example software package.",
    "category": "example",
    "tags": ["example", "example_tag"],
    "min_python_version": "3.8",
    "target_python_version": "3.12",
    "compatible_os": "windows"
}
```

> 该文件中包含软件包名为`example`、版本号为`1.0.0`、作者为`developer`、描述为`This is an example software package.`、分类为`example`、标签为`example`和`example_tag`、最低 Python 版本为`3.8`、目标 Python 版本为`3.12`、兼容性最佳操作系统为`windows`。

PY OS Improved 第三方软件包的安装、更新、卸载等操作，均需要读取该文件中的信息，所以请务必填写完整。

### 1.4 第三方软件包名

PY OS Improved 第三方软件包名必须遵循以下规范：

- 包名全部小写，多个单词使用下划线连接。
- 包名不得与已有软件包名和系统命令名重复。
- 包名会在安装完成后自动重命名给主程序py文件

> 例如：包名为`example`的软件包安装完成后主程序文件名为`example.py`，包名为`my_module`的软件包安装完成后主程序文件名为`my_module.py`。

### 1.5 软件包文件目录结构

软件包文件目录结构必须遵循以下规范：

``` txt
(! 必需文件) (? 可选文件)

软件包(example.sap)
├── ? data
│   ├── ? config.json
├── ? resources
│   ├── ? example.png
│   ├── ? example.wav
├── ? depends
│   ├── ? module1.py
│   ├── ? module2.py
├── ? docs
│   ├── ? UserGuide.md
│   ├── ? Tips.txt
├── ! main.py
├── ! requiarements.txt
├── ! info.json
├── ? README.md
├── ? icon.png
├── ? LICENSE
......

(总结：主程序文件、依赖库文件、应用基本信息文件必须存在，其余可选)
```

**需要注意的是**：

- `配置文件`：如果您的软件需要读取配置文件，则必须放在`data`目录下。<br>(未来 PY OS Improved 可能会强制`/data/apps/`目录下为只读，应用只能将数据存储在`/data/data/"软件包名"/`下)
- `资源文件`：如果您的软件需要使用资源文件，则必须放在`resources`目录下，并以资源文件名命名。
- `依赖库文件`：如果您的软件需要调用您自己准备的本地库，则必须放在`depends`目录下，并以库文件名命名。

### 1.6 软件包封装格式

PY OS Improved 第三方软件包必须使用`sap`格式封装（Shizuku Application Package）。其原理为使用`zipfile`模块将软件文件打包成`zip`格式，并将文件扩展名修改为`.sap`。

> 例如：打包为`example.zip`后，经 **PY OS Improved 应用程序打包程序** 修改扩展名，得到`example.sap`。

同理，安装软件时，Shizuku Software Manager 会自动将`.sap`格式的软件包解压到/data/apps/"app_name"/目录下，并重命名主程序文件名。

### 1.7 软件包兼容性

因 PY OS Improved 主要基于 **Python 3.8** 版本开发，所以第三方软件包必须保证兼容该版本。

如果您的软件包不兼容更低版本的 Python，请在`info.json`文件中`min_python_version`和`target_python_version`指定具体版本号。

另外，PY OS Improved 未来可能会整理出系统API，以便第三方软件开发者可以更方便地调用系统功能。但由于现在的核心代码堆成屎山(bushi)，所以短时间内不太有可能给予公示。

所以现阶段的第三方软件开发者，请尽量使您的软件尽可能适配兼容 PY OS Improved。

## 2. 第三方软件代码规范

### 2.1 注释

请在您的代码头部添加注释，包括但不限于软件包名、版本号、作者、描述、分类、标签等。

以下两种注释方式均可：

``` python
#!/usr/bin/env python3

"""
@ Name: DE_NumGuess
@ Auther: ElofHew
@ Version: 2.3
@ Description: A simple number guessing game.
@ Date: 2025.01.01
"""
```

``` python
#!/usr/bin/env python3

# Name: DE_NumGuess
# Auther: ElofHew
# Version: 2.3
# Description: A simple number guessing game.
# Date: 2025.01.01
```

### 2.2 报错

我们建议您在代码中使用`try-except`语句尽可能捕获并处理可能出现的错误。

``` python
try:
    # 可能出现的错误代码
except Exception as e:
    print("Error:", e)
```

### 2.3 代码测试

请确保您的软件包经过充分测试，确保其功能正常运行。

如果您的软件包尚未完成测试，请在软件包的`README.md`文件中说明测试方法。并且发布软件包时，在您计划的包名后加入`_beta`、`_alpha`等字样，以示测试版本。

> 例如：`example`发布测试版本为`example_beta`、发布正式版本为`example`。

## 3. 第三方软件安装&卸载

### 3.1 使用Shizuku安装&卸载

如果您的软件包已经经过测试，可以直接使用Shizuku软件管理器安装。

``` txt
shizuku install example.sap
```

按照提示安装完成后，使用以下命令启动第三方应用程序：

``` txt
szk example
```

如需卸载软件包，请使用以下命令：

``` txt
shizuku remove example
```

按照提示即可完成卸载。

### 3.2 手动安装&卸载

如果您的软件包尚未经过测试，或者您不想使用Shizuku软件管理器安装，可以手动将软件包解压到/data/apps/"app_name"/目录下，并重命名主程序文件名。

> [!TIP]
> 请确保"app_name"、"main.py"与软件包名一致（例如文件夹改为example，文件改为example.py），否则会导致启动失败。

按照上述步骤完成后，使用以下命令启动第三方应用程序：

``` txt
szk example
```

如需卸载软件包，可以手动删除/data/apps/"app_name"/目录。

## 4. 补充说明

PY OS Improved 第三方软件开发规范仅供参考，开发者可以根据实际情况适当添加自己的想法。

<hr>
<p align="center">—— PY OS Improved 第三方软件开发规范 ——</p>
<p align="center">—— 2025.05.01 更新——</p>
