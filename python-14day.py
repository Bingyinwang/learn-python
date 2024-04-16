# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/12  16:35
# 复习和练习
# 1，给定整数n，编写程序以生成包含（i，i*i）的字典，该字典为1-n之间的整数（都包括在内）
# 假设输入8
# 输出应为{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# 方法一：使用for循环
n = int(input("请输入一个整数："))
ans = {}
for i in range(1, n+1):
    ans[i] = i * i

print(ans)

# 方法二：使用字典
n = int(input("请输入一个整数："))
ans = {i: i * i for i in range(1, n+1)}

print(ans)


# 2,编写以下程序，该程序接受一个逗号分隔的数字序列，并生成一个列表和一个包含每个数字的元组
# 例如，输入：11,33,67,43,97,54,27,87
# 方法一：
lst = input("请输入一个逗号分隔的数字序列：").split(",")
tup = tuple(lst)

print("列表形式：", lst)
print("元组形式：", tup)

# 方法二：一行解决
print(tuple(input("请输入一个逗号分隔的数字序列：").split(",")))


# 3，定义一个至少有两个方法的类，getstring:从控制台输入获取字符串，printstring：以大写字母打印字符串,包括简单的测试来测试类方法
class MyClass:
    def getstring(self):
        user_input = input("请输入一个字符串：")
        return user_input

    def printstring(self, input_string):
        upper_string = input_string.upper()
        print(upper_string)


if __name__ == "__main__":
    a = MyClass()
    input_string = a.getstring()
    a.printstring(input_string)

# 4,编写一个程序，根据给定的公式计算并打印该值
# Q = [(2_C_D)/H]的平方根
# 其中，C和H是固定值，D是变量
# C为50，H为30，D的值以逗号分隔输入到程序中
#
# 方法一：
from math import sqrt

C, H = 50, 30


def calc(D):
    return sqrt((2 * C * D) / H)


D = [int(x) for x in input("请输入D的值，以逗号分隔：").split(",")]  # 以逗号分隔在列表中
D = [int(x) for x in D]  # 转换字符串为整数
D = [calc(x) for x in D]  # 返回浮点值，通过每个项目的计算方法
D = [round(x) for x in D]  # 所有的浮动值是圆形的，round得到的是四舍五入的值
D = [str(x) for x in D]  # 所有整数被转换为字符串，以便能够应用加入操作

print(",".join(D))

# 方法二：
from math import sqrt

C, H = 50, 30


def calc(D):
    return sqrt((2 * C * D) / H)


D = [int(x) for x in input("请输入D的值，以逗号分隔：").split(",")]  # 以逗号分隔在列表中
D = [str(round(calc(x))) for x in D]
print(",".join(D))

# 5,map()函数用法
# 在Python中，map() 是一个内置函数，它接受一个函数和一个或多个可迭代对象（如列表、元组等）作为输入，并返回一个迭代器，该迭代器会逐个应用函数到可迭代对象的每个元素上。
# 示例：
def sancifang(q):
    return q ** 3


nums = [1, 2, 3]
s = map(sancifang, nums)  # map() 函数返回一个迭代器，你可以通过 list() 函数将其转换为列表，以便查看结果
print(list(s))


# 6，编写一个程序，该程序X，Y两位数字作为输入并生成一个二维数组，数组的第i行的第j列的值为i*j。
# 注：i = 0,1...,x-1 j = 0,1....y-1,假设一下输入提供给程序：3,5

# 方法一：
x, y = map(int, input("请输入x,y的值，以逗号分隔：").split(","))
lst = []  # 初始化一个空列表lst，用于存放二维数组

for i in range(x):
    tmp = []   # 初始化一个空列表tmp，用于存放每一行的元素
    for j in range(y):  # 遍历每一行
        tmp.append(i * j)  # 将i*j添加到tmp列表中

    lst.append(tmp)   # 将每一行添加到lst列表中

print(lst)

# 方法二：
x, y = map(int, input("请输入x,y的值，以逗号分隔：").split(","))
lst = [[i * j for j in range(y)] for i in range(x)]  # 使用列表推导式生成二维数组
print(lst)


# 7，编写一个程序，该程序接受以逗号分隔的单词序列作为输入，并按字母顺序对单词进行排序后以逗号分隔的顺序打印这些单词
# 随意提供几个单词输入测试

# 方法一：
items = [x for x in input("请输入以逗号分隔的单词序列：").split(",")]
items.sort()
print(",".join(items))


# 方法二：
# 定义函数
def my_fun(e):
    return e[0]


my_list = input("请输入以逗号分隔的单词序列：").split(',')
my_list.sort(key=my_fun)
print(",".join(my_list))

# 8,编写一个接受行序列作为输入的程序，使句子中所有字符都大写之后打印行。
# 输入：Out of sight，out of love.
# 方法一：
lst = []
while True:
    x = input('请输入一行字符：')
    if len(x) == 0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)


# 方法二：

def u_input():
    while True:
        x = input('请输入一行字符：')
        if not x:  # 检查用户输入的字符串x是否为空（即用户是否输入了一个空行或只按下了回车）。
            return  # 如果x为空，则退出循环并返回None。
        yield x  # 如果x不为空，则使用yield关键字将x作为生成器的下一个值返回。这允许生成器在每次迭代时“暂停”和“恢复”，而不是一次性执行完整个循环。


for line in map(str.upper, u_input()):
    print(line)


# 9,编写一个程序，该程序接受一系列以空格分隔的单词作为输入，并在删除所有重复的单词并将其按字母数字顺序排序后打印这些单词

# # 方法一：
word = input('请输入：').split()
u_word = list(set(word))
u_word.sort()

print(' '.join(u_word))


# # 方法二：
i = input('请输入：').split()
o = []
for words in i:
    if words not in o:
        o.append(words)

print(' '.join(sorted(o)))


# 10,编写一个程序，该程序查找介于1000,3000之间的数字，都包括在内，打印所有偶数，以逗号分隔
# 方法一：
for i in range(1000, 3001):
    if i % 2 == 0:
        print(i, end=',')

# 方法二：
a = [i for i in range(1000, 3001) if i % 2 == 0]
lst = [a]
print(';'.join(map(str, lst)))

