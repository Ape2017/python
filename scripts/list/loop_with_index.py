#!/usr/bin/env python3

'''
A pythonic solution

Source: http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
Author: Mike Hordecki
Date: 2009/02/06
'''

lst = ['liuz', 'monica', 'foo', 'bar']
for idx, val in enumerate(lst):
    print(idx, val)