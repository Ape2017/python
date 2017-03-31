#!/usr/bin/env python3

from io import StringIO

# Write into StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

print(f.getvalue())

# Read from StringIO
print('*' * 30)
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())