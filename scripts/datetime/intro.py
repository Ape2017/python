#!/usr/bin/env python3

'''
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000
作者：廖雪峰

计算机中，时间实际上使用数字表示的。把 1970 年 1 月 1 日 00:00:00 UTC+00:00 时区的时刻称为 `epoch time`，记为 0，当前时间就是相对于 epoch time 的秒数，称为 `timestamp`。

https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
日期格式化字符串编码意义如下：

Directive | Meaning                                       | Example
-- | ---------------------------------------------------- | -------
%Y | Year with century as a decimal number                | 0001, 0002, ..., 2017
%m | Month as a zero-padded decimal number                | 01, 02, ..., 12
%d | Day of the month as a zero-padded decimal number     | 01, 02, ..., 31
%H | Hour (24-hour clock) as a zero-padded decimal number | 00, 01, ..., 23
%M | Minute as a zero-padded decimal number               | 00, 01, ..., 23
%S | Second as a zero-padded decimal number               | 00, 01, ..., 23
%j | Day of the year as a zero-padded decimal number      | 001, 002, ..., 366
%a | Weekday as locale's abbreviated name                 | Sun, Mon, ..., Sat
%b | Month as locale's abbreviated name                   | Jan, Feb, ..., Dec
'''

from datetime import datetime

# datetime.now: 获取当前日期和时间
now = datetime.now()
print(now)                          # ===> 2017-04-11 11:39:55.145977
print(type(now))                    # ===> <class 'datetime.datetime'>
print(now.strftime('%j'))           # ===> 091

# 设置日期和时间
dt = datetime(2015, 6, 18, 12, 34, 56)
print(dt)                           # ===> 2015-06-18 12:34:56

# datetime.timestamp(): 获取时间戳，单位是秒，浮点数。
dt = datetime(2017, 4, 1, 11, 50)
print('timestamp:', dt.timestamp()) # ===> 1491018600.0

# datetime.fromtimestamp(): 从时间戳获取日期时间
t = 1491018600.0
print(datetime.fromtimestamp(t))    # ===> 2017-04-01 11:50:00

# datetime.utcfromtimestamp(): 从时间戳获取 UTC 标准时区的时间
t = 1491018600.0
print(datetime.utcfromtimestamp(t)) # ===> 2017-04-01 03:50:00

# datetime.strptime: 字符串转换成时间。
cday = datetime.strptime('2017-4-11 11:58:00', '%Y-%m-%d %H:%M:%S')
print(cday)                         # ===> 2017-04-11 11:58:00

# datetime.strftime: 时间日期转换为字符串
now = datetime.now()
res = now.strftime('%a, %b %d %H:%M')
print(res)                          # ===> Sat, Apr 01 13:43

# datetime + timedelta: 日期的增减
from datetime import timedelta
now = datetime.now()
later = now + timedelta(hours=10)
print(later)                        # ===> 2017-04-01 23:46:12.455222
before = now - timedelta(days=1)
print(before)                       # ===> 2017-03-31 13:46:12.455222
later = now + timedelta(days=2, hours=12)
print(later)                        # ===> 2017-04-04 01:46:12.455222

# 本地时间转换为 UTC 时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
print(now)                          # ===> 2017-04-01 13:51:23.488386
print(dt)                           # ===> 2017-04-01 13:51:23.488386+08:00

# 时区转换
# 先通过 `utcnow()` 拿到当前的 UTC 时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('   utc_dt:', utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('    bj_dt:', bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(' tokyo_dt:', tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt2:', tokyo_dt2)