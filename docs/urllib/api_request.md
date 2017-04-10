# urllib.request - 打开 URL 的扩展包

来源：[python 官网](https://docs.python.org/3.6/library/urllib.request.html#module-urllib.request)

`urllib.request` 模块定义了一些函数和类，有助于在复杂世界中打开 URL（大部分都是 HTTP）--- 基本和摘要验证，重定向，cookies 以及更多。

> 对于更抽象的 HTTP 客户端接口，推荐使用 [Requests 包](http://docs.python-requests.org/en/master/)。

`urllib.request` 模块定义了如下函数：

* urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)

打开 `url`，它可以是字符串或者 `Request` 对象。