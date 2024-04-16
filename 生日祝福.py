# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/14  17:18
import wx

# 定义粉色
PINK_COLOUR = (255, 192, 203)
import turtle as t
import math as m
import random as r


class Greeting():
    def run(self):
        t.Turtle().screen.delay(0)  # 【画的更快 可以注释掉】

        def drawX(a, i):
            angle = m.radians(i)
            return a * m.cos(angle)

        def drawY(b, i):
            angle = m.radians(i)
            return b * m.sin(angle)

        # 设置背景颜色，窗口位置以及大小  可以放到__init__里面
        t.bgcolor("#d3dae8")
        t.setup(700, 800)
        t.penup()
        t.goto(150, 0)
        t.pendown()

        def layer_0():  # 第一层蛋糕

            # 蛋糕第一层白色糕身
            t.pencolor("white")
            t.fillcolor("#fef5f7")
            t.begin_fill()
            for i in range(180):
                x = drawX(150, i)
                y = drawY(-60, i) - 120
                t.goto(x, y)
            t.goto(x, y + 120)

            for i in range(180):
                x = drawX(-150, i)
                y = drawY(60, i)
                t.goto(x, y)
            t.end_fill()

            # 蛋糕第一层的顶部奶油（粉色）
            t.pencolor("#f2d7dd")
            t.begin_fill()
            for i in range(360):
                x = drawX(150, i)
                y = drawY(60, i)
                t.goto(x, y)
            t.fillcolor("#f2d7dd")  # 奶油色
            t.end_fill()

            # 粉色奶油下溢（类似于瀑布蛋糕）
            t.begin_fill()
            t.pensize(4)
            t.pencolor("#f2d7dd")
            for i in range(1800):
                x = drawX(150, 0.1 * i)
                y = drawY(-20, i) - 85
                t.goto(x, y)
            t.goto(-150, 0)
            t.pensize(1)
            for i in range(0, 180):
                x = drawX(-150, i)
                y = drawY(-60, i)
                t.goto(x, y)
            t.fillcolor("#f2d7dd")
            t.end_fill()

        def layer_1():  # 第二层蛋糕

            # 第二层蛋糕打底rose_pink色
            t.pencolor("#ffa79d")  # rose_pink
            t.begin_fill()
            t.pu()
            t.goto(120, 0)
            t.pd()
            t.begin_fill()
            for i in range(360):
                x = drawX(120, i)
                y = drawY(48, i)
                t.goto(x, y)
            t.fillcolor("#ffa79d")
            t.end_fill()

            t.begin_fill()
            t.fillcolor("#ffa79d")

            for i in range(180):
                x = drawX(120, i)
                y = drawY(48, i) + 70
                t.goto(x, y)
            t.goto(-120, 0)

            t.end_fill()
            t.pu()
            t.goto(120, 70)

            # 浇头蓝色蛋糕
            t.pd()
            t.begin_fill()
            t.pencolor('#cbd9f9')  # "#cbd9f9" blue color
            for i in range(360):
                x = drawX(120, i)
                y = drawY(48, i) + 70
                t.goto(x, y)

            t.fillcolor("#cbd9f9")
            # t.end_fill()  # 可加可不加，加了第二层蛋糕顶端就是蓝色

            # 蓝色中心为顶向下浇浇头
            t.begin_fill()
            t.pensize(8)
            t.goto(120, 70)
            for s in range(0, 12):  # 相当于涂抹糕身的特效
                for i in range(180):
                    x = drawX(120, i)
                    y = drawY(-48, i) + 70 - 5 * s
                    t.goto(x, y)
                for i in range(180):
                    x = drawX(-120, i)
                    y = drawY(-48, i) + 70 - 5.1 * s
                    t.goto(x, y)

            # 蓝色蛋糕的顶面白色涂层
            t.pu()
            t.goto(120, 70)
            t.pd()
            t.pencolor("#fff0f3")
            t.begin_fill()
            for i in range(360):
                x = drawX(120, i)
                y = drawY(48, i) + 70
                t.goto(x, y)
            t.fillcolor("#fff0f3")
            t.end_fill()

            # 蓝色蛋糕的顶面白色涂层里的涂层
            t.pu()
            t.goto(110, 70)
            t.pd()
            t.pencolor("#fff9fb")
            t.begin_fill()
            for i in range(360):
                x = drawX(110, i)
                y = drawY(44, i) + 70
                t.goto(x, y)
            t.fillcolor("#fff9fb")
            t.end_fill()

            # 第二层蛋糕圆弧部分（类似于瀑布蛋糕）
            t.pu()
            t.goto(120, 70)
            t.pd()
            t.begin_fill()
            t.pensize(4)
            t.pencolor("#fff0f3")
            for i in range(1800):
                x = drawX(120, 0.1 * i)
                y = drawY(-18, i) + 10
                t.goto(x, y)
            t.goto(-120, 70)
            t.pensize(1)
            for i in range(180, 360):
                x = drawX(120, i)
                y = drawY(48, i) + 70
                t.goto(x, y)
            t.fillcolor("#fff0f3")
            t.end_fill()

        def layer_2():  # 第三层棕色蛋糕部分

            # 棕色蛋糕糕身
            t.pencolor("#6f3732")
            t.pu()
            t.goto(80, 70)
            t.pd()
            t.begin_fill()
            t.pencolor("#6f3732")
            t.goto(80, 120)
            for i in range(180):
                x = drawX(80, i)
                y = drawY(32, i) + 120
                t.goto(x, y)
            t.goto(-80, 70)
            for i in range(180, 360):
                x = drawX(80, i)
                y = drawY(32, i) + 70
                t.goto(x, y)
            t.fillcolor("#6f3732")
            t.end_fill()

            # 棕色蛋糕的表面涂层
            t.pu()
            t.goto(80, 120)
            t.pd()
            t.pencolor("#ffaaa0")
            t.begin_fill()
            for i in range(360):
                x = drawX(80, i)
                y = drawY(32, i) + 120
                t.goto(x, y)
            t.fillcolor("#ffaaa0")
            t.end_fill()

            # 涂层内圈
            t.pu()
            t.goto(70, 120)
            t.pd()
            t.pencolor("#ffc3be")
            t.begin_fill()
            for i in range(360):
                x = drawX(70, i)
                y = drawY(28, i) + 120
                t.goto(x, y)
            t.fillcolor("#ffc3be")
            t.end_fill()

            # 第二层涂层圆弧部分（类似于瀑布蛋糕）
            t.pu()
            t.goto(80, 120)
            t.pd()
            t.begin_fill()
            t.pensize(3)
            t.pencolor("#ffaaa0")
            for i in range(1800):
                x = drawX(80, 0.1 * i)
                y = drawY(-12, i) + 80
                t.goto(x, y)
            t.goto(-80, 120)
            t.pensize(1)
            for i in range(180, 360):
                x = drawX(80, i)
                y = drawY(32, i) + 120
                t.goto(x, y)
            t.fillcolor("#ffaaa0")
            t.end_fill()

        def candle_part():  # 蜡烛
            t.pu()
            t.goto(0, 120)
            t.pd()
            t.pencolor("#b1c9e9")
            t.begin_fill()
            for i in range(360):
                x = drawX(4, i)
                y = drawY(1, i) + 130
                t.goto(x, y)
            t.goto(4, 180)
            for i in range(540):
                x = drawX(4, i)
                y = drawY(1, i) + 180
                t.goto(x, y)
            t.goto(-4, 130)
            t.fillcolor("#b1c9e9")
            t.end_fill()
            t.pencolor("white")
            t.pensize(2)
            for i in range(1, 6):
                t.goto(4, 130 + 10 * i)
                t.pu()
                t.goto(-4, 130 + 10 * i)
                t.pd()
            t.pu()
            t.goto(0, 180)
            t.pd()
            t.goto(0, 190)
            t.pensize(1)
            t.pu()
            t.goto(4, 200)
            t.pd()

            # 火焰部分
            t.pencolor("#F160AD")
            t.begin_fill()
            for i in range(360):
                ii = r.randint(0, 1)  # 模拟火焰大小随机形状
                if ii == 0:
                    x = drawX(4, i) + r.random()
                else:
                    x = drawX(4, i) - r.random()
                y = drawY(10, i) + 200
                t.goto(x, y)
            t.fillcolor("#F160AD")
            t.end_fill()

        # 随机星星点点
        def writing():
            color = ["#e28cb9", "#805a8c", "#eaa989", "#6e90b7", "#b8b68f", "#e174b5", "#cf737c", "#7c8782"]

            # 棕色蛋糕部分
            for i in range(24):  # 个人私设的小彩蛋，Ta的生日多大就有多少个小星星，你们开心就好
                t.pu()
                x = r.randint(-80, 80)
                y = r.randint(60, 90)
                t.goto(x, y)
                t.pd()
                t.dot(r.randint(2, 5), color[r.randint(0, 7)])

            # 背景板的星星点点（可加可不加,我个人不喜欢）
            for i in range(50):
                t.pu()
                x = r.randint(-500, 500)
                y = r.randint(150, 300)
                t.goto(x, y)
                t.pd()
                t.dot(r.randint(3, 5), color[r.randint(0, 7)])

            t.seth(90)
            t.pu()
            t.goto(0, 0)
            t.fd(210)
            t.left(90)
            t.fd(200)
            t.pd()

            # 祝福文字
            t.pencolor('white')
            t.write("Happy Birthday")  # 可以自己导入喜欢的字体
            t.done()

        layer_0()
        layer_1()
        layer_2()
        candle_part()
        writing()
        t.done()


