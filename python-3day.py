# 开发人：wby
# 类型：python
# 开发时间：2024/3/30  9:47
# 逻辑控制与循环

# 逻辑判断 ， True & False
# 布尔类型 ： True & False
# 能够产生一个布尔值的表达式称为布尔表达式
# 1>2               #False
# 1<2<3             #True
# 42 != '42'        #True
# 'Name' == 'name'  #False
# 'M' in 'Magic'    #True
# number = 12
# number is 12      #True

# 比较运算符  如果比较式成立则返回True，不成立则返回False

# 多条件的比较，先给变量赋值，再进行多条件比较
# middle = 5
# 1 < middle < 10

# 变量的比较
# two = 1 + 1
# three = 1 + 3
# two < three

# 字符串的比较
# 'Eddie Van Helen' == 'eddie van helen'  # python中有严格的大小写区分

# 两个函数产生的结果进行比较： 比较运算符会先调用函数后再进行比较
# abs(-10) > len('length of this word')          # 其结果等价于10>19, abs()是一个会返回输入参数绝对值的参数
# 不同类型的对象不能使用'<,>,<=,>='进行比较，可以使用'==,!='
# 例如：字符串和数字之间，整数和浮点虽是不同类型，但不影响比较运算


# 列表
# wby = []       # 创建列表，列表为空
wby = ['paper', 'china', 'money', 7, 9, 11, True]  # 往列表中添加东西，非空列表
wby.append('new song')  # 列表中添加新内容，使用列表的append方法，会自动添加到列表尾部
print(wby[0], wby[-1])  # 列表索引

p = 'money' in wby  # 从列表中查找'money'是否在里面
print(p)  # 结果为True

# 归属关系布尔运算符（in，not in）    身份鉴别布尔运算符（is，is not）
# python中任何一个对象都要满足身份（identity）类型（Type）值(Value)这三点缺一不可
# is 操作符号就是用来身份对比的
E = 'Eddie'
name = 'Eddie'
e = E == name
q = E is name
print(e)
print(q)

# 逻辑运算符
# and & or 用于布尔之间的运算，经常用于处理复合条件，两个条件同时满足
# and 并且，一假都为假，两真才是真
# or  或者，一真都为真，两假才是假

# 条件控制: if...else
# 例子：账户登录
# def account_login():
#     password = input('请输入Password:')
#     if password == '123456':
#         print('登录成功！')
#     else:
#         print('登录失败，请重新输入')
#         account_login()  # 运行函数
#
#
# account_login()  # 调用函数


# 完善上述账户登录，增加重置密码功能

password_list = ['@******', '123456789']  # 创建列表，储存用户密码，初始密码及其他数据


def account_login():  # 定义函数
    password = input('请输入Password:')  # 用户输入密码储存在变量password中
    password_c = password == password_list[-1]  # 用户输入密码等于列表最后一个元素时，登录成功
    password_reset = password == password_list[0]  # 用户输入密码等于列表第一个元素时，重置密码
    if password_c:
        print('登录成功！')
    elif password_reset:
        new_password = input('设置一个新password:')
        password_list.append(new_password)  # 新密码更新到列表最后一个元素
        print('密码更改成功，请重新登录')
        account_login()  # 运行函数
    else:
        print('登录失败，请重新输入')
        account_login()  # 运行函数


account_login()  # 调用函数


