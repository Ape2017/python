# [模块](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200171577d6385bb5b4f4875bee9cbf0f0fa29c5000)

Python 按目录来组织模块的方法，称为包（Package）。

每个包目录下都会有一个 `__init__.py` 文件，它必须存在。否则，Python 就把该目录当成普通目录，而不是一个包。`__init__.py` 本身就是一个模块，模块名为所在的目录名。

可以有多级目录，组成多级层次的包结构。

## [使用模块](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200196665403ac40fac14536939dd5af20810782000)

查看[module_hello 模块](../scripts/module_hello.py)代码。

注意：模块名称不能有 `-` 连字符，否则导入时会引发语法错误。

### 别名

```python
# 优先使用速度更快的 cStringIO
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
```

```python
# simplejson v2.6 之前是独立的第三方库，从 2.6 开始内置
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5
```

### 作用域

正常的函数和变量名是公开的（public）。

类似 `__xxx__` 这样的变量是特殊变量，有特殊用途，比如 `__author__`, `__name__`, `__doc__` 等。

类似于 `_xxx` 和 `__xxx` 这样的函数或变量就是非公开的（private），不应该被直接引用，比如 `_abc`, `__abc` 等。

查看 [private 函数的代码](../scripts/module_greeting.py)。

## [使用第三方模块](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200214529634268c5b3b45b3a3ba1cd81a251a3b000)

在 Python 中，使用 setuptools 安装第三方模块。Python 有两个封装了 setuptools 的包管理工具：`easy_install` 和 `pip`。目前官方推荐使用 `pip`。

第三方库都会在 Python 官方的 pypi.python.org 注册。

安装 Python Imaging Library 的命令：

```sh
pip install PIL # for Python 2.x
pip install Pillow # for Python 3.x
```

> PIL 目前只支持到 Python 2.7，并且有年头没有更新了。基于 PIL 的 Pillow 项目开发非常活跃，并且支持最新的 Python 3。

其他常用的第三方库还有：

- `MySQL-python`: MySQL驱动
- `numpy`: 科学计算的 NumPy 库
- `Jinja2`: 生成文本的模版工具

### 模块搜索路径

默认情况下，Python 解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在 `sys` 模块的 `path` 变量中：

```python
import sys
sys.path
```

有两种方法，可以添加搜索路径

```python
import sys
sys.path.append('/Users/michael/my_py_scripts')
```

设置 `PYTHONPATH` 环境变量。

## [使用 __future__](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820023084e5263fe54fde4e4e8616597058cc4ba1000)

Python 提供的 `__future__` 模块，把下一个新版本的特性导入到当前版本，于是可以在当前版本中测试一些新版本的特性。

> 感觉类似 JavaScript 世界中的 Babel 转译，可以提前尝鲜。

```python

# 引入Unicode码
from __future__ import unicode_literals

# 在 2.x 中引入精确除法
from __future__ import division
```