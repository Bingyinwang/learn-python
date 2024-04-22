# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/20


# 1.1 发送GET请求，获取响应
import urllib.request  # 导入urllib.request模块

url = 'http://www.baidu.com/?action=query&ID=10'  # 请求URL网址，？后的内容是请求参数，多个参数用&分隔，例如action是参数名，query是参数值

req = urllib.request.Request(url)  # 创建一个请求对象，默认是GET请求
with urllib.request.urlopen(req) as response:  # 发送请求，并获取响应对象，可是使用with as代码块管理和释放
    data = response.read()  # 读取数据，为字节序列数据
    json_data = data.decode()  # 将字节序列数据转换为字符串
    print(json_data)  # 输出字符串数据

# 1.2 发送POST请求，提交数据

import urllib.request  # 导入urllib.request模块

url = 'http://www.baidu.com/'

# 准备HTTP参数
params_dict = {'action': 'query', 'ID': '10'}
params_str = urllib.parse.urlencode(params_dict)  # 将字典转换为URL参数字符串
print(params_str)

# 字符串转换为字节序列数据
params_bytes = params_str.encode()

# 创建一个请求对象，设置请求方法为POST
req = urllib.request.Request(url, data=params_bytes)  # 发送POST请求，并设置请求方法为POST

with urllib.request.urlopen(req) as response:  # 发送请求，并获取响应对象，可使用with as代码块管理和释放
    data = response.read()  # 读取数据，为字节序列数据
    json_data = data.decode()  # 将字节序列数据转换为字符串
    print(json_data)  # 输出字符串数据

# 1.3 使用json模块提供的loads（str）函数进行JSON数据的解码，参数str是JSON字符串，返回python数据。
import urllib.request  # 导入urllib.request模块
import json

url = 'http://www.baidu.com/?action=query&ID=10'  # 请求URL网址，？后的内容是请求参数，多个参数用&分隔，例如action是参数名，query是参数值

req = urllib.request.Request(url)  # 创建一个请求对象，默认是GET请求

with urllib.request.urlopen(req) as response:  # 发送请求，并获取响应对象，可是使用with as代码块管理和释放
    data = response.read()  # 读取数据，为字节序列数据
    json_data = data.decode()  # 将字节序列数据转换为字符串
    print('JSON字符串：', json_data)  # 输出字符串数据

    py_dict = json.load(json_data)  # 解码json字符串，返回字典
    print('备忘录ID:', py_dict['ID'])
    print('备忘录日期:', py_dict['CDate'])
    print('备忘录内容:', py_dict['Content'])
    print('用户ID:', py_dict['UserID'])

# 1.4 下载图片示例
import urllib.request  # 导入urllib.request模块

url = 'http://www.baidu.com/img/logo.png'

req = urllib.request.Request(url)  # 创建一个请求对象，默认是GET请求

with urllib.request.urlopen(req) as response:  # 发送请求，并获取响应对象，可使用with as代码块管理和释放
    data = response.read()  # 读取数据，为字节序列数据
    f_name = 'logo.png'  # 文件名
    with open(f_name, 'wb') as f:  # 创建文件对象，并设置写入模式，wb表示写入二进制数据
        f.write(data)  # 将字节序列数据写入文件
        print('图片下载完成')

# 1.5 返回所有备忘录信息
import urllib.request  # 导入urllib.request模块
import json

url = 'http://www.baidu.com/'  # 请求URL网址

req = urllib.request.Request(url)  # 创建一个请求对象，默认是GET请求

with urllib.request.urlopen(req) as response:  # 发送请求，并获取响应对象，可是使用with as代码块管理和释放
    data = response.read()  # 读取数据，为字节序列数据
    json_data = data.decode()  # 将字节序列数据转换为字符串

    py_dict = json.load(json_data)  # 解码json字符串，返回字典
    record_array = py_dict['Record']  # 获取备忘录数组

    for record_obj in record_array:
        print('--------备忘录信息--------')
        print('备忘录ID:', record_obj['ID'])
        print('备忘录日期:', record_obj['CDate'])
        print('备忘录内容:', record_obj['Content'])
        print('用户ID:', record_obj['UserID'])

# **********************************************************************************
# 数据库SQLite
# 无条件查询，无WHERE子句
import sqlite3  # 导入sqlite3模块
import os

# 数据库文件路径
db_path = r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db'

# 检查文件是否存在
if not os.path.exists(db_path):
    print(f"数据库文件 {db_path} 不存在！")

