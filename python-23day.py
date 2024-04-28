# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/28
# 子窗体
from tkinter import *


def newwindow():
    winNew = Toplevel(root)
    winNew.geometry('320x240')
    winNew.title('子窗口')
    zlab = Label(winNew, text='这是一个子窗口')
    zlab.place(relx=0.2, rely=0.2)
    close = Button(winNew, text='关闭', command=winNew.destroy)
    close.place(relx=0.7, rely=0.5)


root = Tk()
root.title('主窗口')
root.geometry('320x240')

lab = Label(root, text='这是一个主窗口', font=('黑体', 20, 'bold'))
lab.place(relx=0.2, rely=0.2)

mainmenu = Menu(root)
menuFile = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label='菜单', menu=menuFile)
menuFile.add_command(label='新窗体', command=newwindow)
menuFile.add_separator()
menuFile.add_command(label='退出', command=root.destroy)

root.config(menu=mainmenu)
root.mainloop()

# 消息对话框
from tkinter import *
import tkinter.messagebox


def xx():
    answer = tkinter.messagebox.askokcancel('请选择', '请选择确定或取消')
    if answer:
        lab.config(text='已确认', fg='green')
    else:
        lab.config(text='已取消', fg='red')


root = Tk()
root.title('消息对话框')
root.geometry('300x100')
lab = Label(root, text='')
lab.pack()
btn = Button(root, text='弹出对话框', fg='blue', command=xx)
btn.pack()
root.mainloop()

# 输入对话框
from tkinter.simpledialog import *
from tkinter import *


def sr():
    q = askstring('请输入', '请输入一段文字')
    lab.config(text=q)


root = Tk()
root.title('输入对话框')
root.geometry('320x240')
lab = Label(root, text='')
lab.pack()
btn = Button(root, text='输入', fg='blue', command=sr)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()

# 文件选择对话框
from tkinter import *
import tkinter.filedialog


def wjxz():
    filename = tkinter.filedialog.askopenfilename()  # 返回文件路径
    print(filename)

    if filename != '':
        # 打开文件并读取内容
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                lab.config(text='你选的文件是：' + filename + '\n文件内容：\n' + content)
        except Exception as e:
            lab.config(text='打开文件时出错：' + str(e))
    else:
        lab.config(text='未选择文件')


root = Tk()
root.title('文件选择对话框')
root.geometry('700x800')  # 增加了窗口的高度以容纳更多文本

lab = Label(root, text='')
lab.pack(pady=20)  # 增加垂直内边距，使标签与按钮之间的空间更大

btn = Button(root, text='选择文件', fg='blue', command=wjxz)
btn.place(relx=0.01, rely=0.01)

root.mainloop()

# 颜色选择对话框
from tkinter import *
import tkinter.colorchooser


def ys():
    color = tkinter.colorchooser.askcolor()
    colorstr = str(color)
    print('打印字符串%s 切掉后=%s' % (colorstr, colorstr[-9:-2]))
    lab.config(text=colorstr[-9:-2], bg=colorstr[-9:-2])


root = Tk()
root.title('颜色选择对话框')
root.geometry('300x200')
lab = Label(root, text='请关注颜色的变化', bg='white')
lab.pack()
btn = Button(root, text='选择颜色', fg='blue', command=ys)
btn.place(relx=0.01, rely=0.01)
root.mainloop()
