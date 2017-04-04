# itertools

来源：[廖雪峰的Python教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200162233153835cfdd1a541a18ddc15059e3ddeec000)

Python 的内建模块 itertools 提供了非常有用的用于操作迭代对象的函数。

## count() - 无限迭代器

```python
import itertools
natuals = itertools.count(1)
for n in natuals:
    print(n)
```

## cycle() - 无限重复传人的序列

```python
import itertools
cs = itertools.cycle('ABC')
for c in cs:
    print(c)
```

## repeat() - 无限重复某一元素

```python
# 第二个参数可以限定重复次数
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)
```

无限序列虽然可以无限迭代下去，但是通常我们会通过`takewhile()` 等函数根据条件判断来截取出一个有限的序列：

```python
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10, natuals)
list(ns)
```

## chain() - 串联迭代对象，形成更大的迭代器

```python
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
```

## groupby() - 相邻的重复元素挑出来放在一起

```python
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C, 'C']
# A ['A', 'A', 'A']
```