try:
    # 连接到SQLite数据库
    con = sqlite3.connect(r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db')

    # 创建一个Cursor对象，用于执行SQL命令
    cursor = con.cursor()

    # 执行SQL查询操作
    sql = 'SELECT s_id, s_name, s_sex, s_birthday FROM student'
    cursor.execute(sql)  # 执行SQL命令

    # 提取结果集
    result_set = cursor.fetchall()
    for row in result_set:
        print('学号：{0} - 姓名：{1} - 性别：{2} - 生日：{3}'.format(row[0], row[1], row[2], row[3]))

except sqlite3.Error as e:
    print('数据库查询发生错误:{}'.format(e))

finally:
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭数据库连接
    if con:
        con.close()

# 有条件查询，有WHERE子句，WHERE自己是查询条件
import sqlite3  # 导入sqlite3模块
import os

# 数据库文件路径
db_path = r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db'

# 检查文件是否存在
if not os.path.exists(db_path):
    print(f"数据库文件 {db_path} 不存在！")

istr = input('请输入生日（YYYYMMDD）:')  # 获取用户输入的生日

try:
    # 连接到SQLite数据库
    con = sqlite3.connect(r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db')

    # 创建一个Cursor对象，用于执行SQL命令
    cursor = con.cursor()

    # 执行SQL查询操作
    sql = 'SELECT s_id, s_name, s_sex, s_birthday FROM student WHERE s_birthday < ?'  # 查询学生信息
    cursor.execute(sql, [istr])  # 执行SQL命令,参数放到序列或元组中

    # 提取结果集
    result_set = cursor.fetchall()
    for row in result_set:
        print('学号：{0} - 姓名：{1} - 性别：{2} - 生日：{3}'.format(row[0], row[1], row[2], row[3]))

except sqlite3.Error as e:
    print('数据库查询发生错误:{}'.format(e))

finally:
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭数据库连接
    if con:
        con.close()

# 插入数据
import sqlite3  # 导入sqlite3模块
import os

# 数据库文件路径
db_path = r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db'

# 检查文件是否存在
if not os.path.exists(db_path):
    print(f"数据库文件 {db_path} 不存在！")
i_name = input('请输入姓名:')  # 获取用户输入的姓名
i_sex = input('请输入性别(1表示男，0表示女):')  # 获取用户输入的性别
i_birthday = input('请输入生日（YYYYMMDD）:')  # 获取用户输入的生日

try:
    # 连接到SQLite数据库
    con = sqlite3.connect(r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db')

    # 创建一个Cursor对象，用于执行SQL命令
    cursor = con.cursor()

    # 执行SQL查询操作
    sql = 'INSERT INTO  student(s_name, s_sex, s_birthday) VALUES (?, ?, ?)'
    cursor.execute(sql, [i_name, i_sex, i_birthday])  # 执行SQL命令,参数放到序列或元组中

    # 提取数据库事务
    con.commit()
    print('插入成功！')

except sqlite3.Error as e:
    print('插入数据失败:{}'.format(e))

    # 回滚数据库事务
    con.rollback()

finally:
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭数据库连接
    if con:
        con.close()

# 更新数据
import sqlite3  # 导入sqlite3模块
import os

# 数据库文件路径
db_path = r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db'

# 检查文件是否存在
if not os.path.exists(db_path):
    print(f"数据库文件 {db_path} 不存在！")
i_id = input('请输入学号:')  # 获取用户输入的学号
i_name = input('请输入姓名:')  # 获取用户输入的姓名
i_sex = input('请输入性别(1表示男，0表示女):')  # 获取用户输入的性别
i_birthday = input('请输入生日（YYYYMMDD）:')  # 获取用户输入的生日

try:
    # 连接到SQLite数据库
    con = sqlite3.connect(r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db')

    # 创建一个Cursor对象，用于执行SQL命令
    cursor = con.cursor()

    # 执行SQL查询操作
    sql = 'UPDATE  student SET s_name=?, s_sex=?, s_birthday=? WHERE s_id=?'
    cursor.execute(sql, [i_name, i_sex, i_birthday, i_id])  # 执行SQL命令,参数放到序列或元组中

    # 提取数据库事务
    con.commit()
    print('更新数据库成功')

except sqlite3.Error as e:
    print('更新数据库失败:{}'.format(e))

    # 回滚数据库事务
    con.rollback()

finally:
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭数据库连接
    if con:
        con.close()

# 删除数据
import sqlite3  # 导入sqlite3模块
import os

# 数据库文件路径
db_path = r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db'

# 检查文件是否存在
if not os.path.exists(db_path):
    print(f"数据库文件 {db_path} 不存在！")
i_id = input('请输入要删除学生的学号:')  # 获取学号

try:
    # 连接到SQLite数据库
    con = sqlite3.connect(r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db')

    # 创建一个Cursor对象，用于执行SQL命令
    cursor = con.cursor()

    # 执行SQL查询操作
    sql = 'DELETE  FROM student  WHERE s_id=?'
    cursor.execute(sql, [i_id])  # 执行SQL命令,参数放到序列或元组中

    # 提取数据库事务
    con.commit()
    print('删除数据成功')

except sqlite3.Error as e:
    print('删除数据失败:{}'.format(e))

    # 回滚数据库事务
    con.rollback()

finally:
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭数据库连接
    if con:
        con.close()

# 防止SQL攻击
import sqlite3  # 导入sqlite3模块
import os

# 数据库文件路径
db_path = r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db'

# 检查文件是否存在
if not os.path.exists(db_path):
    print(f"数据库文件 {db_path} 不存在！")

istr = input('请输入生日（YYYYMMDD）:')  # 获取用户输入的生日

try:
    # 连接到SQLite数据库
    con = sqlite3.connect(r'D:\桌面文件\DB\新建数据库的相关文件\school_db.db')

    # 创建一个Cursor对象，用于执行SQL命令
    cursor = con.cursor()

    # 执行SQL查询操作
#    sql = 'SELECT s_id, s_name, s_sex, s_birthday FROM student WHERE s_birthday < ?'  # 查询学生信息
#    cursor.execute(sql, [istr])  # 执行SQL命令,参数放到序列或元组中
    sql = 'SELECT s_id, s_name, s_sex, s_birthday FROM student WHERE s_birthday < ' + istr  # 查询学生信息，这种方式容易造成，SQL注入攻击
    cursor.execute(sql)  # 执行SQL命令,参数放到序列或元组中

    # 提取结果集
    result_set = cursor.fetchall()
    for row in result_set:
        print('学号：{0} - 姓名：{1} - 性别：{2} - 生日：{3}'.format(row[0], row[1], row[2], row[3]))

except sqlite3.Error as e:
    print('数据库查询发生错误:{}'.format(e))

finally:
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭数据库连接
    if con:
        con.close()
