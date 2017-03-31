#!/usr/bin/env python3

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')