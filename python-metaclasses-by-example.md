# Python metaclasses by example

http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example

作者：Eli Bendersky

日期：2011年8月14日

The aim of this article is to demonstrate a few actual uses of metaclasses in widely used Python code.

This article focuses on Python 2.6 & 2.7

## Classes are objects too

In Python, *everything* is an *object*. And that includes classes. See [code demo](scripts/create_dynamic_class.py).

## The class of a class

Python lets us examine the class of an object with the `__class__` attribute. See [code demo](scripts/metaclass_class.py).

So `type` is the class of Python classes.

## Metaclass

A metaclass is defined as "the class of a class". Any class whose instances are themselves classes, is a metaclass. `type` is a metaclass, it's the default metaclass of all classes.

When we create classes with a standard `class` definition, what Python does under the hood is the following:

* When it sees a `class` definition, Python executes it to collect the attributes (including methods) into a dictionary.
* When the `class` definition is over, Python determines the metaclass of the class. Let's call it `Meta`
* Eventually, Python executes `Meta(name, bases, dct)`, where:
    * `Meta` is the metaclasses, so this invocation is instantiating it.
    * `name` is the name of the newly created class
    * `bases` is a tuple of the class's base classes
    * `dct` maps attribute names to objects, listing all of class's attributes

If either a class or one of its bases has a `__metaclass__` attribute, it's taken as the metaclass. Otherwise, `type` is the metaclass.

So what happens when we define:

```python
class MyKlass(object):
    foo = 2
```

is this: `MyKlass` has no `__metaclass__` attribute, so `type` is used instead, and the class creation is done as:

```python
MyKlass = type(name, bases, dct)
```

If, on the other hand, `MyKlass` does have a metaclass defined:

```python
class MyKlass(object):
    __metaclass__ = MyMeta
    foo = 2
```

Then the class creation is done as:

```python
MyKlass = MyMeta(name, bases, dct)
```

So `MyMeta` should be implemented appropriately to support such calling form and return the new class. It's actually similar to writing a normal class with a pre-defined constructor signature.

## Metaclass's `__new__` and `__init__`

To control the creation and initialization of the class in the metaclass, you can implement the metaclass's `__new__` method and/or `__init__` constructor. Most real-life metaclasses will probably override just one of them. `__new__` should be implemented when you want to control the **creation of a new object (class in this case)**, and `__init__` should be implemented when you want to control the **initialization of the new object** after it has been created.

So when the call to `MyMeta` is done above, what happens under the hood is this:

```python
MyKlass = MyMeta.__new__(MyMeta, name, bases, dct)
MyMeta.__init__(MyKlass, name, bases, dct)
```

Here's a more [concrete example](scripts/metaclass_concrete_example.py).

## Metaclass's `__call__`

`__call__` is called when the already-created class is "called" to instantiate a new object. Here are [some code](scripts/metaclass_call.py) to clarify this.

## Examples

### string.Template

