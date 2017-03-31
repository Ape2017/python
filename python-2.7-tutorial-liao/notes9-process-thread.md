# [进程和线程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319272686365ec7ceaeca33428c914edf8f70cca383000)

作者：廖雪峰

操作系统轮流让多个任务交替执行，实现多任务。

一个任务就是一个进程（Process）。进程内的“子任务”叫做线程（Thread）。

多任务的实现有3种方式：

* 多进程模式
* 多线程模式
* 多进程 + 多线程模式

如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。

多进程和多线程的程序涉及到同步、数据共享的问题，编写起来复杂。

## 多进程（multiprocessing）

Unix/Linux 操作系统提供了 `fork()` 系统调用，调用一次，返回两次。操作系统自动把当前进程（父进程）复制了一份（子进程），分别在父进程和子进程内返回。

子进程永远返回 `0`，而父进程返回子进程的 ID。子进程通过调用 `getppid()` 可以拿到父进程的 ID。

Python 的 os 模块封装了创建的系统调用，包括 `fork`。查看[代码](../scripts/multitask/do_fork.py)。

### multiprocessing

`multiprocessing` 模块是跨平台的多进程模块，可以解决 Windows 没有 `fork` 调用的问题。`multiprocessing` 提供了一个 `Process` 类来代表一个进程对象，[这个代码例子](../scripts/multitask/multi_processing.py)演示了启动一个子进程并等待其结束。

### Pool

如果要启动大量的子进程，可以使用进程池的方式批量创建子进程。查看[代码]()。

### 进程间通信

