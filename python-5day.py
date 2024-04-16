# 开发人：wby
# 类型：python
# 开发时间：2024/4/1  14:38
# 运算符：算数运算符，比较运算符，逻辑运算符，位运算符，赋值运算符，运算符的优先级
#
# 1，算术运算符：用于组织整数类型和浮点类型的数据，有一元运算符和二元运算符之分
# 一元运算符，正号（+），负号（-），例如+a还是a，-a是对a的取反运算
# 二元运算符 加（+） 减（-） 乘（*） 除（/） 取余（%） 幂（**） 地板除法（//）
# 地板除法（//）：a // b 求小于a与b的商的最大整数
#
# 2，比较运算符： 等于（==） 不等于（！=） 大于（>） 小于（<） 小于等于（<=） 大于等于（>=）
# 返回类型为bool，正确返回True，其他返回False
#
# 3，逻辑运算符：逻辑非（not） 逻辑与（and） 逻辑或（or）
# and & or 用于布尔之间的运算，经常用于处理复合条件，两个条件同时满足
# and 并且，一假都为假，两真才是真
# or  或者，一真都为真，两假才是假
#
# 4，位运算符 以二进制位（bit）为单位进行运算，操作数和结果都是整数类型的数据
# 位反（~） 位与（&） 位或（|） 位异或（^） 右移（>>） 左移（<<）
# ~x : 将x的值按位取反  公式：~a = -1 *（a+1）
# x & y : 将x与y按位进行位与运算
# x | y : 将x与y按位进行位或运算
# x ^ y : 将x与y按位进行位异或运算
# x >> a : 将x右移a位，高位采用符号位补位
# x << a : 将x左移a位，低位用0补位

# 程序流程控制
# 分支语句，循环语句，跳转语句
# 1，分支语句
# 1.1 if结构
#      if 条件:
#           语句组
# 例：
score = int(input('请输入一个0-100的整数：'))
if score >= 85:
    print('优秀')
if score < 60:
    print('要努力了！')
if (score >= 60) and (score < 85):
    print('良好')

# 1.2 if-else结构
#     if 条件:
#         语句组
#     else：
#         语句组
# 例
score = int(input('请输入一个0-100的整数：'))
if score >= 60:

    if score >= 85:
        print('优秀')
    else:
        print('良好')
else:
    print('要努力了！')

# 1.3 if-elif-else （多分支）
#     if 条件:
#         语句组1
#     elif:
#         语句组2
#     elif:
#         语句组3
#       ...
#     elif:
#         语句组n
#     else：
#         语句组 n+1
# 例
score = int(input('请输入一个0-100的整数：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
# print('Grade =' + grade)          # 第一种写法
# print('Grade={}'.format(grade))   # 第二种写法，str.format()
print(f'Grade = {grade}')           # 第三种写法，使用f-string（在Python 3.6及更高版本中）

# 2 循环语句
# 2.1 while语句
# 例
i = 0
while i * i < 1000:
    i += 1
print('i ={}'.format(i))
print(f'i * i = {i*i}')

# 2.2 while-else语句
# 例
i = 0
while  i * i < 20:
    i += 1
    if i == 4:
     break
    print(f'{i}*{i}={i*i}')
else:
    print('while over!')

# 2.3 for 语句 for...in...
# for 变量 in 可迭代对象   # 可迭代对象包括字符串，列表，元组，集合和字典等
# 例
for i in 'wby':   #迭代字符串
    print(i)

numbers = [11,22,33,44,55,66,77,88,99]     # 声明整数列表
for j in numbers:
    print(j)

# 2.4 for-else
# 例
for a in range(10):
    print(a)
else:
    print('for over!!!')

# 加if
for b in range(10):
    if b == 5:
        break
    print(b)
else:
    print('for over!!!')


# 3 跳转语句 （break continue）--用于循环体， （return）--用于函数体
# 3.1 break语句 ，用于强行退出循环体，不再执行循环体剩下的语句
for b in range(10):
    if b == 3:
        break
    print(b)
# 3.2 continue语句，用于结束本次循环，跳过循环体尚未执行的语句，接着进行终止条件的判断，以决定是否继续循环
for b in range(10):
    if b == 3:
       continue
    print(b)






