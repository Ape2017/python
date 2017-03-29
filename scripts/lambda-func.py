#!/usr/bin/env python3
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868198760391f49337a8bd847978adea85f0a535591000

res = map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(res))

f = lambda x: x * x
print(f(5))

def build(x, y):
    return lambda: x * x + y * y
res = build(7, 8)
print(res)
print(res())