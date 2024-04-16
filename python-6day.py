# 开发人：wby
# 类型：python
# 开发时间：2024/4/2  8:26
# 一些小练习
# 1，计算水仙花数，水仙花数是指一个 n 位数 (n≥3)，它的每个位上的数字的 n 次幂之和等于它本身
# 计算水仙花数是一个三位数，三位数各位的立方之和等于三位数本身
# while循环求法
i = 100;
r = 0;
s = 0;
t = 0
while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == (r ** 3 + s ** 3 + t ** 3):
        print(f'水仙花数为:{i}')

    i += 1


# for循环求法
def shuixianhua():
    for i in range(100, 1000):
        r = i // 100
        s = (i // 10) % 10
        t = i % 10
        num = r ** 3 + s ** 3 + t ** 3
        if num == i:
            print('水仙花数为:{}'.format(i))


shuixianhua()

# 2，猜大小 （由AI改编）
# import random
#
#
# def roll_dice(numbers=3):
#     points = []
#     for _ in range(numbers):
#         point = random.randrange(1, 7)
#         points.append(point)
#     return points
#
#
# def roll_result(total):
#     return 'Big' if 11 <= total <= 18 else 'Small'
#
#
# def start_game():
#     balance = 1000  # 初始金额
#     odds = 1  # 默认赔率
#     bet = 0  # 初始下注金额为0
#
#     while balance > 0:
#         print('<<<<<<<  猜大小游戏 >>>>>>>')
#         print(f'当前余额：{balance}')
#         print('请输入下注金额（余额为0时游戏结束）：', end=' ')
#         bet_input = input()
#         if bet_input.lower() == '0':
#             print('游戏结束，感谢您的参与！')
#             break
#         try:
#             bet = int(bet_input)
#             if bet > balance:
#                 print('下注金额超过余额，请重新输入！')
#                 continue
#         except ValueError:
#             print('请输入有效的数字作为下注金额！')
#             continue
#
#         print('请输入Big or Small：', end=' ')
#         your_choice = input()
#         if your_choice not in ['Big', 'Small']:
#             print('无效输入，请重新输入！')
#             continue
#
#         points = roll_dice()
#         total = sum(points)
#         result = roll_result(total)
#
#         print(f'投掷结果为：{points} = {total}')
#
#         if your_choice == result:
#             win_amount = bet * odds
#             balance += win_amount
#             print(f'你赢了！赢得金额：{win_amount}，当前余额：{balance}')
#         else:
#             balance -= bet
#             print(f'你输了！扣除下注金额：{bet}，当前余额：{balance}')
#
#         # 开始游戏
#
#
# start_game()

# 3，查找数字，可以被7整除，但不能是5的倍数，在1000-3000之间，包含1000和3000，获得的数字打印在一行上，用逗号隔开
# 使用for循环
a = []
for i in range(1000, 3001):
    if i % 7 == 0 and (i % 5 != 0):
        a.append(str(i))
# print(','.join(a))
print(f'{a}')

# 4，计算数字阶乘
# 使用while循环
n = int(input('请输入想要计算的数字：'))
a = 1
i = 1
while i <= n:
    a = a * i
    i += 1
print(a)

# 使用for循环
n = int(input('请输入想要计算的数字：'))
a = 1
for i in range(1,n+1):
    a = a * i
print(a)
