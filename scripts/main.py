#!/usr/bin/env python3
import module_greeting

greeting = module_greeting.greeting
while True:
    print('What is your name?')
    name = input()
    if name.strip() == '':
        break
    res = greeting(name)
    print(res)
    print(len(res) * '*')