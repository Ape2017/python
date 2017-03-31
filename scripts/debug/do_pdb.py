#!/usr/bin/env python3

import pdb

s = '0'
n = int(s)
pdb.set_trace() # set a breakpoint
print(10 / n)

# python -m pdb do_pdb.py
# l: list code
# n: next line
# c: continue run code
# p: print variable value
# q: quit pdb