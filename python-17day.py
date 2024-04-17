# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/17  13:32

# 1 字符串的编码和解码
print(ord('中'))
print(ord('国'))

CN = chr(20013) + chr(22269)
print(CN)

# 2 BMI指数计算
height = float(input('请输入您的身高(m):'))
weight = float(input('请输入您的体重(kg):'))
bmi = weight / (height ** 2)
print('您的BMI指数为:', bmi)
if bmi < 18.5:
    print('您的体重过轻')
elif bmi < 25:
    print('您的体重正常')
elif bmi < 28:
    print('您的体重过重')
elif bmi < 32:
    print('您的体重肥胖')
else:
    print('您的体重非常肥胖')

# 3 双色球
import random

red_ball = [i for i in range(1, 34)]
blue_ball = [i for i in range(1, 17)]

n = int(input('机选几注：'))
for _ in range(n):
    selected_balls = random.sample(red_ball, 6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f'\033[31m{ball:0>2d}', end=' ')

    selected_blue_ball = random.choice(blue_ball)
    print(f'\033[34m{selected_blue_ball:0>2d}', end=' ')

    print()

# 4 输出彩色文字   ANSI颜色代码
m = "地方规划局"
print(f'\033[31m{m}')
# "\033[*m"是转义序列以“\033[”开头，后面跟着一系列的数字和分号，最后以字母“m”结尾，*号更换为数字。其中，数字和分号的组合表示不同的颜色和样式
'''
注："\033[*m"------是转义序列以“\033[”开头，后面跟着一系列的数字和分号，最后以字母“m”结尾，*号更换为数字。其中，数字和分号的组合表示不同的颜色和样式
    在ANSI颜色代码中，有8种基本颜色，分别是黑色30、红色31、绿色32、黄色33、蓝色34、洋红色35、青色36和白色37。
    除了基本颜色，ANSI颜色代码还支持一些特殊的样式，如加粗、下划线、闪烁等，这些样式也有对应的数字代码，可以与颜色代码组合使用。
'''

# 5 跑马灯文字  在终端运行效果更好
import os
import time

text = '\033[31m每一个不曾起舞的日子，都是对生命的辜负。' + ' ' * 15
while True:
    os.system('cls')
    print(text)
    text = text[1:] + text[0]
    time.sleep(0.2)




