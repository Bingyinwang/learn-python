# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/10  13:28
# 图形用户界面
# 1，Python中图形用户界面开发库------wxPython
# 1.1，第一个wxPython程序！
# 例子：
import wx  # 导入wxPython模块

# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = wx.Frame(None, title="第一个wxPython程序！", size=(400, 300), pos=(100, 100))  # None表示没有父窗口，size窗口的大小，pos窗口的位置

# 显示窗口
frm.Show()  # 窗口默认隐藏，需要调用Show()方法才能显示

# 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

# 1.2，自定义窗口类
# 例子：
import wx  # 导入wxPython模块


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="中国", size=(400, 300), pos=(100, 100))  # None表示没有父窗口，size窗口的大小，pos窗口的位置
        # 你的代码，窗口中的控件在这里添加


# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = MyFrame()

# 显示窗口
frm.Show()  # 窗口默认隐藏，需要调用Show()方法才能显示

# 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

# 1.3，窗口中添加两个控件，一个面板（Panel），一个静态文本（StaticText）
# 面板是一个没有标题栏的容器（可以容纳其他控件的控件）
# 例子：
import wx  # 导入wxPython模块


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="中国", size=(400, 300), pos=(100, 100))  # None表示没有父窗口，size窗口的大小，pos窗口的位置
        # 你的代码，窗口中的控件在这里添加
        panel = wx.Panel(parent=self)  # 创建面板对象
        statictext = wx.StaticText(parent=panel, label='中国有56个民族', pos=(10, 10))  # 创建静态文本对象


# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = MyFrame()

# 显示窗口
frm.Show()  # 窗口默认隐藏，需要调用Show()方法才能显示

# 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

# 1.4，事件处理
# 事件源：事件发生的场所，就是各个控件
# 事件：wxPython中的事件被封装为事件类wx.Event及其子类，例如按钮事件类是wx.CommandEvent,鼠标事件类是wx.MoveEvent。
# 事件处理程序：一个响应用户事件的方法
# 例子：
import wx  # 导入wxPython模块


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="事件处理", size=(300, 180))  # None表示没有父窗口，size窗口的大小
        # 你的代码，窗口中的控件在这里添加
        panel = wx.Panel(parent=self)  # 创建面板对象
        self.statictext = wx.StaticText(parent=panel, label='请点击OK按钮', pos=(110, 20))  # 创建静态文本对象
        b = wx.Button(parent=panel, label='OK', pos=(100, 50))  # 创建按钮对象
        self.Bind(wx.EVT_BUTTON, self.on_click, b)  # 绑定事件，wx.EVT_BUTTON是事件类型，即按钮点击事件，self.on_click是事件处理程序，b是事件源，即按钮对象

    def on_click(self, event):  # 事件处理程序
        self.statictext.SetLabel('中国')


# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = MyFrame()

# 显示窗口
frm.Show()  # 窗口默认隐藏，需要调用Show()方法才能显示

# 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

