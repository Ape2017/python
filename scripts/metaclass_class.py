#!/usr/bin/env python

class SomeKlass(object):
    pass

someobject = SomeKlass()
print 'someobject.__class__:', someobject.__class__
# ===> <class '__main__.SomeKlass'>
print 'SomeKlass.__class__:', SomeKlass.__class__
# ===> <type 'type'>