#!/usr/bin/env python

age = raw_input("How old are you? ")
age = int(age)

if age >= 18:
    print 'Adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'
