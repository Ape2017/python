# 正则表达式

Book: Introuducing Python

Author: Bill Lubanovic

## Extract match with match()

```python
import re

source = "Young Frankenstein"
m = re.match('Frank', source)
if m:
    print(m.group())
# m is None
```

`match()` works only if the pattern is at the beginning of the source. But `search()` works if the pattern is anywhere:

```python
m = re.search('Frank', source)
if m:
    print(m.group())
```

## First match with search()

```python
m = re.search('Frank', source)
if m:
    print(m.group())
```

## Find matches with findall()

```python
m = re.findall('n', source)
m
```

## Split at matches with split()

```python
m = re.split('n', source)
m
```

## Replace at matches with sub()

```python
m = re.sub('n', '?', source)
m
```

[Source Code](../../scripts/re/intro.py)
