#!/usr/bin/env python3
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001418612030427b1f1cf4ea04c41368e8a6753dca43070000

def is_odd(n):
    return n % 2 == 1

res = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
res = list(res)
print(res)

def not_empty(s):
    return s and s.strip()

res = filter(not_empty, ['A', '', 'B', None, 'C', '    '])
res = list(res)
print(res)