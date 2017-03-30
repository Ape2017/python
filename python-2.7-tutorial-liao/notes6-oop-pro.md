# [面向对象高级编程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820058291028118ddeefc4de7860a8e48b9942e9b000)

作者：廖雪峰

涉及到的概念有：多重继承、定制类、元类等。

## 使用 `__slots__`

Python 允许在定义 class 时，使用 `__slots__` 特殊变量限制实例的属性。

查看[代码实例](../scripts/oop_slots.py)。

## 使用 @property

`@property` 广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查。可以减少程序运行时出错的可能性。

查看[代码实例](../scripts/oop_property.py)。