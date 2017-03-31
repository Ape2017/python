#!/usr/bin/env python3

import pickle

d = dict(name='Bob', age=20, score=88)

# pickle any object into bytes
res = pickle.dumps(d)

print('After pickle:', res)

with open('dump.txt', 'wb') as f:
    # Write into a file-like object
    pickle.dump(d, f)