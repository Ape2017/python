# [urllib](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000)

作者：廖雪峰

urllib 提供了一系列用于操作 URL 的功能。

## GET

urllib 的 `request` 模块可以很方便地抓取 URL 内容。

例如，对豆瓣的一个 URL `https://api.douban.com/v2/book/2129650` 进行抓取，并返回响应。[查看代码](../../scripts/urllib/request_douban.py)。

如果想模拟浏览器发送 GET 请求，需要使用 `Request` 对象，通过向 `Request` 对象添加 HTTP 头，就可以把请求伪装成浏览器。[查看代码](../../scripts/urllib/user_agent.py)。

## POST

如果要 POST 请求，需要把参数 `data` 以 bytes 形式传入。

模拟一个微博登录，先读取登录的邮箱和口令，然后按照 weibo.cn 的登录页的格式以 `username=xxx&password=xxx` 的编码传入。[查看代码](../../scripts/urllib/weibo_login.py)。

具体参见 Python 文档对于 [urllib](./api.md) 的详细介绍。