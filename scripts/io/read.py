#!/usr/bin/env python3

try:
    f = open('./data.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()