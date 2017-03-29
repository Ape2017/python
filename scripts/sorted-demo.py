#!/usr/bin/env python3
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001418612033918f1f341b1e0f14762a118891fa52949aa000

res = sorted([36, 5, 12, 9, 21])
print(res)

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

# python 2
# sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
# res = sorted([36, 5, 12, 9, 21], reversed_cmp)
# print(res)

# python 3
# sorted(iterable, /, *, key=None, reverse=False)

# sorted by absolute value
res = sorted([36, 5, -12, 9, -21], key=abs)
print(res)

# sorted ignore case
res = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(res)

# reverse sorted
res = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(res)

# sorted by name
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
res = sorted(L, key=by_name)
print(res)