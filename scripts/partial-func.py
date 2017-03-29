#!/usr/bin/env python3
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819893624a7edc0e3e3df4d5d852a352b037c93ec000

import functools

int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1000000', base=10))