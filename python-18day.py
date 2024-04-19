# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/19
# coding=utf-8

# 参考
import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', '我用Python') \
            if flag else ('blue', '人生苦短')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('300x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象
    label = tkinter.Label(top, text='为什么选择Python？', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()

# *****************************************************************************
# 参数Label示例

from tkinter import *

root = Tk()
Label(root, text='标签',  # 文本内容
      bg='#d3fbfb',  # 背景颜色
      fg='red',  # 字体颜色
      font=('微软雅黑', 12),  # 字体和字体大小
      width=15,  # 宽度
      height=2,  # 高度
      relief=RAISED).pack()  # 3D浮雕样式 参数：FLAT(平的)、RAISED(凸起的)、SUNKEN(凹陷的)、GROOVE(沟槽状边缘)和 RIDGE(脊状边缘)
Label(root, text='绿', fg='green', font=('微软雅黑', 12), relief=RAISED).pack(side=BOTTOM)
Label(root, text='蓝', fg='blue', font=('微软雅黑', 12), relief=RAISED).pack(fill=BOTH)

Label(root, text='红', fg='red', font=('微软雅黑', 12), relief=RAISED).pack(side=RIGHT)
Label(root, text='黄', fg='yellow', font=('微软雅黑', 12), relief=RAISED).pack(fill=Y)
root.title('测试')
root.geometry('320x240')
root.mainloop()

# *****************************************************************************
# message框示例

from tkinter import *

root = Tk()
msg1 = Message(root, text='''人生最难的是遇见，更难的其实是重逢。有时候不喜欢你的人对你不好，其实就是对你好。''',
               relief=GROOVE)
msg1.place(relx=0.2, y=80, relheight=0.4, width=200)

root.title('测试')
root.geometry('320x240')
root.mainloop()

# ******************************************************************************************

# 时钟
import tkinter
import time


def gettime():
    timestr = time.strftime("%H:%M:%S")
    lb.configure(text=timestr)
    root.after(1000, gettime)


root = tkinter.Tk()
root.title('时钟')
lb = tkinter.Label(root, fg='red', font=("黑体", 90))
lb.pack()
gettime()
root.mainloop()

# ******************************************************************************************

from tkinter import *
# import time
import datetime


def gettime():
    s = str(datetime.datetime.now()) + '\n'
    txt.insert(END, s)
    root.after(1000, gettime)


root = Tk()
root.title('时钟')
root.geometry('320x240')
txt = Text(root)
txt.pack()
gettime()
root.mainloop()

# ******************************************************************************************
# 使用tkinker库实现一个简单的加法器
from tkinter import *
import tkinter
import tkinter.messagebox


def run():
    a = float(inp1.get())
    b = float(inp2.get())
    s = '%0.1f+%0.1f=%0.1f\n' % (a, b, a + b)
    txt.insert(END, s)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入
    inp2.delete(0, END)  # 清空输入


def quit():
    if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
        root.quit()


root = Tk()
root.geometry('460x240')
root.title('简单加法器')

lb1 = Label(root, text='请输入两个数，进行加法计算')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
lb2 = Label(root, text='+')
lb2.place(relx=0.45, rely=0.2, relwidth=0.1, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)

# 方法-直接调用 run1()
btn1 = Button(root, text='等于', command=run)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.2)
btn2 = Button(root, text='退出', command=quit)
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.2)

txt = Text(root)
txt.place(rely=0.6, relheight=0.4)  # 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框

root.mainloop()
