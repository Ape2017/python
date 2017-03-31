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

如果要启动大量的子进程，可以使用进程池的方式批量创建子进程。查看[代码](../scripts/multitask/use_pool.py)。

### 进程间通信

Python 的 `multiprocessing` 模块提供了 `Queue`, `Pipes` 等多种方式交换数据。查看[代码](../scripts/multitask/use_queue.py)。

## 多线程

Python 线程是真正的 Posix Thread ，而不是模拟出来的线程。

Python 标准库提供了两个模块：`_thread`（低级模块） 和 `threading`（高级模块）。

启动一个线程就是把一个函数传入并创建 `Thread` 实例，然后调用 `start()` 开始执行。查看代码。

### Lock

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

可以用锁机制来解决问题。查看[代码](../scripts/multitask/use_lock.py)。

### 多核CPU

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个 `GIL` 锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

## ThreadLocal

