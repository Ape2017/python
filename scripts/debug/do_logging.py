#!/usr/bin/env python3

import logging

# 配置记录信息的级别，有 `debug`, `info`, `warning`, `error` 几个级别
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)