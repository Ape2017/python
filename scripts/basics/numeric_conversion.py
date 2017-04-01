#!/usr/bin/env python3

'''
http://www.pythontab.com/html/2013/pythonjichu_0102/86.html

作者：不详

数值之间转换函数包括：

int, bin, oct, hex
'''

# int: 其他进制 => 十进制
print(int('100', 2))  # ===> 4
print(int('10', 8))   # ===> 8
print(int('0xf', 16)) # ===> 15

# bin: 十进制 => 二进制
print(bin(10))        # ===> 0b1010

# oct: 十进制 => 八进制
print(oct(10))        # ===> 0o12

# hex: 十进制 => 十六进制
print(hex(17))        # ===> 0x11