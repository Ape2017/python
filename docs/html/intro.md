# [HTMLParser](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320023122880232500da9dc4a4486ad00426f081c15000)

作者：廖雪峰

HTML 本质上是 XML 的子集，但是 HTML 的语法没有 XML 那么严格，所以不能用标准的 DOM 或 SAX 来解析 HTML。

好在 Python 提供了 `HTMLParser` 来非常方便地解析 HTML，只需简单[几行代码](../../scripts/html/parser.py)。

