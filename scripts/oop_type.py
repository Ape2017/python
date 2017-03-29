#!/usr/bin/env python3

print(type(123))
print(type('str'))
print(type(None))

print(type(abs))

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
print(type(a))

print(type(123) == type(245))

import types
print(type('abc') == str)

def fn():
    pass

print('fn: ', type(fn) == types.FunctionType)
print('abs: ', type(abs) == types.BuiltinFunctionType)
print('lambda: ', type(lambda x:x) == types.LambdaType)
print('generator: ', type((x for x in range(10))) == types.GeneratorType)
print('animal: ', type(a))

print('=' * 20)
print('Use isinstance()')

d = Dog()
h = Husky()

print('h is husky? ', isinstance(h, Husky))
print('h is dog? ', isinstance(h, Dog))
print(isinstance(h, (Dog, Husky)))

# use dir()
print(dir('ABC'))

# __len__ is a special attribute
class MyObject(object):
    def __len__(self):
        return 100

obj = MyObject()
print('len: ', len(obj))

# getattr(), setattr(), hasattr()
print('=' * 20)
print('hasattr, setattr, getattr BEGIN')
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print('has x attr? ', hasattr(obj, 'x'))
print('has y attr? ', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('has y attr? ', hasattr(obj, 'y'))
print('obj.y = ', getattr(obj, 'y'))
print('obj.z = ', getattr(obj, 'z', 404))