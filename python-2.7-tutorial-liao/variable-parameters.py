#!/usr/bin/env python

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2)
print calc(1, 2, 3)
print calc(1, 2, 3, 4)
print calc(*[1, 2, 3, 4, 5])
