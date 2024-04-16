# 开发人：wby
# 类型：python
# 开发时间：2024/3/31  9:52

# 循环
# for循环  于...其中的每一个元素，做...事情
for every_letter in 'hello world':
    print(every_letter)

for num in range(1, 11):
    print(str(num) + ' + 1 = ', num + 1)

# for 与 if 结合使用
songlist = ['负重一万斤长大', '动物世界', '牧马城市']  # 创建一个歌曲列表
for song in songlist:
    if song == '负重一万斤长大':
        print(song, ' - 太一')
    elif song == '动物世界':
        print(song, ' - 薛之谦')
    elif song == '牧马城市':
        print(song, ' - 毛不易')

# 嵌套循环 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i * j))

# while 循环 只要条件成立，就一直做
# while 1<3:           # 死循环
#     print('1比3小')   # 不暂停会一直打印

# 在循环过程中，制造某种可以使循环停下来的条件
count = 0
while True:
    print('我最棒！！！')
    count = count + 1
    if count == 5:
        break

# password_list = ['@110119120', '123456789']
# def account_login():
#     tries = 3
#     while tries > 0:
#         password = input('请输入Password：')
#         password_c = password == password_list[-1]
#         password_r = password == password_list[0]
#
#         if password_c:
#             print('登录成功')
#             break
#         elif password_r:
#             new_password = input('重置一个新密码：')
#             password_list.append(new_password)
#             print('密码更改成功，请重新登录')
#             account_login()
#         else:
#             print('密码错误或无效输入')
#             tries = tries - 1
#             print(tries, 'times left')
#
#     else:
#         print('账户已锁定')
#
#
# account_login()


# 练习1，设计一个函数，在桌面的文件夹中创建10个txt文件，以数字命名
# 使用for循环
# def c_txt():  # 定义函数
#     i = 1
#     # name = ['1','2','3','4','5','6','7','8','9','10']   # 第一种列表
#     # for i in name:
#     for i in range(1, 11):  # 第二种排列
#         i = str(i)
#         desktop_path = 'D://桌面文件/1-10/'  # 桌面路径
#         full_path = desktop_path + i + '.txt'  # 完整路径
#         file = open(full_path, 'w')  # 有，打开，保存。没有，创建
#         file.close()  # 关闭
#
#         i = i + str(1)  # i +1 后每次重新赋值得到i
#
#
# c_txt()  # 调用函数
#
#
# # 使用while循环
# def c_txt():  # 定义函数
#     i = 1
#     while i > 0:
#         i_s = str(i)
#         desktop_path = 'D://桌面文件/1-10/'  # 桌面路径
#         full_path = desktop_path + i_s + '.txt'  # 完整路径
#         file = open(full_path, 'w')  # 有，打开，保存。没有，创建
#         file.close()  # 关闭
#         i = i + 1  # i +1 后每次重新赋值得到i
#         if i == 11:  # 这个条件非常重要，不加的话，程序运行下去，会创建n个文件哦！不要问我为啥，我试了，啊哈哈哈！
#             break
#
#
# c_txt()  # 调用函数


# 练习2，复利(参考的CSDN上的博客和AI，完成）

amount = float(input('请输入amount: '))
time = int(input('请输入投资期限(单位：年): '))
rate = float(input('请输入投资年化收益率: '))


def invest(amount, time, rate=0.05):
    for i in range(time):
        amount = amount * (rate + 1)
        print(f'第{i + 1}年结束时，本利合计：{amount:.2f}')


invest(amount, time, rate)

# 练习3，打印1-100内的偶数
# a = 1
# count = 0
# for a in range(1, 101):
#     if a % 2 == 0:  # 条件1，偶数
#         print(a)
#     elif a <= 100:  # 条件2 1-100之间
#         a = a + 1
#         count = count + 1  # 计数
# print('共有偶数:', count)
#
# # 练习4，打印1-100内的奇数
# a = 1
# count = 0
# for a in range(1, 101):
#     if a % 2 == 1:  # 条件1，奇数
#         print(a)
#     elif a <= 100:  # 条件2 1-100之间
#         a = a + 1
#         count = count + 1  # 计数
# print('共有奇数:', count)
