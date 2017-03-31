# [错误、调试和测试](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431913726557e5e43e1ee8d54ee486bddc3f607afb75000)

作者：廖雪峰

Python 的 `pdb` 可以单步执行代码。

## 错误处理

Python 内置了一套 `try...except...finally...` 的错误处理机制。查看[代码](../scripts/try_catch_finally.py)。

## 调试

1. 使用 `print`。查看[代码](../scripts/debug/do_print.py)
2. 使用 `assert` 断言。查看[代码](../scripts/debug/do_assert.py)。启动 Python 解释器时可用 `-O` 参数关闭断言。
3. 使用 `logging`，不会抛出错误，而且可以输出到文件。查看[代码](../scripts/debug/do_logging.py)。
4. 使用 `pdb` 单步调试。`python3 -m pdb err.py`。查看[代码](../scripts/debug/do_pdb.py)
    * `pdb.set_trace()` 设置断点

## 单元测试

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。查看[代码](../scripts/unittest/mydict_test.py)。

## 文档测试

是一种在代码中书写测试代码的方式，Python 内置的“文档测试”（doctest）模块可用直接提取注释中的代码并执行测试。

> 实际测试中，即使注释了 `__getattr__()` 方法，依然没有报错。后来发现是缺少了 `doctest.testmod()` 的方法执行。查看[代码](../scripts/unittest/mydict2.py)。

