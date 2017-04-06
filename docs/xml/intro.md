[XML](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432002075057b594f70ecb58445da6ef6071aca880af000)

作者：廖雪峰

## DOM vs. SAX

操作 XML 有两种方法：DOM 和 SAX。DOM 会把整个 XML 读入内存，解析为树，占用内存大，解析慢，优点是可以任意遍历树的节点。SAX 是流模式，边读边解析，占用内存小，解析快，缺点是需要自己处理事件。

优先考虑 SAX，因为 DOM 实在太占内存。

在 Python 中使用 SAX 解析 XML 关心的事件是 `start_element`, `end_element` 和 `char_data`。查看[代码](../../scripts/xml/intro.py)。