#!/usr/bin/env python3

# Use type to dynamically craate new class
def fn(self, name='world'):
    print('Hello, %s.' % name)

# class_name, sup_class, attributes
Hello = type('Hello', (object,), dict(hello=fn)) # Create Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# metaclass => class => instance
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)

print('=' * 20)
print('ORM Begin ....')

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# There are lots of code, which I don't understand, so omit them.
# ...
# ...

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()