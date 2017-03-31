#!/usr/bin/env python3

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def __str__(self):
        return 'Student (name=%s, age=%s, score=%s)' % (self.name, self.age, self.score)

class Teacher(object):
    def __init__(self, name, job):
        self.name = name
        self.job = job

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Liu Zhuan', 25, 100)
print(json.dumps(s, default=lambda obj:obj.__dict__))

t = Teacher('Miss Zhang', 'Math')
print(json.dumps(t, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age":20, "score":88, "name":"Bob"}'
print(json.loads(json_str, object_hook=dict2student))