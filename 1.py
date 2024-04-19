# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/9  1:17
# import tkinter as tk
#
#
# def on_button_click():
#     print("Button clicked!")
#
#
# root = tk.Tk()
# root.title("Tkinter Example")
# root.geometry("400x300")
# button = tk.Button(root, text = "张杰学python!", command=on_button_click)
# button.pack()
#
# root.mainloop()

# 爱心动态代码
# import random
# from math import sin, cos, pi, log
# from tkinter import *
#
# CANVAS_WIDTH = 640
# CANVAS_HEIGHT = 480
# CANVAS_CENTER_X = CANVAS_WIDTH / 2
# CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
# IMAGE_ENLARGE = 11
# HEART_COLOR = "#FFC0CB" #ff2121
#
#
# def heart_function(t, shrink_ratio: float = IMAGE_ENLARGE):
#
#     x = 16 * (sin(t) ** 3)
#     y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
#
#     x *= shrink_ratio
#     y *= shrink_ratio
#
#     x += CANVAS_CENTER_X
#     y += CANVAS_CENTER_Y
#
#     return int(x), int(y)
#
#
# def scatter_inside(x, y, beta=0.15):
#
#     ratio_x = - beta * log(random.random())
#     ratio_y = - beta * log(random.random())
#
#     dx = ratio_x * (x - CANVAS_CENTER_X)
#     dy = ratio_y * (y - CANVAS_CENTER_Y)
#
#     return x - dx, y - dy
#
#
# def shrink(x, y, ratio):
#
#     force = -1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6)  # 这个参数...
#     dx = ratio * force * (x - CANVAS_CENTER_X)
#     dy = ratio * force * (y - CANVAS_CENTER_Y)
#     return x - dx, y - dy
#
#
# def curve(p):
#
#     return 2 * (2 * sin(4 * p)) / (2 * pi)
#
#
# class Heart:
#
#     def __init__(self, generate_frame=20):
#         self._points = set()  # 原始爱心坐标集合
#         self._edge_diffusion_points = set()  # 边缘扩散效果点坐标集合
#         self._center_diffusion_points = set()  # 中心扩散效果点坐标集合
#         self.all_points = {}  # 每帧动态点坐标
#         self.build(2000)
#
#         self.random_halo = 1000
#
#         self.generate_frame = generate_frame
#         for frame in range(generate_frame):
#             self.calc(frame)
#
#     def build(self, number):
#
#         for _ in range(number):
#             t = random.uniform(0, 2 * pi)
#             x, y = heart_function(t)
#             self._points.add((x, y))
#
#
#         for _x, _y in list(self._points):
#             for _ in range(3):
#                 x, y = scatter_inside(_x, _y, 0.05)
#                 self._edge_diffusion_points.add((x, y))
#
#
#         point_list = list(self._points)
#         for _ in range(4000):
#             x, y = random.choice(point_list)
#             x, y = scatter_inside(x, y, 0.17)
#             self._center_diffusion_points.add((x, y))
#
#     @staticmethod
#     def calc_position(x, y, ratio):
#
#         force = 1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.520)  # 魔法参数
#
#         dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
#         dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)
#
#         return x - dx, y - dy
#
#     def calc(self, generate_frame):
#         ratio = 10 * curve(generate_frame / 10 * pi)  # 圆滑的周期的缩放比例
#
#         halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
#         halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))
#
#         all_points = []
#
#         heart_halo_point = set()
#         for _ in range(halo_number):
#             t = random.uniform(0, 2 * pi)
#             x, y = heart_function(t, shrink_ratio=11.6)
#             x, y = shrink(x, y, halo_radius)
#             if (x, y) not in heart_halo_point:
#                 heart_halo_point.add((x, y))
#                 x += random.randint(-14, 14)
#                 y += random.randint(-14, 14)
#                 size = random.choice((1, 2, 2))
#                 all_points.append((x, y, size))
#
#         for x, y in self._points:
#             x, y = self.calc_position(x, y, ratio)
#             size = random.randint(1, 3)
#             all_points.append((x, y, size))
#
#         for x, y in self._edge_diffusion_points:
#             x, y = self.calc_position(x, y, ratio)
#             size = random.randint(1, 2)
#             all_points.append((x, y, size))
#
#         for x, y in self._center_diffusion_points:
#             x, y = self.calc_position(x, y, ratio)
#             size = random.randint(1, 2)
#             all_points.append((x, y, size))
#
#         self.all_points[generate_frame] = all_points
#
#     def render(self, render_canvas, render_frame):
#         for x, y, size in self.all_points[render_frame % self.generate_frame]:
#             render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)
#
#
# def draw(main: Tk, render_canvas: Canvas, render_heart: Heart, render_frame=0):
#     render_canvas.delete('all')
#     render_heart.render(render_canvas, render_frame)
#     main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)
#
#
# if __name__ == '__main__':
#     root = Tk()  # 一个Tk
#     canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
#     canvas.pack()
#     heart = Heart()
#     draw(root, canvas, heart)
#     root.mainloop()
#
# # 运行另一个Python脚本添加的模块
# import subprocess
#
# # 运行另一个 Python 脚本
# subprocess.run(["python", "1.py"], check=True)
#

# *******************************************************************************************************
import pyqrcode

# 设置二维码信息
s = "https://www.baidu.com"

# 生成二维码
url = pyqrcode.create(s)

# 保存二维码
url.svg("baidu.svg", scale=8)

# 显示二维码
url.show()

# 打印二维码信息
# print(url.terminal(quiet_zone=1))

# 密码验证
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# 假设的密码，实际应用中应使用更安全的方式存储和验证密码
PASSWORD = "123456"

# 模板字符串，用于渲染HTML页面
template = """
<!doctype html>
<html>
<head>
    <title>Password Protected Content</title>
</head>
<body>
    <h1>Enter Password</h1>
    <form method="POST" action="{{ url_for('verify_password') }}">
        <input type="password" name="password" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""


@app.route('/')
def index():
    # 渲染登录页面
    return render_template_string(template)


@app.route('/verify', methods=['POST'])
def verify_password():
    # 获取用户输入的密码
    password = request.form.get('password')

    # 验证密码
    if password == PASSWORD:
        # 密码正确，重定向到内容页面或返回内容
        return redirect(url_for('protected_content'))
    else:
        # 密码错误，返回错误信息
        return "Incorrect password", 401  # HTTP状态码401表示未授权


@app.route('/content')
def protected_content():
    # 保护的内容，这里只是一个示例页面
    return 'China'


if __name__ == '__main__':
    app.run(debug=True)



import pyqrcode
from pyqrcode import QRCode

# Flask应用的URL（确保这个URL是外部可访问的）
url = "http://localhost:5000"  # 如果你的服务器部署在其他地方，替换为相应的URL

# 生成二维码
qr = QRCode(url, version=1)

# 保存二维码为SVG文件
qr.svg("password_protected_content.svg", scale=8)

# 显示二维码
qr.show()