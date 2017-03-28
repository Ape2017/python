#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file = open('data.txt')
data = file.read().strip()
print('Enter your password')
word = input()

if word == data:
    print('Access granted')
    if word == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')
