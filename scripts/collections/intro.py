#!/usr/bin/env python3

'''
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431953239820157155d21c494e5786fce303f3018c86000

作者：廖雪峰

内建的集合类有：
* namedtuple:  自定义 tuple 对象
* deque:       双向列表，插入和删除效率高
* defaultdict: 提供默认键值的字典
* OrderedDict: 保持键值顺序的字典
* Counter:     简单计数器
'''

# namedtuple: 自定义 tuple 对象
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y, p[0], p[1])     # ===> 1 2 1 2
print(isinstance(p, Point))     # ===> True
print(isinstance(p, tuple))     # ===> True
print(isinstance(Point, tuple)) # ===> False

# deque: 高效实现插入和删除操作的双向列表
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q) # ===> deque(['y', 'a', 'b', 'c', 'x'])

# defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # ===> abc
print(dd['key2']) # ===> N/A

# OrderedDict: 保持 key 的顺序
from collections import OrderedDict
d = dict([('a', 1), ('c', 3), ('b', 2)])
print(d) # ===> {'a':1, 'b':3, 'b':2}
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print(od) # ===> OrderedDict([('a', 1), ('c', 3), ('b', 2)])

# Counter: 简单计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# ===> Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})