# if __name__ == '__main__':
# happy_birthday = Greeting()
# happy_birthday.run()


class IIWby(wx.Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, title='哇哦！', size=(250, 300))
        self.CentreOnScreen()
        # 添加窗口控件
        panel = wx.Panel(self)  # 创建面板对象
        panel.SetBackgroundColour(PINK_COLOUR)  # 设置面板的背景颜色为粉色

        self.tc1 = wx.TextCtrl(panel)
        self.tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        userid = wx.StaticText(panel, label='姓名ID：')
        password = wx.StaticText(panel, label='密码：')
        b = wx.Button(panel, label='查看')
        #
        b.Bind(wx.EVT_BUTTON, self.button, b)  # 绑定事件

        self.statictext = wx.StaticText(panel, label='张总，请登录后查看')  # 创建静态文本

        # 创建垂直方向盒子布局管理器对象iivbox
        iivbox = wx.BoxSizer(wx.VERTICAL)

        iivbox.Add(userid, 0, wx.EXPAND | wx.LEFT, 10)
        iivbox.Add(self.tc1, 0, wx.EXPAND | wx.ALL, 10)
        iivbox.Add(password, 0, wx.EXPAND | wx.LEFT, 10)
        iivbox.Add(self.tc2, 0, wx.EXPAND | wx.ALL, 10)
        iivbox.Add(self.statictext, 0, wx.CENTER | wx.FIXED_MINSIZE | wx.TOP, 10)
        #        iivbox.Add(panel, 1, wx.EXPAND | wx.ALL, 10)

        iivbox.Add(b, 1, wx.CENTER | wx.ALL, 20)

        # 设置面板的布局管理器为iivbox
        panel.SetSizer(iivbox)

    #        self.Fit()

    def button(self, event):
        tc1 = self.tc1.GetValue()
        tc2 = self.tc2.GetValue()
        print(f'姓名ID：{tc1}, 密码：{tc2}')
        self.EndModal(wx.ID_OK)
        if tc1 == 'zhangjie' and tc2 == '20240414':
            happy_birthday = Greeting()
            happy_birthday.run()


