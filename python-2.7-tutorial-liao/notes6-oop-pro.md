# [面向对象高级编程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820058291028118ddeefc4de7860a8e48b9942e9b000)

作者：廖雪峰

涉及到的概念有：多重继承、定制类、元类等。

## 使用 `__slots__`

Python 允许在定义 class 时，使用 `__slots__` 特殊变量限制实例的属性。

查看[代码实例](../scripts/oop_slots.py)。

## 使用 @property

`@property` 广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查。可以减少程序运行时出错的可能性。

查看[代码实例](../scripts/oop_property.py)。

## 多重继承

通过多重继承，一个子类就可以同时获得多个父类的所有功能。查看[代码实例](../scripts/oop_multi_inheritance.py)。

### Mixin

通过多重继承实现的设计，叫做 `Mixin` 。

Python 自带的很多库也使用了 Mixin。比如，`TCPServer` 和 `UDPServer` 两类网络服务。要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由 `ForkingMixIn` 和 `ThreadingMixIn` 提供。通过组合，就可创造出合适的服务来。

```python
# 多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
```

只允许单一继承的语言（如Java）不能使用 Mixin 的设计。

## 定制类

`__str__`, `__repr__` 让类在 print 打印输出时，信息更友好。

`__getattr__` 让动态属性和动态方法成为可能。

`__iter__`, `__next__`, `__getitem__` 让类的行为更像列表。

`__call__` 让实例像函数一样可以执行调用。

查看[代码实例](../scripts/oop_custom_class.py)。

## 使用枚举类

Python 提供 `Enum` 类实现枚举类型。查看[代码实例](../scripts/oop_enum.py)。

## 使用元类

动态语言和静态语言最大的不同，就是函数和类的定义，不是在编译时定义的，而是运行时动态创建的。

> 元类比较复杂，此处没有学习明白。需要单独学习。