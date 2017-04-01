# [Base64 编码](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431954588961d6b6f51000ca4279a3415ce14ed9d709000)

作者：廖雪峰

Base64 是一种用 64 个字符表示任意二进制数据的方法。

## 原理

首先，准备一个包含 64 个字符的数组：

```python
['A', 'B', 'C', ..., 'a', 'b', 'c', ..., '0', '1', ..., '+', '/']
```

然后，对二进制进行处理，每 3 个字节一组，一共是 `3*8=24` 比特，划为 4 组，每组 6 比特：

![base64 diagram](http://www.liaoxuefeng.com/files/attachments/001399415038305edba53df7d784a7fa76c6b7f6526873b000)

这样就得到4个数字作为索引，查表得到相应字符，就是编码后的字符串。

Base64 会把 3 字节的二进制数据编码为 4 字节的文本数据，长度增加 33%。好处是编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不足 3 的倍数，Base64 用 `\x00` 字节在末尾补足后，再在编码的末尾加上 1 个或 2 个 `=` 号，表示补了多少字节，解码时会自动去掉。

## 应用

```python
import base64
base64.b64encode(b'binary\x00string')
base64.b64.decode(b'YmluYXJS==')
```

由于标准的 Base64 编码后可能出现字符 `+` 和 `/` ，在 URL 中不能直接作为参数，所以有一种 "url safe" 的 base64 编码，其实就是把字符 `+` 和 `/` 分别变成 `-` 和 `_`：

```python
base64.urlsafe_b64encode(b'i\xb7\x1d\xef\xff')
base64.urlsafe_b64decode(b'abcd--__')
```

Base64 是一种通过查表的编码方式，不能用于加密。