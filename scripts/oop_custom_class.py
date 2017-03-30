#!/usr/bin/env python3

class Student(object):
    def __init__(self, name):
        self.name = name

    # make print more prettier
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # make repr pretty too 
    __repr__ = __str__

    # dynamically return a attribute
    # only not found attributes will invoke `__getattr__`
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        # return a func
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student('Liu Zhuan')
print(s)
print('s.score is %d.' % s.score)
print('s.age is %d.' % s.age())

# raise AttributeError when non-found attribute is invoked.
# print(s.abc)

print('Create Fib class...')
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100: # condition for exiting loop
            raise StopIteration()
        return self.a
    
    # behaves like list or tuple
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
    
    def __setitem__(self, value):
        pass
    
    def __delitem(self, value):
        pass

for n in Fib():
    print(n)

print('Fib()[5] = %d.' % Fib()[5])

f = Fib()
print(f[0:5])
print(f[:10])

print('Chain Object Init...')

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        if path == 'users':
            return lambda x:Chain('%s/users/%s' % (self._path, x))
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    
    __repr__ = __str__

print(Chain())
print(Chain().status)
print(Chain().status.user.timeline.list)
print(Chain().users('michael').repos)

# `__call__`
print('=' * 20)
print('`__call__` begin...')

class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

print('s is callable?', callable(s))