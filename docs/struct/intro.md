# struct 简介

来源：[廖雪峰的Python教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000)

`struct` 模块可以解决 `bytes` 和其他二进制数据类型的转换。

`struct` 的 `pack` 函数把任意数据类型变成 `bytes`:

```python
import struct
struct.pack('>I', 10240099)
# ===> b'\x00\x9c@c'
```

`pack` 的第一个参数是处理指令，`>I` 的意思是：

`>` 表示字节顺序是 big-endian, 也就是网络序，`I` 表示4字节无符号整数。

后面的参数个数要和处理指令一致。

`unpack` 把 `bytes` 变成相应的数据类型：

```python
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
# ===> (4042322160, 32896)
```

根据 `>IH` 的说明，后面的 `bytes` 依次变为 `I`: 4字节无符号整数和 `H`: 2字节无符号整数。

尽管 Python 不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用 `struct` 就方便多了。