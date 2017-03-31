#!/usr/bin/env python3

# Write into BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# Read from BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
res = f.read()
print(res)