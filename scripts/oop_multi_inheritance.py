#!/usr/bin/env python3

__author__ = 'Liu Zhuan'

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Bird(Animal):
    pass

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass 

bat = Bat()
bat.fly()