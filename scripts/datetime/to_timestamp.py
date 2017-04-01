#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000

作者：廖雪峰
练习：假设你获取了用户输入的日期和时间如 2015-1-21 9:01:30，以及一个时区信息如 UTC+5:00，均是str，请编写一个函数将其转换为 timestamp：
'''

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    tzinfo = get_tzinfo(tz_str)
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt = dt.replace(tzinfo=tzinfo)

    return dt.timestamp()

def get_tzinfo(tz_str):
    re_timezone = re.compile(r'^UTC([\+\-]\d{1,2}):(\d{2})$')
    groups = re_timezone.match(tz_str).groups()
    hours, minutes = map(int, groups)
    return timezone(timedelta(hours=hours, minutes=minutes))

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')