# WSGI interface

http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012393132788f71e0edad4676a3f76ac7776f3a16000

Author: Liao Xuefeng

WSGI: Web Server Gateway Interface

Let's look at a simple "Hello, web!"

```python
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
```

上面的 `application()` 函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

* `environ`：一个包含所有HTTP请求信息的dict对象；
* `start_response`：一个发送HTTP响应的函数。

在application()函数中，调用：

```python
start_response('200 OK', [('Content-Type', 'text/html')])
```

就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次 `start_response()` 函数。`start_response()` 函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。

Python内置了一个WSGI服务器，这个模块叫 `wsgiref` ，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

## 运行 WSGI 服务

Create `server.py`, it will run WSGI server, and load `application()` function.

```python
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000....')
httpd.serve_forever()
```

[server.py](./scripts/server.py)
