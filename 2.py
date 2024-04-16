# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/9  2:03
# 例子：待办事项列表
# import tkinter as tk
# from tkinter import messagebox
#
#
# def add_task():
#     task = task_entry.get()
#     if task:
#         tasks_listbox.insert(tk.END, task)
#         task_entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("警告", "请输入任务内容！")
#
#
# def remove_task():
#     selected_index = tasks_listbox.curselection()
#     if selected_index:
#         tasks_listbox.delete(selected_index)
#
#
# root = tk.Tk()
# root.title("待办事项列表")
#
# # 输入框和按钮
# task_entry = tk.Entry(root)
# task_entry.pack()
#
# add_button = tk.Button(root, text="添加任务", command=add_task)
# add_button.pack()
#
# remove_button = tk.Button(root, text="删除任务", command=remove_task)
# remove_button.pack()
#
# # 待办事项列表框
# tasks_listbox = tk.Listbox(root)
# tasks_listbox.pack()
#
# root.mainloop()

# ***********************************和上面分开******************************************************************
# import tkinter as tk
#
#
# def create_new_window():
#     # 创建一个新的Toplevel窗口
#     new_window = tk.Toplevel(root)
#     new_window.title("新窗口")
#
#     # 在新窗口中创建一个标签
#     label = tk.Label(new_window, text="好好学习")
#     label.pack()
#
#
# # 创建主窗口
# root = tk.Tk()
# root.title("主窗口")
#
# # 在主窗口中添加一些内容
# label = tk.Label(root, text="王者荣耀")
# label.pack()
#
# # 自动打开第一个新窗口
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
# create_new_window()
#
#
# # 进入主窗口的事件循环
# root.mainloop()
# ***********************************************************************************************************
# import tkinter as tk
# import random
# import time
# from tkinter import font
#
# # 定义浅粉色
# PINK = '#FFC0CB'
#
# # 存储已创建的窗口及其位置
# created_windows = []
#
#
# def create_new_window():
#     global created_windows
#     # 随机计算窗口的位置
#     x, y = get_random_position()
#
#     # 创建一个新的Toplevel窗口
#     new_window = tk.Toplevel(root)
#     new_window.configure(bg=PINK)
#     new_window.title("新窗口")
#     new_window.geometry("200x100")  # 设置窗口大小
#
#     # 创建标签并设置字体
#     font_size = 12
#     label_font = font.Font(family='TkDefaultFont', size=font_size)
#     label = tk.Label(new_window, text="新窗口", bg=PINK, font=label_font)
#     label.pack()
#
#     # 将新窗口及其位置添加到已创建的窗口列表中
#     created_windows.append((new_window, (x, y)))
#
#     # 打包窗口组件（这一步应该在创建所有组件之后执行一次）
#     new_window.update_idletasks()
#     new_window.lift()  # 确保窗口在顶层
#
#
# def get_random_position():
#     # 尝试获取一个不与其他窗口重叠的位置
#     while True:
#         x = random.randint(0, root.winfo_screenwidth() - 200)  # 减去窗口宽度
#         y = random.randint(0, root.winfo_screenheight() - 100)  # 减去窗口高度
#
#         # 检查这个位置是否已被占用
#         if not any(pos == (x, y) for window, pos in created_windows):
#             return x, y
#
#         # 创建主窗口
#
#
# root = tk.Tk()
# root.withdraw()  # 隐藏主窗口
#
# # 设置弹出窗口的总数和每个窗口之间的间隔
# total_windows = 100
# interval = 10 / total_windows  # 30秒内完成所有窗口的弹出
#
# # 开始创建窗口
# for _ in range(total_windows):
#     create_new_window()
#     time.sleep(interval)  # 暂停一段时间

# 进入主窗口的事件循环
# root.mainloop()


# 国旗
# import turtle
#
#
# def draw_rectangle(x, y, width, height):
#     """绘制矩形"""
#     turtle.goto(x, y)
#     turtle.pencolor('red')
#     turtle.fillcolor('red')
#     turtle.begin_fill()
#     for i in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#     turtle.end_fill()
#
#
# def draw_star(x, y, radius):
#     """绘制五角星"""
#     turtle.setpos(x, y)
#     pos1 = turtle.pos()
#     turtle.circle(-radius, 72)
#     pos2 = turtle.pos()
#     turtle.circle(-radius, 72)
#     pos3 = turtle.pos()
#     turtle.circle(-radius, 72)
#     pos4 = turtle.pos()
#     turtle.circle(-radius, 72)
#     pos5 = turtle.pos()
#     turtle.color('yellow', 'yellow')
#     turtle.begin_fill()
#     turtle.goto(pos3)
#     turtle.goto(pos1)
#     turtle.goto(pos4)
#     turtle.goto(pos2)
#     turtle.goto(pos5)
#     turtle.end_fill()
#
#
# def main():
#     """主程序"""
#     turtle.speed(12)
#     turtle.penup()
#     x, y = -270, -180
#     # 画国旗主体
#     width, height = 540, 360
#     draw_rectangle(x, y, width, height)
#     # 画大星星
#     pice = 22
#     center_x, center_y = x + 5 * pice, y + height - pice * 5
#     turtle.goto(center_x, center_y)
#     turtle.left(90)
#     turtle.forward(pice * 3)
#     turtle.right(90)
#     draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
#     x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
#     # 画小星星
#     for x_pos, y_pos in zip(x_poses, y_poses):
#         turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
#         turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
#         turtle.forward(pice)
#         turtle.right(90)
#         draw_star(turtle.xcor(), turtle.ycor(), pice)
#     # 隐藏海龟
#     turtle.ht()
#     # 显示绘图窗口
#     turtle.mainloop()
#
#
# if __name__ == '__main__':
#     main()


# *************************************************************************************
# 小猪佩奇

"""
绘制小猪佩奇
"""
from turtle import *


def nose(x,y):
    """画鼻子"""
    penup()
    # 将海龟移动到指定的坐标
    goto(x,y)
    pendown()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i <90:
            a = a + 0.08
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    """画头"""
    color((255, 155, 192), "pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0<= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3) #向左转3度
            fd(a) #向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x,y):
    """画耳朵"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x,y):
    """画眼睛"""
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x,y):
    """画脸颊"""
    color((255, 155, 192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x,y):
    """画嘴巴"""
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def setting():
    """设置参数"""
    pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    """主函数"""
    setting()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    done()


if __name__ == '__main__':
    main()
