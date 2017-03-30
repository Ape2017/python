#!/usr/bin/env python

# classes can be created at runtime
def make_myklass(**kwattrs):
    return type('MyKlass', (object,), dict(**kwattrs))

myklass_foo_bar = make_myklass(foo=2, bar=4)

# myklass_foo_bar is equivalent to:
# class MyKlass(object):
#     foo = 2
#     bar = 4

print myklass_foo_bar
x = myklass_foo_bar()
print x
print x.foo, x.bar