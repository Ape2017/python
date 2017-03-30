#!/usr/bin/env python3

class Student(object):
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value
    
    # This is a read-only property, without `*.setter`
    @property
    def age(self):
        return 2017 - self._birth

s = Student()
s.score = 60
print(s.score)

try:
    s.score = 999
except ValueError:
    print('WRONG INTEGER')

s.birth = 1986
print('age: %s' % s.age)

# AttributeError: can't set attribute
# s.age = 25

class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must be negative')
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value < 0:
            raise ValueError('height must be negative')
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution:', s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution