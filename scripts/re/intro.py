#!/usr/bin/env python3

'''
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
作者：廖雪峰

\d    一个数字
\w    一个字母或数字
\s    一个空格
.     任意字符

*     任意个字符（包括0个）
+     至少一个字符
?     0个或1个字符
{n}   n个字符
{n,m} n-m个字符

[]    匹配范围
A|B   匹配A或B
^     匹配开头
$     匹配结尾

常用的正则表达式函数如下：

* re.match           判断是否匹配成功
* re.split           拆分字符串
* re.compile         编译正则表达式
* match.group(index) 按位置获取匹配组
* match.groups()     获取所有匹配组

'''

import re

# re.match: 判断是否匹配成功
match = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(match) # ===> <_sre.SRE_Match object; span=(0,9), match='010-12345'>

match = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(match) # ===> None

def is_matched(str):
    if re.match(r'^\d{3}\-\d{3,8}', str):
        print(str, 'is matched? ok')
    else:
        print(str, 'is matched? failed')

is_matched('010-12345')
is_matched('010 12345')

# re.split: 切分字符串
res = re.split(r'\s+', 'a b       c')
print(res)

res = re.split(r'[\s,]+', 'a, b, c       d')
print(res)

res = re.split(r'[\s,;]+', 'a, b;; c       d;e')
print(res)

# match.group: 提取分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print('group[0]:', m.group(0))
print('group[1]:', m.group(1))
print('group[2]:', m.group(2))
print('groups:', m.groups())

# 贪婪匹配：默认模式
res = re.match(r'^(\d+)(0*)$', '102300').groups()
print('贪婪：', res)

# 非贪婪匹配，数量词后增加 `?`
res = re.match(r'^(\d+?)(0*)$', '102300').groups()
print('非贪婪：', res)

# re.compile: 编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

res1 = re_telephone.match('010-12345').groups()
print(res1)

res2 = re_telephone.match('010-8086').groups()
print(res2)