# TCP/IP 简介

http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320037768360d53e4e935ca4a1f96eed1c896ad1217000

作者：廖雪峰

为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，为了实现互联网这个目标，互联网协议簇（Internet Protocol Suite）就是通用协议标准。

**IP协议负责把数据从一台计算机通过网络发送到另一台计算机**。数据被分割成一小块一小块，然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。**IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达**。

> IP 协议，只管送，不管送到。

IP 地址实际上是一个 32 位整数（称为IPv4），以字符串表示的 IP 地址如 `192.168.0.1` 实际上是把 32 位整数按 8 位分组后的数字表示，目的是便于阅读。

IPv6 地址实际上是一个 128 位整数，它是目前使用的 IPv4 的升级版，以字符串表示类似于`2001:0db8:85a3:0042:1000:8a2e:0370:7334`。

> IPv6 长度是 IPv4 的 4 倍。

**TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达**。TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。

许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。

一个IP包除了包含要传输的数据外，还包含**源IP地址**和**目标IP地址**，**源端口**和**目标端口**。

端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。一个IP包来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。
