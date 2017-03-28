#!/usr/bin/env python3
# map/reduce from Liao Xuefeng's Python Tutorial

def f(x):
    return x * x

old_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = map(f, old_lst)
# map returns a map object, should converted to list
print(list(lst))

lst2 = map(str, old_lst)
print(list(lst2))
