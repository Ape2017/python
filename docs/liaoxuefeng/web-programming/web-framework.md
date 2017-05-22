# Using Web Framework

http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012745805707cb9f00a484d968c72dbb7cfc90b91000

Author: Liao Xuefeng

[Flash](http://flask.pocoo.org/)

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.

> **Werkzeug**: Werkzeug is a WSGI utility library for Python. It's widely used and BSD licensed. http://werkzeug.pocoo.org/
> **Jinja**: Jinja2 is a full featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed. http://jinja.pocoo.org/
> **pocoo**: The Pocoo Team consists of people from the Python community that are working under one umbrella on various Python libraries and applications. The Pocoo Team is led by Georg Brandl and Armin Ronacher. http://www.pocoo.org/

## Install Flash

```
$ pip install flask
```

Write `app.py` to process 3 URL:

* `GET /`: index, return home page
* `GET /signin`: login page, show login form
* `POST /signin`: process login form, show login result

Flash use decorator to associate URL and function. So our code is like:

```python
# app.py

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
                <p><input name="username"></p>
                <p><input name="password" type="password"></p>
                <p><button type="submit">Sign In</button></p>
                </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username and password.</h3>'

if __name__ == '__main__':
    app.run()

```

[app.py](./scripts/app.py)

除了Flask，常见的Python Web框架还有：

* Django：全能型Web框架；
* web.py：一个小巧的Web框架；
* Bottle：和Flask类似的Web框架；
* Tornado：Facebook的开源异步Web框架。
