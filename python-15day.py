# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/14
# 复习第十二天：图形用户界面wxPython + 送朋友的生日祝福
# import wx  # 导入wxPython模块
#
# app = wx.App()  # 创建应用程序对象
# wby = wx.Frame(None, title='测试', size=(320, 150), pos=(550, 350))  # 创建窗口对象，设置参数
# wby.Show()  # 显示窗口
# app.MainLoop()  # 进入主事件循环

# 自定义
import wx
import random
# 定义粉色
PINK_COLOUR = (255, 192, 203)


class IIIWby(wx.Dialog):
    def __init__(self):
        super().__init__(None, title='祝君好', size=(320, 150))
        self.CentreOnScreen()

        self.quotes = ['人生最难的是遇见，更难的其实是重逢。',
                       '人是不容易看清楚自己的。',
                       '你不知道，一听到你的声音，我就很幸福了。',
                       '回忆是一条没有归途的路，以往的一切春天都无法复原。',
                       '有时候不喜欢你的人对你不好，其实就是对你好。',
                       '每一个不曾起舞的日子，都是对生命的辜负。',
                       'Out of sight，out of love. （看不到了，也就不再爱了）',
                       '不乱于心，不困于情，不畏将来，不念过往，如此，安好！',
                       '死亡时一面镜子，反射出生命在它面前做的各种姿态是如此的徒劳。',
                       '除了拼命工作之外，不存在第二条通向成功之路。一个人想要跨越到什么样的阶层，过什么样的生活，就看他怎样对待自己的工作,',
                       '拼不一定活，不拼一定死。',
                       '你若盛开，清风自来；你若精彩，天自安排。',
                       '我们必须接受有限的失望，但是千万不可失去无限的希望。'
                       '当你凝视深渊时，深渊也在凝视你。',
                       '你是我人生中唯一的主角，我却只能演配角。',
                       '我愿做一个不动声色的大人了。不准情绪化，不准偷偷想念，不准回头看，去过自己另外的生活。',
                       '你走之后，我再也没见过这么好看的天空。',
                       '你走，我走，来生再见。']

        random_1 = random.choice(self.quotes)
        # 添加窗口控件
        panel = wx.Panel(parent=self)  # 创建面板对象
        panel.SetBackgroundColour(PINK_COLOUR)  # 设置面板的背景颜色为粉色
        self.statictext = wx.StaticText(parent=panel, label=random_1)  # 创建静态文本

        # 创建垂直方向盒子布局管理器对象iiivbox
        iiivbox = wx.BoxSizer(wx.VERTICAL)
        iiivbox.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
        # 设置面板的布局管理器为iiivbox
        self.SetSizer(iiivbox)
        self.Fit()


class IIWby(wx.Dialog):
    def __init__(self):
        super().__init__(None, title='警告！', size=(320, 150))
        self.CentreOnScreen()
        # 添加窗口控件
        panel = wx.Panel(parent=self)  # 创建面板对象
        panel.SetBackgroundColour(PINK_COLOUR)  # 设置面板的背景颜色为粉色
        self.statictext = wx.StaticText(parent=panel, label='说了不要碰我，不听是吧，想死是吧')  # 创建静态文本

        # 创建垂直方向盒子布局管理器对象iivbox
        iivbox = wx.BoxSizer(wx.VERTICAL)
        iivbox.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
        # 设置面板的布局管理器为iivbox
        self.SetSizer(iivbox)
        self.Fit()


class IWby(wx.Dialog):
    def __init__(self):
        super().__init__(None, title='哼', size=(320, 150))
        self.CentreOnScreen()
        # 添加窗口控件
        panel = wx.Panel(parent=self)  # 创建面板对象
        panel.SetBackgroundColour(PINK_COLOUR)  # 设置面板的背景颜色为粉色
        self.statictext = wx.StaticText(parent=panel, label='点就点吧，真拿你没办法')  # 创建静态文本

        # 创建垂直方向盒子布局管理器对象ivbox
        ivbox = wx.BoxSizer(wx.VERTICAL)
        ivbox.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
        # 设置面板的布局管理器为ivbox
        self.SetSizer(ivbox)
        self.Fit()


class Wby(wx.Frame):  # 自定义窗口父类Wby
    def __init__(self):
        super().__init__(None, title='反骨', size=(300, 350))
        self.CentreOnScreen()
        # 添加窗口控件
        panel = wx.Panel(parent=self)  # 创建面板对象
        panel.SetBackgroundColour(PINK_COLOUR)  # 设置面板的背景颜色为粉色
        self.statictext = wx.StaticText(parent=panel, label='我是反骨仔')  # 创建静态文本
        b1 = wx.Button(parent=panel, id=10, label='别点我!')  # 创建按钮对象
        b2 = wx.Button(parent=panel, id=11, label='不许碰我!')  # 创建按钮对象
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
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()

        elif event_id == 11:
            iiwby = IIWby()
            iiwby.ShowModal()
            iiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
        else:
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiwby = IIWby()
            iiwby.ShowModal()
            iiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            iiiwby = IIIWby()
            iiiwby.ShowModal()
            iiiwby.Destroy()
            self.Close()  # 关闭窗口


#        event.Skip()  # 调用默认的事件处理函数
app = wx.App()  # 创建应用程序对象
kpl = Wby()  # 创建窗口对象
kpl.Show()  # 显示窗口
app.MainLoop()  # 进入主事件循环

