# Python 2.7 教程

by 廖雪峰

## [函数](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013747383144265f6402ab37cc40c5aecc816c08d8b771000)

2017-03-21 19:06

## 调用函数

* abs()
* help()
* cmp()
* int()
* float()
* str()
* unicode()
* bool()

## 定义函数

空函数

```python
def nop():
    pass
```

## 返回多个值

## [函数的参数](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738449338c8a122a7f2e047899fc162f4a7205ea3000)

2017-03-21 19:20

** 默认对象必须指向不变对象！**

```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

### 可变参数

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

### 关键字参数

关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

```python
def Person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

Person('Bob', 23, city='Beijing')
# name: Bob age: 23 other: {city:'Beijing'}
```

## 递归函数

解决递归调用栈溢出的方法是通过**尾递归优化**，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

## 迭代

```python
for key in d
for value in d.itervalues()
for k,v in d.iteritems()
```

如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

```python
from collections import Iterable
isinstance('ABC', Iterable)
```

如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

```python
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
```

## [列表生成式](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681963899940a998c0ace64bb5ad45d1b56b103c48000)