# 2, 布局管理
# 2.1 盒子布局管理器，wx.BoxSizer
# Box布局管理器是最常用的布局管理器，可以让其中的子窗口（或控件）沿垂直或水平方向布局
# 2.1.1 创建盒子布局管理对象
# 设置水平方向布局wx.BoxSizer(wx.HORIZONTAL)，默认值可以省略
# 设置垂直方向布局wx.BoxSizer(wx.VERTICAL)
# 2.1.2 添加子窗口（或控件）到父窗口
# 使用wx.BoxSizer对象的Add()方法添加子窗口（或控件）到父窗口，对Add()方法说明如下
# 添加到父窗口：Add(Window,proportion=0,flag=0,border=0)
# 添加到另一个布局对象,用于布局嵌套：Add(sizer,proportion=0,flag=0,border=0)
# proportion参数用于设置当前子窗口（或控件）在父窗口中所占的空间比例。
# flag参数是布局标志，用来控制对齐方式，边框和调整尺寸。
# border参数用于设置边框的宽度
'''flag对齐标志如下
    标志                     说明
wx.ALIGN_TOP                顶对齐
wx.ALIGN_BOTTOM             底对齐
wx.ALIGN_LEFT               左对齐
wx.ALIGN_RIGHT              右对齐
wx.ALIGN_CENTER             居中对齐
wx.ALIGN_CENTER_VERTICAL    垂直居中对齐
wx.ALIGN_CENTER_HORIZONTAL  水平居中对齐
wx.ALIGN_CENTRE             同wx.ALIGN_CENTER
wx.ALIGN_CENTRE_VERTICAL    同wx.ALIGN_CENTER_VERTICAL
wx.ALIGN_CENTRE_HORIZONTAL  同wx.ALIGN_CENTER_HORIZONTAL
'''
'''flag边框标志如下
标志                   说明
wx.TOP                设置有顶部边框，边框宽度需要通过Add()方法的border参数设置
wx.BOTTOM             设置有底部边框
wx.LEFT               设置有左边框
wx.RIGHT              设置有右边框
wx.ALL                设置4面全有边框
'''
'''flag调整尺寸标志
标志                                 说明
wx.EXPAND                           调整子窗口（或控件）完全填满有效空间
wx.SHAPED                           调整子窗口（或控件）填充有效空间，但保存宽高比
wx.FIXED_MINSIZE                    调整子窗口（或控件）为最小尺寸
wx.RESERVE_SPACE_EVEN_IF_HIDDEN     设置后，子窗口（或控件）如果被隐藏，则所占空间保留
'''
# 例子：
import wx  # 导入wxPython模块


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="事件处理", size=(300, 180))  # None表示没有父窗口，size窗口的大小
        # 你的代码，窗口中的控件在这里添加
        panel = wx.Panel(parent=self)  # 创建面板对象
        self.statictext = wx.StaticText(parent=panel, label='请点击OK按钮', pos=(110, 20))  # 创建静态文本对象
        b = wx.Button(parent=panel, label='OK', pos=(100, 50))  # 创建按钮对象
        self.Bind(wx.EVT_BUTTON, self.on_click, b)  # 绑定事件，wx.EVT_BUTTON是事件类型，即按钮点击事件，self.on_click是事件处理程序，b是事件源，即按钮对象

        # 创建垂直方向盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加静态文本到vbox布局管理器
        vbox.Add(self.statictext, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE | wx.Top, border=30)
        # 添加按钮b到vbox布局管理器
        vbox.Add(b, proportion=1, flag=wx.EXPAND | wx.BOTTOM, border=10)
        # 设置面板采用vbox布局管理器
        panel.SetSizer(vbox)

    def on_click(self, event):  # 事件处理程序
        self.statictext.SetLabel('中国')


app = wx.App()  # 创建应用程序对象
frm = MyFrame()  # 创建窗口对象
frm.Show()  # 显示窗口，窗口默认隐藏，需要调用Show()方法才能显示
app.MainLoop()  # 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的


# 2.2 布局管理器嵌套
# 例子：
import wx  # 导入wxPython模块


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="布局管理器嵌套", size=(300, 120))  # None表示没有父窗口，size窗口的大小
        # 你的代码，窗口中的控件在这里添加
        panel = wx.Panel(parent=self)  # 创建面板对象
        self.statictext = wx.StaticText(parent=panel, label='请点击按钮1或2')  # 创建静态文本对象
        b1 = wx.Button(parent=panel, id=10, label='1')  # 创建1按钮对象
        b2 = wx.Button(parent=panel, id=11, label='2')  # 创建2按钮对象

        # 创建水平方向的盒子布局管理器hbox对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # 添加b1到hbox布局管理
        hbox.Add(b1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        # 添加b1到hbox布局管理
        hbox.Add(b2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # 创建垂直方向盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加静态文本到vbox布局管理器
        vbox.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE | wx.Top, border=10)
        # 添加按钮hbox到vbox布局管理器
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)  # 将hbox布局管理器对象添加到vbox布局管理器对象

        # 设置面板采用vbox布局管理器
        panel.SetSizer(vbox)

        # 绑定事件，wx.EVT_BUTTON是事件类型，即按钮点击事件，self.on_click是事件处理程序，id，id2是事件源，即按钮对象
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

    def on_click(self, event):
        event_id = event.GetId()  # 获得绑定按钮的id
        print(event_id)
        if event_id == 10:  # 根据id判断点击哪一个按钮
            self.statictext.SetLabel('大熊猫')
        else:
            self.statictext.SetLabel('小熊猫')


