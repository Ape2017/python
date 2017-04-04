#!/usr/bin/env python3

import hashlib

md5 = hashlib.md5()

# Feeding string objects into update() is not supported, as hashes work on bytes, not on characters.
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))

print(md5.hexdigest())
# ===> d26a53750bc40b38b65a520292f69306

# 如果数据量很大，可以分块多次调用 `update()`，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# ===> d26a53750bc40b38b65a520292f69306