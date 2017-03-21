# Python 2.7 教程

by 廖雪峰

## [数据类型和变量](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738264643de15c5c4abad47dd9510e3b86286acb8000)

Python 允许用 `r''` 表示 `''` 内部的字符串默认不转义；Python 允许用 `'''...'''` 表示多行内容。

布尔值可用 `and`, `or` 和 `not` 运算。

## 字符串和编码

计算机系统通用的字符编码工作方式：

在内存中，统一使用 Unicode 编码，当需要保存到硬盘或者需要传输时，就转换为 UTF-8 编码。

char => `ord()` => ASCII => `chr()` => char

Python 以 Unicode 表示的字符串用 `u'...'` 表示。把 `u'xxx'` 转换为 UTF-8 编码的 'xxx' 用 `encode('utf-8')`方法：

```python
u'ABC'.encode('utf-8')
u'中文'.encode('utf-8')
```

反过来，把 UTF-8 编码表示的字符串 `'xxx'` 转换为 Unicode 字符串 `u'xxx'` 用 `decode('utf-8')` 方法：

```python
'abc'.decode('utf-8')
```

当源代码包含中文时，通常在文件头写上:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

## 使用 list 和 tuple

* `len()`: 获取元素个数
* `append()`: 增加到尾部
* `insert(idx, item)`: 插入到指定位置
* `pop()`: 删除末尾元素
    * `pop(i)`: 删除指定位置元素

## 条件判断和循环

```python
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'
```

```python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
```

## 使用 dict 和 set

```python
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
```

要避免 key 不存在的错误，有两种办法：

* `in` 判断
* `get()` 方法, 比如 `d.get('Thomas', -1)`

要删除一个 key, 用 `pop(key)` 方法，对应的 value 也会从 dict 中删除：

```python
d.pop('Bob')
```

dict 的 key 必须是不可变对象。

### set

set 和 dict 类似，也是一组 key 的集合，但不存储 value 。在 set 中，没有重复的 key 。

要创建一个 set ，需要提供一个 list 作为输入集合：

```python
s = set([1, 2, 3])
```

常用的函数

* `add(key)`: 添加元素
* `remove(key)`: 删除元素

set 可用看成数学意义上的无序和无重复的集合，因此，两个 set 可用做数学意义上的并集、交集等操作：

```python
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2
```

2017-03-21 19:05