app = wx.App()  # 创建应用程序对象
frm = MyFrame()  # 创建窗口对象
frm.Show()  # 显示窗口，窗口默认隐藏，需要调用Show()方法才能显示
app.MainLoop()  # 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的

# 3，控件，wxPython所有控件都继承自wx.Control类
# 3.1，文本输入控件wx.TextCtrl
# 例子：在界面中实现三个文本输入控件，和三个静态文本
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="文本输入控件", size=(300, 260))  # None表示没有父窗口，size窗口的大小
        # 你的代码，窗口中的控件在这里添加
        panel = wx.Panel(parent=self)  # 创建面板对象
        tc1 = wx.TextCtrl(panel)  # 创建普通文本输入控件
        tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)  # 创建密码输入控件
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)  # 创建多行文本输入控件

        userid = wx.StaticText(panel, label='账号ID：')
        pwd = wx.StaticText(panel, label='密码：')
        content = wx.StaticText(panel, label='多行文本：')

        # 创建垂直方向盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 添加控件到vbox布局管理器
        vbox.Add(userid, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(pwd, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc2, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(content, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc3, flag=wx.EXPAND | wx.ALL, border=10)

        # 设置面板采用vbox布局管理器
        panel.SetSizer(vbox)

        # 设置tc1初始值
        tc1.SetValue('Wby')

        # 获取tc1值
        print('读取账户ID：{0}'.format(tc1.GetValue()))


app = wx.App()  # 创建应用程序对象
frm = MyFrame()  # 创建窗口对象
frm.Show()  # 显示窗口，窗口默认隐藏，需要调用Show()方法才能显示
app.MainLoop()  # 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的

# 3.2， 复选框wx.CheckBox, 单选按钮wx.RadioButton
# 例子：在界面中实现一组复选框和一组单选按钮
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="复选框和单选按钮", size=(500, 120))  # None表示没有父窗口，size窗口的大小
        # 你的代码，窗口中的控件在这里添加
        panel = wx.Panel(parent=self)  # 创建面板对象
        st1 = wx.StaticText(panel, label='选择你喜欢的编程语言')
        cb1 = wx.CheckBox(panel, id=1, label='Python')
        cb1.SetValue(True)
        cb2 = wx.CheckBox(panel, id=2, label='Java')
        cb3 = wx.CheckBox(panel, id=3, label='C++')
        cb4 = wx.CheckBox(panel, id=4, label='Php')
        cb5 = wx.CheckBox(panel, id=5, label='C')
        cb6 = wx.CheckBox(panel, id=6, label='Go')
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1, id2=6)

        st2 = wx.StaticText(panel, label='选择性别')
        radio1 = wx.RadioButton(panel, id=7, label='男', style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, id=8, label='女')
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio1_click, id=7, id2=8)

        hbox1 = wx.BoxSizer()
        hbox1.Add(st1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox1.Add(cb1)
        hbox1.Add(cb2)
        hbox1.Add(cb3)
        hbox1.Add(cb4)
        hbox1.Add(cb5)
        hbox1.Add(cb6)

        hbox2 = wx.BoxSizer()
        hbox2.Add(st2, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox2.Add(radio1)
        hbox2.Add(radio2)

        # 创建垂直方向盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, flag=wx.CENTER, border=10)  # 将hbox1布局管理器对象添加到vbox布局管理器对象
        vbox.Add(hbox2, flag=wx.CENTER, border=10)  # 将hbox2布局管理器对象添加到vbox布局管理器对象
        # 设置面板采用vbox布局管理器
        panel.SetSizer(vbox)

    def on_checkbox_click(self, event):
        cb = event.GetEventObject()
        print(f'选择{cb.GetLabel()}，状态{event.IsChecked()}')

    def on_radio1_click(self, event):
        rb = event.GetEventObject()
        print(f'第一组{rb.GetLabel()}被选中')


app = wx.App()  # 创建应用程序对象
frm = MyFrame()  # 创建窗口对象
frm.Show()  # 显示窗口，窗口默认隐藏，需要调用Show()方法才能显示
app.MainLoop()  # 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的

# 3.3 列表控件wx.ListBox
# 例子：在界面实现两个列表控件，单选和多选
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="列表控件", size=(360, 300))  # None表示没有父窗口，size窗口的大小
        # 你的代码，窗口中的控件在这里添加
        panel = wx.Panel(parent=self)  # 创建面板对象

        st1 = wx.StaticText(panel, label='选择你喜欢的编程语言')
        list1 = ['Python', 'Java', 'C++', 'Php', 'C', 'Go']
        lb1 = wx.ListBox(panel, choices=list1, style=wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox1, lb1)

        st2 = wx.StaticText(panel, label='选择你喜欢的水果')
        list2 = ['苹果', '香蕉', '梨', '橘子', '橙子', '草莓']
        lb2 = wx.ListBox(panel, choices=list2, style=wx.LB_EXTENDED)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox2, lb2)

        hbox1 = wx.BoxSizer()
        hbox1.Add(st1, proportion=1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox1.Add(lb1, proportion=1)

        hbox2 = wx.BoxSizer()
        hbox2.Add(st2, proportion=1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox2.Add(lb2, proportion=1)

        # 创建垂直方向盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, flag=wx.ALL | wx.EXPAND, border=5)  # 将hbox1布局管理器对象添加到vbox布局管理器对象
        vbox.Add(hbox2, flag=wx.ALL | wx.EXPAND, border=5)  # 将hbox2布局管理器对象添加到vbox布局管理器对象
        # 设置面板采用vbox布局管理器
        panel.SetSizer(vbox)

    def on_listbox1(self, event):
        listbox1 = event.GetEventObject()
        print(f'选择{listbox1.GetSelections()}')

    def on_listbox2(self, event):
        listbox2 = event.GetEventObject()
        print(f'选择{listbox2.GetSelections()}')


app = wx.App()  # 创建应用程序对象
frm = MyFrame()  # 创建窗口对象
frm.Show()  # 显示窗口，窗口默认隐藏，需要调用Show()方法才能显示
app.MainLoop()  # 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的
# 注：创建列表控件时，参数style常见取值
'''
wx.LB_SINGLE   单选
wx.LB_MULTIPLE 多选
wx.LB_EXTENDED 多选，但是需要按住Ctrl键或Shift键时选择
wx.LB_SORT     对列表选择项进行排序
'''

# 3.4，静态图片控件，wxPython可以支持任意图片格式,wx.StaticBitmap
# 在界面中实现两个按钮和一个静态图片控件，单击不同按钮显示不同图片
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="静态图片控件", size=(600, 900))  # None表示没有父窗口，size窗口的大小
        # 你的代码，窗口中的控件在这里添加
        self.panel = wx.Panel(parent=self)  # 创建面板对象,它是该类的实例变量

        # 创建wx.Bitmap图片对象的列表
        self.bmps = [wx.Bitmap('D:/桌面文件/1-10/1.jpg', wx.BITMAP_TYPE_ANY),
                     wx.Bitmap('D:/桌面文件/1-10/2.jpg', wx.BITMAP_TYPE_ANY),
                     wx.Bitmap('D:/桌面文件/1-10/3.jpg', wx.BITMAP_TYPE_ANY)]

        b1 = wx.Button(self.panel, id=1, label='1')
        b2 = wx.Button(self.panel, id=2, label='2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)

        self.image = wx.StaticBitmap(self.panel, bitmap=self.bmps[0])

        # 创建垂直方向盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1, proportion=1, flag=wx.FIXED_MINSIZE, border=5)  # 将b1添加到vbox布局管理器对象
        vbox.Add(b2, proportion=1, flag=wx.FIXED_MINSIZE, border=5)  # 将b2添加到vbox布局管理器对象
        vbox.Add(self.image, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)  # 添加图片控件到布局管理器
        # 设置面板采用vbox布局管理器
        self.panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 1:
            self.image.SetBitmap(self.bmps[1])
        else:
            self.image.SetBitmap(self.bmps[2])
        self.panel.Layout()  # 更新布局
        self.Refresh()  # 刷新窗口显示


app = wx.App()  # 创建应用程序对象
frm = MyFrame()  # 创建窗口对象
frm.Show()  # 显示窗口，窗口默认隐藏，需要调用Show()方法才能显示
app.MainLoop()  # 进入主事件循环：事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示及响应用户事件的处理都是通过主事件循环实现的
