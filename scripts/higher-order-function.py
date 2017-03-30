#!/usr/bin/env python3
# code from:
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819873910807d8c322ca74d269c9f80f747330a52000
 
# `add` is `higher order function`
def add(x, y, f):
    return f(x) + f(y)

res = add(-5, 6, abs)
print('add(-5, 6, abs) =', res)
