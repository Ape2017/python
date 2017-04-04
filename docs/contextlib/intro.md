# contextlib

来源：[廖雪峰的Python教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001478651770626de401ff1c0d94f379774cabd842222ff000)

任何对象，只要正确实现了上下文管理，就可以使用 `with` 语句。

实现上下文管理是通过 `__enter__` 和 `__exit__` 两个方法实现的。查看[代码](../../scripts/contextlib/use_with.py)。