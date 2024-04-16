# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/8  16:50

import this  # python之禅

# 第三方库和异常处理

# 第三方库（详细使用及介绍，自行网上查找）
# awesome-python.com上按照分类查找，上面收录了比较全的第三方库
# 也可以在搜索引擎上使用相关关键词进行搜索，最好尝试英文搜索会发现更大的世界
# 安装第三方库
# 1，可以直接在pycharm中直接安装。2，也可以在终端使用pip安装。3，手动安装，下载好安装包，自行导入
# pip常用命令：pip install --upgrade pip  # 升级pip
#             pip uninstall flask       # 卸载库
#             pip list                  # 查看已安装库
# 装第三方库时会遇到依赖包问题，一个原则，缺啥装啥
# 使用第三方库，import 库名，未使用库前显示灰色状态



# 异常处理
# 第一个异常，除零异常
# 在数学中，任何整数都不能除以0，如果在计算机程序中，将整数除以0，则会引发异常
i = input('请输入一个数：')
n = 8888
result = n / int(i)
print(result)
print(f'{n}除以{i}等于{result}')

# 第二个异常，捕获异常
# 发现异常能捕获并处理异常，不至于让程序终止运行
# 使用到：try-except语句,在try代码块中包含在执行过程中可能引发异常的语句，如果没有发生异常，则跳到except代码块执行，这就是异常捕获
# 语法规则：
# try:
#      可能会引发异常的语句
# except 异常类型:            # 异常类型可用省略
#      处理异常
# 指定具体的异常类型，则捕获指定的，不指定具体的异常类型，则捕获全部异常
# 例：指定具体的异常类型
i = input('请输入一个数：')
n = 8888
try:
    result = n / int(i)
    print(result)
    print(f'{n}除以{i}等于{result}')
except ZeroDivisionError as e:            # 捕获除零异常
    print('不能除以0，异常；{}'.format(e))

# 多个except代码块
# 多条语句可能引发多种不同的异常，对每一种异常都会采用不同的处理方式，针对这种情况，可以在try后面跟多个except代码块
i = input('请输入一个数：')
n = 8888
try:
    result = n / int(i)
    print(result)
    print(f'{n}除以{i}等于{result}')
except ZeroDivisionError as e:  # 捕获除零异常
    print('不能除以0，异常；{}'.format(e))
except ValueError as e:  # 捕获整数转换异常
    print('输入的是无效数字，异常：{}'.format(e))

# 多重异常捕获
i = input('请输入一个数：')
n = 8888
try:
    result = n / int(i)
    print(result)
    print(f'{n}除以{i}等于{result}')
except (ZeroDivisionError, ValueError) as e:
    print('异常；{}'.format(e))

# try-except语句嵌套
i = input('请输入一个数：')
n = 8888
try:
    i2 = int(i)
    try:
        result = n / int(i)
        print(result)
        print(f'{n}除以{i}等于{result}')
    except ZeroDivisionError as e1:  # 捕获除零异常
        print('不能除以0，异常；{}'.format(e1))

except ValueError as e2:  # 捕获整数转换异常
    print('输入的是无效数字，异常：{}'.format(e2))

# 使用finally释放资源
# 在try-except代码块后跟一个finally代码块可以释放资源
# 无论是try代码块正常结束，还是except代码块异常结束，都会执行finally代码块
i = input('请输入一个数：')
n = 8888
try:
    result = n / int(i)
    print(result)
    print(f'{n}除以{i}等于{result}')
except ZeroDivisionError as e:  # 捕获除零异常
    print('不能除以0，异常；{}'.format(e))
except ValueError as e:  # 捕获整数转换异常
    print('输入的是无效数字，异常：{}'.format(e))
finally:
    print('资源释放......')


# 自定义异常和手动引发异常
# class wby(Exception):  # wby是自定义异常类的名称，Exception是异常父类
#     def __init__(self, message):  # 构造方法，参数message是描述异常信息
#         super().__init__(message)  # 调用父类构造方法，并把参数message传给父类构造方法
#
#
# i = input('请输入一个数：')
# n = 8888
# try:
#     result = n / int(i)
#     print(result)
#     print(f'{n}除以{i}等于{result}')
# except ZeroDivisionError as e:  # 捕获除零异常
# #    print('不能除以0，异常；{}'.format(e))
#      raise wby('不能除以0')
# except ValueError as e:  # 捕获整数转换异常
# #    print('输入的是无效数字，异常：{}'.format(e))
#      raise wby('输入的是无效数字')


