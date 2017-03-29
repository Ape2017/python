#!/usr/bin/env python3
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000

import functools

def log(func):
    # equals `wrapper.__name__ = func.__name__`
    @functools.wraps(func)

    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# now = log(now)
@log
def now():
    print('2017-03-29')

@log
def add(x, y):
    return(x + y)

now()
print(now.__name__)
print(add(3, 4))

# create a decorator with parameters

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017/03/29')

now()
print(now.__name__)

# exerise

print('*' * 20)
print('exercising...')

def log(func):
    def wrapper(*args, **kw):
        print('before call %s' % (func.__name__))
        res = func(*args, **kw)
        print('after call %s ' % (func.__name__))
        return res
    return wrapper

@log
def add(x, y):
    print('f is executing')
    print('%s + %s = %s' % (x, y, x+y))

add(2, 3)