#!/usr/bin/env python3
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0014186131194415d50558b7a1c424f9fb52b84dc9c965c000

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f()) # f is called `Closure`

# local variables changes
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())

# bind local variables into func
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())