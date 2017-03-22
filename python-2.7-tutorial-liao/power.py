#!/usr/bin/env python

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
	s = s * x
    return s

print ' 2^3 = ', power(2, 3)
print ' 3^3 = ', power(3, 3)
print ' 4^3 = ', power(4, 3)
print ' 4^2 = ', power(4)
