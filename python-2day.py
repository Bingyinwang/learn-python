# 开发人：wby
# 类型：python
# 开发时间：2024/3/29  8:22

# 函数， 重新认识函数
# print()      # 是一个放入对象就能将结果打印的函数
# input()      # 是一个可以让用户输入信息的函数
# len()        # 是一个可以测量对象长度的函数
# int()        # 是一个可以将字符串类型的数字转换成整数类型的数字

# 创建函数，定义函数
# def （即define，定义）的含义是创建函数，即定义一个函数
# arg  （即argument，参数）还会有一种写法parameter，都是参数的意思，稍有不同
# return （即返回结果）
# def function(arg1 , arg2):
#     return 'Something'
# 例：定义摄氏度转换华氏度
# def c_f(c):  # 定义函数
#     f = c * 9 / 5 + 32
#     return str(f) + '°F'  # 返回结果
#
#
# C2F = c_f(35)  # 调用函数
# print(C2F)     # 打印结果


# 练习题1
# 输入g转换为kg
# def g_kg(a):       # a为参数
#     kg = a / 1000
#     return str(kg) + 'kg'
#
#
# G_KG = g_kg(90)     # 调用
# print(G_KG)

# 练习题2
# 直角三角形，直角边为参数，求斜边长
# def z_x(a, b):     # a b 为直角边参数
#     x = (a ** 2 + b ** 2) ** (1/2)
#     return str(x) + '是斜边长'
#
#
# ZX = z_x(3, 4)      # 调用
# print(ZX)


# 传递参数：位置参数和关键词参数
# 默认参数，定义参数的时候给参数赋值
# print('  *', ' * *', '* * *', '  | ', sep="\n")  # 打印一颗圣诞树


# 设计自己的函数
# file = open('D://桌面文件/text.txt' , 'w')
# file.write('hello world')

# 定义函数，创建一个文本文件，命名，添加内容
# def text_create(name, msg):
#     desktop_path = 'D://桌面文件/'
#     full_path = desktop_path + name + '.txt'
#     file = open(full_path, 'w')
#     file.write(msg)
#     file.close()
#     print('Done')
#
#
# text_create('1', '123456')  # 调用函数
#
#
# # 敏感词过滤
# def text_filter(word, censored_word='lame', changed_word='Awesome'):
#     return word.replace(censored_word, changed_word)
#
#
# text_filter('Python is lame!')


# def censored_text_create(name, msg):
#     clean_msg = text_filter(msg)
#     text_create(name, clean_msg)
#
#
# censored_text_create('Try', 'lame!,lame!,lame!')
