# [IO 编程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917590955542f9ac5f5c1479faf787ff2b028ab47000)

作者：廖雪峰

IO 编程中，Stream(流)是个很重要的概念。

根据是否等待IO执行的结果，可以分成同步 IO 和异步 IO 。

## 文件读写

### 读文件

要以读的模式打开一个文件对象，使用 Python 内置的 `open()` 函数，传入文件名和标示符：

```python
f = open('/path/to/file.txt', 'r')
```

如果文件打开成功，使用 `read()` 一次性读取全部文件内容。最后调用 `close()` 方法关闭文件。查看[代码](../scripts/io/read.py)。

每次都这么写太繁琐，Python 引入了 `with` 语句来自动调用 `close()` 方法：

```python
with open('/path/to/file', 'r') as f:
    print(f.read())
```

查看[代码](../scripts/io/do_with.py)。

除了 `read` 一次性读取全部文本内容，还有如下函数可以读取：

* `read(size)`, 每次最多读取 size 个字节的内容
* `readline()`, 每次读取一行的内容
* `readlines()`, 一次读取所有的内容，并按行返回 `list`

```python
for line in f.readlines():
    print(line.strip()) # remove rear `\n`
```

### file-like Object

file-like Object 只需要实现 `read()` 方法就行。

`StringIO` 就是在内存中创建的 file-like Object，常用做临时缓冲。

### 二进制文件

使用 `rb` 模式打开。

### 字符编码

需要给 `open()` 函数传入 `encoding` 参数：

```python
f = open('/path/to/file', 'r', encoding='gbk')
f.read()
```

如果夹杂非法编码的字符，会导致 `UnicodeDecodeError`，使用 `errors` 参数指定如何处理错误。

```python
f = open('/path/to/file', 'r', encoding='gbk', errors='ignore')
```

### 写文件

使用 `w` 或 `wb` 模式。

使用 `with` 语句操作文件IO是个好习惯。

## StringIO 和 BytesIO

StringIO 就是在内存中读写 str ，查看[代码](../scripts/io/stringio.py)。

BytesIO 在内存中操作二进制数据，查看[代码](../scripts/io/bytesio.py)。

## 操作文件和目录

Python 内置的 `os` 模块可以直接调用操作系统提供的基本功能：

```python
import os
os.name # 操作系统类型
os.uname() # 详细的系统信息
os.environ # 环境变量
os.environ.get('PATH') # 获取某个环境变量
os.environ.get('x', 'default') # return `default`
```

### 操作文件和目录

```python
os.path.abspath('.')                              # 当前目录的绝对路径
os.path.join('/Users/liuzhuan', 'testdir')        # 拼接路径
os.path.split('/Users/liuzhuan/testdir/file.txt') # 拆分路径
os.path.splitext('/path/to/file.txt')             # 得到文件扩展名
os.path.isdir('/path')                            # 判断是否是文件夹
os.path.isfile('/path')                           # 判断是否为文件

os.mkdir('/Users/liuzhuan/testdir')               # 创建目录
os.rmdir('/Users/liuzhuan/testdir')               # 删除目录
os.listdir('.')                                   # 列出当前文件夹的内容
os.rename('test.txt', 'test.py')                  # 重命名
os.remove('test.py')                              # 删掉文件
```

`shutil` 模块提供了 `copyfile()` 函数。可以看作是 `os` 模块的补充。

```python
# 列出所有的文件夹
[x for x in os.listdir('.') if os.path.isdir(x)]

# 列出所有的 .py 文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
```

查看[代码](../scripts/io/my_grep.py)

## 序列化

把变量从内存中变成可存储或传输的过程称之为序列化，在 Python 中叫 `pickling` ；反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即 `unpickling`。

Python 提供了 `pickle` 模块来实现序列化。Pickle 只能用于 Python ，并且可能不同版本的 Python 都不兼容，因此只能保存那些不重要的数据。查看[代码](../scripts/io/do_pickle.py)

> 哪些数据是不重要的...

### JSON

Python 内置的 `json` 模块提供了非常完善的 Python 对象到 JSON 对象的转换。

代码实例如下：

* [json](../scripts/io/use_json.py)
* [json 高级用法](../scripts/io/use_json_pro.py)