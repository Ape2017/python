#!/usr/bin/env python3

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# exception-hierarchy: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# try...except can pass multiple layers
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    print('MAIN BEGIN...')
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()