#!/usr/bin/env python3
# search a specific pattern under current directory
# Usage: ./my_grep.py .py

import os
import sys
import pdb

def grep(dir, pattern):
    res = []
    # pdb.set_trace()
    for f in os.listdir(dir):
        full_path = os.path.join(dir, f)
        if os.path.isfile(full_path):
            if pattern in f:
                res.append(full_path)
        elif os.path.isdir(full_path):
            res += grep(full_path, pattern)

    return res

if __name__ == '__main__':
    res = grep('.', sys.argv[1])
    print('\n'.join(res))