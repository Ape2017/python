#!/usr/bin/env python3

class Student(object):
    pass

s = Student()
s.name = 'Liu Zhuan'
print(s.name)

# Add a method to a specific instance
def set_age(self, age):
    self.age = age
    
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# dynamicly added function not working for another instance
s2 = Student()
try:
    s2.set_age(10)
except AttributeError:
    print('can not find set_age function')

# Add method to Class
def set_score(self, score):
    self.score = score
Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)

# `__slots__` could limit dynamic attributes
print('Use `__slots__` to limit dynamic attributes')

class Student(object):
    __slots__ = ('name', 'age') # use tuple to define permitted attribute names

s = Student()
s.name = 'Liu Zhuan __slots__'
s.age = 25

try:
    s.score = 99
except AttributeError:
    print('Warning: s can not have score attribute now!')

# __slots__ do not work on subclass
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
print('g.score = %s' % g.score)