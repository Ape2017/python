#!/usr/bin/env python3

import pickle

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print('After pickle:', d)

print('Outside pickle:', d)