class IWby(wx.Dialog):
    def __init__(self):
        super().__init__(None, title='祝福语', size=(400, 350))
        self.CentreOnScreen()
        # 添加窗口控件
        panel = wx.Panel(parent=self)  # 创建面板对象
        panel.SetBackgroundColour(PINK_COLOUR)  # 设置面板的背景颜色为粉色
        self.statictext = wx.StaticText(parent=panel, label='祝张总前程似锦！愿你的未来更加灿烂辉煌！')  # 创建静态文本

        # 创建垂直方向盒子布局管理器对象ivbox
        ivbox = wx.BoxSizer(wx.VERTICAL)
        ivbox.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
        # 设置面板的布局管理器为ivbox
        self.SetSizer(ivbox)
        self.Fit()


class Wby(wx.Frame):  # 自定义窗口父类Wby
    def __init__(self):
        super().__init__(None, title='生日祝福--->张杰', size=(300, 220))
        self.CentreOnScreen()
        # 添加窗口控件
        panel = wx.Panel(parent=self)  # 创建面板对象
        panel.SetBackgroundColour(PINK_COLOUR)  # 设置面板的背景颜色为粉色
        self.statictext = wx.StaticText(parent=panel,
                                        label='                     张总，生日快乐！           \n      在这个特殊的日子里，愿你的每个愿望都能如期而至，每个梦想都能触手可及。愿你的每一天都充满阳光和欢笑，每一步都留下美好的回忆。')  # 创建静态文本
        b1 = wx.Button(parent=panel, id=10, label='快点我！')  # 创建按钮对象
        b2 = wx.Button(parent=panel, id=11, label='蛋糕！')  # 创建按钮对象
        b3 = wx.Button(parent=panel, id=12, label='Bye！')  # 创建按钮对象

        # 创建水平方向盒子布局管理器对象hbox
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # 添加b1按钮到hbox
        hbox.Add(b1, proportion=1, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        # 添加b2按钮到hbox
        hbox.Add(b2, proportion=1, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        # 添加b3按钮到hbox
        hbox.Add(b3, proportion=1, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # 创建垂直方向盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加静态文本到vbox
        vbox.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE | wx.TOP, border=10)
        # 添加hbox到vbox
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)
        # 设置面板的布局管理器为vbox
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.next, id=10)  # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.next, id=11)  # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.next, id=12)  # 绑定事件

    def next(self, event):  # 事件处理函数
        event_id = event.GetId()  # 获取事件ID
        print(event_id)
        if event_id == 10:  # 判断事件ID
            iwby = IWby()
            iwby.ShowModal()
            iwby.Destroy()
        elif event_id == 11:
            iiwby = IIWby()
            iiwby.ShowModal()
            iiwby.Destroy()
        else:
            self.Close()  # 关闭窗口


#        event.Skip()  # 调用默认的事件处理函数
app = wx.App()  # 创建应用程序对象
kpl = Wby()  # 创建窗口对象
kpl.Show()  # 显示窗口
app.MainLoop()  # 进入主事件循环



