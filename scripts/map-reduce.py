#!/usr/bin/env python3
# map/reduce from Liao Xuefeng's Python Tutorial
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00141861202544241651579c69d4399a9aa135afef28c44000

# python3 needs import functools, which python2 need not.
from functools import reduce

print('map start...')
def f(x):
    return x * x

old_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = map(f, old_lst)
# map returns a map object, should converted to list
print(list(lst))

# Change to string type
lst2 = map(str, old_lst)
print(list(lst2))

# Convert to first char capitalized
def format_title(val):
    return val.title()

res = map(format_title, ['adam', 'LISA', 'barT'])
res = list(res)
print(res)

# reduce

print('*' * 30)
print('reduce start...')
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 4, 5, 7, 9]))