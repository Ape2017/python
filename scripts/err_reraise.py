#!/usr/bin/env python3

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        # 捕获错误的目的只是记录一下，便于后续追踪。
        raise

bar()