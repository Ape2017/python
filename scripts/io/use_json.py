#!/usr/bin/env python3

import json

# Write into a json string
d = dict(name='Bob', age=20, score=88)
res = json.dumps(d)
print(res)
# => {"name": "Bob", "age": 20, "score": 88}

# Read from json string
json_str = '{"age":20, "score":88, "name":"Bob"}'
res = json.loads(json_str)
print('Read complete:', res)
# => Read complete: {'age': 20, 'score': 88, 'name': 'Bob'}