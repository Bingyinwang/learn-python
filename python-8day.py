# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/5  8:36

# 统计一篇英文文章中单词出现的频率
wordstring = '''
Life is too short to spend time with people who suck the happiness out of you. If someone wants you in their life, 
they will make room for you. You should not have to fight for a spot. Never, ever insist yourself to someone who 
continuously overlooks your worth. And remember, it’s not the people that stand by your side when you are at your 
best, but the ones who stand beside you when you are at your worst that are your true friends.
'''  # 一篇英文文章
wordstring = wordstring.replace(',', '')
wordstring = wordstring.replace('.', '')  # 标点符号替换

wordlist = wordstring.split()  # 分割单词

wordfreq = []
for w in wordlist:
    # 统计单词出现个数
    wordfreq.append(wordlist.count(w))
d = dict(zip(wordlist, wordfreq))
print(d)

# 补充前面某天学的函数，函数具有函数名，参数，返回值，作用域：当前模块，函数中定义：嵌套函数，类中定义：方法
# 语法格式
# def 函数名(形式参数列表):
#     函数体
#     return 返回值              #如果没有数据返回值，则可以省略return语句

# 1，函数中变量的作用域，可以在模块中创建，作用域使整个模块，称为全局变量。也可以在函数中创建，默认情况下，作用域是整个函数，称为局部变量
x = 20


def p_a():
    x = 10
    print('函数中x={}'.format(x))


p_a()
print('全局变量x={}'.format(x))

# 在函数中将其声明为global，则会将函数中同名的变量提升为全局变量
x = 20


def p_a():
    global x
    x = 10
    print('函数中x={}'.format(x))


p_a()
print('全局变量x={}'.format(x))


# 2，可变函数
# 基于元组的可变函数（*可变函数）
def sum(*numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total


print(sum(100.0, 20.0, 30.0))


# 基于字典的可变函数（**可变函数）
def show_info(**info):
    print('********************************')
    for key, value in info.items():
        print('{0} - {1}'.format(key, value))


show_info(name='wby', age=23, sex=True)
show_info(sutdent_name='wby', student_no='1000')


# 3，过滤函数 filter()
# 语法： filter(function,iterable)
# 参数function是一个提供过滤条件的函数，返回布尔值
# 参数iterable是容器类型的数据

# 处理一批数据
def f1(x):  # 提供过滤条件函数
    return x > 50  # 找出大于50元素


data1 = [66, 15, 91, 55, 77, 43, 63, 78, 22, 19]  # 需要处理的数据
filtered = filter(f1, data1)  # 过滤
data2 = list(filtered)  # 转化为列表
print(data2)  # 输出结果


# 4，映射函数map()
# 语法： map(function,iterable)
# 参数map是一个提供变换规则的函数，返回变换之后的元素
# 参数iterable是容器类型的数据
def f1(x):
    return x * 2  # 变换规则乘以2


data1 = [66, 15, 91, 28, 98, 50, 6, 80, 33]
mapped = map(f1, data1)
data2 = list(mapped)
print(data2)


# 5,匿名函数：lambda()函数
# 语法，lambda 参数列表:lambda体
# lambda体不能是一个代码块，不能包含多条语句，只有一条语句，语句会计算一个结果并返回给lambda()函数，但不需要return语句返回
# 例一：
def calc(opr):
    if opr == '+':
        return lambda a, b: (a + b)
    else:
        return lambda a, b: (a - b)


f1 = calc('+')
f2 = calc('-')
print("10+5={0}".format(f1(10, 5)))
print("10-5={0}".format(f1(10, 5)))


# 例二：
data1 = [66, 15, 91, 28, 98, 50, 6, 80, 33]

filtered = filter(lambda x: (x > 50), data1)
data2 = list(filtered)
print(data2)

mapped = map(lambda x: (x * 2), data1)
data2 = list(mapped)
print(data2)
