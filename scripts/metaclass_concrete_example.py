#!/usr/bin/env python

dash_len = 40

# These print-outs are done at class creation time
class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print '-' * dash_len
        print 'Allocating memory for class', name
        print meta
        print bases
        print dct
        return super(MyMeta, meta).__new__(meta, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        print '-' * dash_len
        print 'Initializing class', name
        print cls
        print bases
        print dct
        super(MyMeta, cls).__init__(name, bases, dct)

class MyKlass(object):
    __metaclass__ = MyMeta
    def foo(self, param=1):
        pass
    barattr = 2