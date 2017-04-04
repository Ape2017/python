#!/usr/bin/env python3

import hashlib

sha1 = hashlib.sha1()
sha1.update(b'how to use sha1 in ')
sha1.update(b'python hashlib?')
print(sha1.hexdigest())
# ===> 2c76b57293ce30acef38d98f6046927161b46a44