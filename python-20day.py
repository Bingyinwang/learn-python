# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/23  13:15
# 多线程
# 以下内容来源于《看漫画学Python》这本书，前面十几天好多内容参考过本书内容，写的挺好。
#
# 1 线程相关知识
# 1.1 进程
# 一个进程就是一个正在执行的程序，每一个进程都有自己独立的一块内存空间，一组系统资源。在进程概念中，每一个进程的内部数据和状态都是完全独立的
#
#  在Windows操作系统中，一个进程就是一个exe或者dll程序，它们相互独立，相互也可以通信。
#
# 1.2 线程
# 在一个进程中可以包含多个线程，多个线程共享一块内存空间和一组系统资源。所以，系统在各个线程之间切换时，开销要比进程小得多，线程被称为轻量级进程。
#
# 1.3 主线程
#  Python程序至少有一个线程，这就是主线程，程序在启动后由Python解释器负责创建主线程，在程序结束后由Python解释器负责停止主线程。
#
#  在多线程中，主线程负责其他线程的启动，挂起，停止等操作。其他线程被称为子线程。
#
# 2 线程模块-----------threading
# Python官方提供的threading模块可以进行多线程编程。threading模块提供了多线程编程的高级API，使用起来比较简单。
#
# 在threading模块中提供了线程类Thread，还提供了很多线程相关的函数，常用如下：
#
# active_count():返回当前处于活动状态的线程个数
#
# current_thread():返回当前的Thread对象
#
# main_thread():返回主线程对象。
#
# 主线程是Python解释器启动的线程。示例代码如下：

import threading  # 导入threading模块

t = threading.current_thread()  # 获取当前线程对象
print(t.name)  # 输出当前线程的名字
print(threading.active_count())  # 输出当前活动线程的个数

t = threading.main_thread()
print(t.name)  # 输出主线程的名字

# 3 创建子线程
# 创建一个可执行的子线程需要：线程对象和线程体
#
# 线程对象：线程对象是threading模块的线程类Thread或Thread子类所创建的对象。
#
# 线程体：线程体是子线程要执行的代码，这些代码会被封装到一个函数中。子线程在启动后会执行线程体。
#
# 实现线程体主要有以下两种方式：
#
# 1，自定义函数实现线程体
#
# 2，自定义线程类实现线程体
#
# 3.1 自定义函数实现线程体
# 创建线程Thread对象的构造方法如下：
#
# Thread（target=None， name=None， args=（））
#
# target参数指向线程体函数，可以自定义该线程体的函数；通过name参数可以设置线程名，若省略这个参数，则系统会为其分配一个名称；args是为线程体函数提供的参数，是一个元组类型。
#
# 示例代码如下：

import threading
import time


def thread_body():  # 定义线程体函数
    t = threading.current_thread()  # 获取当前线程对象
    for n in range(5):  # 执行5次
        print('第{0}次执行线程{1}'.format(n, t.name))
        time.sleep(2)  # 当前线程休眠两秒
    print('线程{0}执行完毕'.format(t.name))


t1 = threading.Thread(target=thread_body)  # 创建线程对象t1
t2 = threading.Thread(target=thread_body, name='MyThready')  # 创建线程对象t2
t1.start()  # 启动线程t1
t2.start()  # 启动线程t2

# 3.2 自定义线程类实现线程体
# 创建一个Thread子类并重写run（）方法，run（）方法就是线程体函数
#
# 示例代码如下：

import threading
import time


class SmallThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    def run(self):  # 重写run()方法
        t = threading.current_thread()  # 获取当前线程对象
        for n in range(5):  # 执行5次
            print('第{0}次执行线程{1}'.format(n, t.name))
            time.sleep(2)  # 当前线程休眠两秒
        print('线程{0}执行完毕'.format(t.name))


t1 = SmallThread()  # 创建线程对象t1
t2 = SmallThread(name='MyThready')  # 创建线程对象t2
t1.start()  # 启动线程t1
t2.start()  # 启动线程t2


# 4 线程管理
# 线程管理包括： 线程创建，线程启动，线程休眠，等待线程结束，和线程停止。
#
# 前三个内容前面已涉及，以下主要是等待线程结束，线程停止的内容。
#
# 4.1 等待线程结束
# 一个线程（假设是主线程）需要等待另一个线程（假设是t1子线程）执行结束后才能继续执行。
# 示例代码如下：

import threading
import time

value = []  # 定义一个共享变量，多个线程可以访问该变量


def thread_body():
    print('t1线程开始...')
    for n in range(2):
        print('t1子线程执行...')
        value.append(n)
        time.sleep(2)
    print('t1子线程结束...')


print('主线程开始执行...')
t1 = threading.Thread(target=thread_body)  # 创建线程对象t1
t1.start()  # 启动线程t1
#t1.join()  # 等待线程t1结束
print('value = {0}'.format(value))
print('主线程继续执行...')

# 4.2 线程停止
# 在线程结束时，线程就停止了，业务复杂时，会在线程体执行一个“死循环”。通过判断停止变量实现线程体是否持续执行“死循环”，“死循环”结束则线程体结束，线程也就结束了。
#
# 一般情况下，死循环会执行线程任务，然后休眠，再执行，再休眠，直到循环结束。
# 示例代码如下：
import threading
import time

# 线程停止变量
isrunning = True


def workthread_body():  # 定义工作线程体函数
    while isrunning:
        print('工作线程正在执行...')
        time.sleep(5)
    print('工作线程结束')


def controlthread_body():  # 定义控制线程体函数
    global isrunning
    while isrunning:
        command = input('请输入停止指令：')
        if command == 'exit':
            isrunning = False
            print('控制线程结束')


workthread = threading.Thread(target=workthread_body)  # 创建工作线程对象
workthread.start()  # 启动工作线程
controlthread = threading.Thread(target=controlthread_body)  # 创建控制线程对象
controlthread.start()  # 启动控制线程


# 5 爬虫下载图片示例：
import threading
import time
import urllib.request

# 线程停止变量
isrunning = True


def workthread_body():  # 定义工作线程体函数
    while isrunning:
        print('工作线程正在执行...')
        download()  # 调用下载图片的函数
        time.sleep(5)
    print('工作线程结束')


def controlthread_body():  # 定义控制线程体函数
    global isrunning
    while isrunning:
        command = input('请输入停止指令：')
        if command == 'exit':
            isrunning = False
            print('控制线程结束')


def download():    # 定义下载图片的函数
    url = '此处替换图片链接'   # 此处替换图片链接
    req = urllib.request.Request(url)  # 创建请求对象
    with urllib.request.urlopen(req) as response:   # 发起请求
        data = response.read()
        f_name = 'download.png'
        with open(f_name, 'wb') as f:  # 打开文件
            f.write(data)
            print('图片下载成功')


workthread = threading.Thread(target=workthread_body)  # 创建工作线程对象
workthread.start()  # 启动工作线程
controlthread = threading.Thread(target=controlthread_body)  # 创建控制线程对象
controlthread.start()  # 启动控制线程
