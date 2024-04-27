# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/24
# 小练习

# 1 生成激活码


def GenKey(length):  # 定义生成激活码函数
    chars = string.ascii_letters + string.digits  # 生成所有字母和数字
    return ''.join(random.choice(chars) for i in range(length))


def SaveKey(content):  # 定义保存激活码函数
    f = open("key.txt", 'a')  # 打开文件，以追加模式写入
    f.write(content + "\n")  # 写入激活码
    f.close()  # 关闭文件


if __name__ == '__main__':  # 判断是否是主程序
    for i in range(200):  # 循环200次
        value = GenKey(20)  # 生成20位的激活码
        print(value)  # 输出激活码
        SaveKey(value)  # 保存激活码
# ***************************************************************************************************************
# 2 生成的激活码保存到sqlite3数据库
import sqlite3  # 导入sqlite3模块

# 连接数据库
conn = sqlite3.connect('keys.db')
# 获取游标
c = conn.cursor()


def creat_table():
    # 调用execute方法创建表
    c.execute('CREATE TABLE IF NOT EXISTS keys (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT NOT NULL)')
    # 提交事务
    conn.commit()


def GenKey(length):  # 定义生成激活码函数
    chars = string.ascii_letters + string.digits  # 生成所有字母和数字
    return ''.join(random.choice(chars) for i in range(length))


def SaveKey(content):  # 定义保存激活码函数
    # 使用占位符?来插入内容，这是防止SQL注入的推荐做法
    c.execute("INSERT INTO keys (key) VALUES (?)", (content,))
    # 提交事务
    conn.commit()


if __name__ == '__main__':  # 判断是否是主程序
    creat_table()  # 创建表

    for i in range(200):  # 循环200次
        value = GenKey(20)  # 生成20位的激活码
        print(value)  # 输出激活码
        SaveKey(value)  # 保存激活码

    conn.close()  # 关闭数据库连接
# **************************************************************************************************************
# 3 生成激活码并保存到sqlite3数据库，并生成一个激活码的二维码，生成的二维码保存到keys文件夹下
import sqlite3, qrcode

# 连接数据库
conn = sqlite3.connect('keys.db')
# 获取游标
c = conn.cursor()


def creat_table():
    c.execute('CREATE TABLE IF NOT EXISTS keys (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT NOT NULL)')
    conn.commit()


def GenKey(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))


def SaveKey(content, index):
    c.execute("INSERT INTO keys (key) VALUES (?)", (content,))
    conn.commit()
    # 生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )

    qr.add_data(content)
    qr.make(fit=True)
    # 保存二维码为图片
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("keys/QR-{}.png".format(index))  # 保存到keys文件夹下，文件名包含激活码


if __name__ == '__main__':
    creat_table()

    # 确保keys文件夹存在
    import os

    if not os.path.exists('keys'):
        os.makedirs('keys')

    for i in range(1, 201):
        value = GenKey(20)
        print(value)
        SaveKey(value, i)

    conn.close()
# **************************************************************************************
# 4 生成激活码并保存到mysql数据库
import mysql.connector  # 导入MySQL连接模块


# 定义生成激活码函数
def GenKey(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


# 定义保存激活码函数
def SaveKey(content):
    # 创建数据库连接（可以考虑使用连接池）
    cnx = mysql.connector.connect(user='root', password='******',
                                  host='localhost',
                                  database='mysql')
    cursor = cnx.cursor()

    # 执行SQL语句，插入激活码
    add_key = ("INSERT INTO `keys` (`key_value`) "
               "VALUES (%s)")
    data = (content,)
    cursor.execute(add_key, data)
    cnx.commit()

    # 关闭数据库连接
    cursor.close()
    cnx.close()


if __name__ == '__main__':  # 判断是否是主程序
    # 考虑使用数据库连接池，或者在循环外部创建连接
    cnx = mysql.connector.connect(user='root', password='******',
                                  host='localhost',
                                  database='mysql')
    cursor = cnx.cursor()

    for i in range(200):  # 循环200次
        value = GenKey(20)  # 生成20位的激活码
        print(value)  # 输出激活码
        SaveKey(value)  # 保存激活码

    # 循环结束后关闭数据库连接
    cursor.close()
    cnx.close()
# *********************************************************************************************************
# 5 生成激活码并保存到redis数据库
import redis, random, string


# 生成随机键的函数
def GenKey(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))


# Redis管理类
class RedisManager:
    def __init__(self, host='localhost', port=6379, db=0, password=None):
        self.r = redis.Redis(host=host, port=port, db=db, password=password)

    def save_key(self, key, value):
        # 将布尔值转换为字符串
        if isinstance(value, bool):
            value = str(value).lower()
        try:
            self.r.set(key, value)
            print(f"Key {key} with value {value} saved to Redis successfully.")
        except redis.exceptions.RedisError as e:
            print(f"Error saving key to Redis: {e}")

    def close(self):
        self.r.close()

    # 主程序


if __name__ == '__main__':
    redis_manager = RedisManager(password='******')  # 创建RedisManager实例

    # 尝试保存一些键值对到Redis中
    for _ in range(200):  # 例如，保存10个键值对
        key = GenKey(20)  # 生成一个随机键
        value = bool(random.randint(0, 1))  # 生成一个随机布尔值作为值
        redis_manager.save_key(key, value)  # 调用save_key方法保存键值对

    redis_manager.close()  # 关闭Redis连接

# **************************************************************************************************************
# 6 任一个英文的纯文本文件，统计其中的单词出现的个数。
from collections import Counter   # 导入Counter模块

with open('Walden.txt', encoding='utf-8') as file:
    text = file.read()  # 文件在这里会自动关闭
counts = Counter([len(word.strip('.!?,')) for word in text.split()])  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
word_count = sum(counts.values())  # 计算单词数量

# print('总共的单词数量：%s' % word_count)  # 输出单词数量
# print(f'总共的单词数量：{word_count}')    # 输出单词数量
print('总共的单词数量：{}'.format(word_count))  # 输出单词数量

wordcount = {}
for word in text.split():
    if word not in wordcount:  # 如果字典中没有该单词，则添加进去
        wordcount[word] = 1    # 初始化计数为1
    else:
        wordcount[word] += 1   # 如果字典中已经有该单词，则计数加1

print('单词出现次数：')
print(wordcount)  # 输出字典

# **************************************************************************************************************



















