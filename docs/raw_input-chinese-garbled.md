# [如何在raw_input() 用中文做提示](http://www.xshell.net/python/raw_input.html)

Author: 破冰

Date: 2013/07/29

PYTHON 2.X 在使用 `raw_input()` 时，如果用中文做提示 `raw_input(u'中文')` ，会提示乱码，解决办法：
`raw_input(u'中文'.encode('gbk'))` ,即可解决乱码问题，中文 CMD 编码默认为 GB2312。
