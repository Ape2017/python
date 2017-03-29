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