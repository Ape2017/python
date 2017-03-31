#!/usr/bin/env python3

print('open with `with`...')
with open('data.txt', 'r') as f:
    print(f.read())

print('open as binary ...')
with open('data.txt', 'rb') as f:
    print(f.read())

# use readlines() to read file
print('='*5, 'readlines()', '='*5)
with open('data.txt', 'r') as f:
    num = 0
    for line in f.readlines():
        num = num + 1
        print(num, line.strip())

# read binary file
with open('../../assets/avatar_github.png', 'rb') as f:
    data = f.read()
    print(data)

with open('../../assets/avatar_github_thumb.jpg', 'rb') as f:
    data = f.read()
    print(data)

from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))