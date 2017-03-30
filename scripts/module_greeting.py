#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'This is a demo for private function'

__author__ = 'Liu Zhuan'

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)