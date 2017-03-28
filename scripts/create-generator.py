#!/usr/bin/env python3

# method 1: using tuple
print('method 1: using tuple')
g = (x*x for x in range(10))
for n in g:
    print(n)

print(10 * '*')

print('method 2: using yield')
# method 2: using `yield`
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1

for n in fib(6):
    print(n)
