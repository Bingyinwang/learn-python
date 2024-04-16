# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/9  15:51

# 常用的内置模块
# 1，数字计算模块 math
# 在math模块中包含数学相关的函数等，例如指数，对数，平方根和三角函数等
'''math模块中常用函数：
ceil(x),返回大于或等于x的最小整数
floor(x),返回小于或等于x的最大整数
sqrt(x),返回x的平方根
pow(x),返回x的y次幂的值
math,log(x[,base]),返回以base为底的x的对数，若省略底数base，则计算x自然对数
sin(x),返回弧度x的三角正弦
degrees(x),将弧度x转换为角度
radians(x),将角度x转换为弧度
'''
# 例：
import math

p = math.sin(0.5 * math.pi)
print(p)
p1 = math.ceil(2.4)
p2 = math.floor(2.4)
p3 = math.ceil(-2.4)
p4 = math.floor(-2.4)
print(p1)
print(p2)
print(p3)
print(p4)

p5 = math.sqrt(49)
print(p5)

p6 = math.pow(2, 10)
print(p6)

p7 = math.log(125, 5)
print(p7)

p8 = math.degrees(0.5 * math.pi)
print(p8)

p9 = math.radians(360 / math.pi)
print(p9)

# 2,日期时间模块---datetime
# datetime: 包含时间和日期
# date：只包含日期
# time：只包含时间
# timedelta：计算时间跨度
# tzinfo：时区信息
# 创建datetime对象
# datetime.datetime(year , mouth , day , hour = 0 , minute = 0 , microsecond = 0 , tzinfo = None)
'''
year 年，不可以省略
month 月，不可以省略  (1 <= month <= 12)
day   日，不可以省略  （1 <= day <= 给定年份和月份，这时该月的最大天数）
hour 小时，可以省略   (0 <= month <= 24)
minute 分钟， 可以省略 (0 <= month <= 60)
second，秒，可以省略   (0 <= month <= 60)
microsecond 微秒，可以省略 (0 <= month <= 1000000)
tzinfo 时区 
'''
import datetime
# 例子：
d = datetime.datetime(2024, 2, 15)
print(d)

import datetime

a = datetime.datetime.today()  # 返回当前时间
print(a)
a1 = datetime.datetime.now()  # 返回当前时间，可指定时区
print(a1)
a2 = datetime.datetime.fromtimestamp(999999999.999)  # 返回与UNIX时间戳对应的本地日期和时间，UNIX时间戳是从1970年1月1日00:00:00开始到现在的秒数
print(a2)

a3 = datetime.date(2024, 1, 29)
print(a3)

a4 = datetime.date.today()
print(a4)

a5 = datetime.date.fromtimestamp(9999999999.999)
print(a5)

a6 = datetime.time(23, 59, 59, 1999)
print(a6)

# 计算时间跨度（timedelta）
# 参数：day（天），second（秒），microsecond（微秒），milliseconds（毫秒），minute（分钟），hour（小时），weeks（周）
c = datetime.date.today()
c_10days = datetime.timedelta(10)  # 创建10天后的timedelta对象
c += c_10days  # 当前日期+10天
print(c)

c1 = datetime.datetime(2024, 4, 9)
c1_10days = datetime.timedelta(weeks=5)  # 创建5周后的timedelta对象
c1 -= c1_10days
# 下面两行可以代替上面两行，结果是一样的（正负号更换位置）
# c1_10days = datetime.timedelta(weeks = -5)
# c1 += c1_10days
print(c1)

# 日期时间与字符串相互转换
# 日期时间转换为字符串，称为日期时间格式化，python中使用strftime(format)
# 字符串转换为日期时间，称为日期时间解析，python使用datetime.strptime(date_string,format)
'''常用的日期和时间格式控制符：
%m 两位月份表示                    01,02,12
%y 两位年份表示                    08,18
%Y 四位年份表示                    2008,2018
%d 两位表示月中的一天               01,02,03
%H 两位小时表示（24小时制）          00,01,23
%l 两位小时表示（12小时制）          01,02,12
%p AM或PM区域性设置                 AM和PM
%M 两位分钟表示                     00,01,59
%S 两位秒表示                      00，01，59
%f 以6位数表示微秒                 000000,000001，...999999
%z +HHMM或-HHMM形式的UTC偏移       +0000，-0400，+1030，如果没有设置时区，则为空
%Z 时区名称                        UTC，EST，CST，如果没有设置时区，则为空
'''
# 例子
k = datetime.datetime.today()
k_s = k.strftime('%Y-%m-%d %H:%M:%S')  # 日期时间转化为字符串
print(f'{k_s}')

k1 = datetime.time()
k1_s = k1.strftime('%H:%M:%S')
print(k1_s)

k2 = '2024-03-15 10:34:59'
k2_s = datetime.datetime.strptime(k2, '%Y-%m-%d %H:%M:%S')  # 字符串转化日期时间，提供的字符串必须是正确的，否则会报错
print(k2_s)

# 3，正则表达式模块----------re
# 正则表达式指的是预先定义好一个“字符串模板“，通过这个“字符串模板”可以匹配，查找和替换那些匹配”字符串模板“的字符串
# 3.1 字符串匹配match(p,text),p是正则表达式，即字母串模板，text是要验证字符串
import re


p = r'\w+@wby\.com'  # \w+ 匹配一个或多个单词字符（字母、数字或下划线） [a-zA-Z0-9_]
email1 = '123@wby.com'
m1 = re.match(p, email1)
email2 = 'zhangjie@163.com'
m2 = re.match(p, email2)
print(type(m1))
print(m1)
print(type(m2))
print(m2)

# 3.2 字符串查找search(p,text)，查询匹配的内容，有，返回一个，没有返回None。findall(p,text)，查询所有匹配的内容，有，返回所有，没有，返回None
import re


p = r'Java|java|JAVA'
text = 'I like Java and java and JAVA'
match_list = re.findall(p, text)
print(match_list)

# 3.3 字符串替换sub()
# re.sub(pattern,repl,string,count=0)
# 参数pattern是正则表达式，参数repl是用于替换的新字符串，参数string是即将被替换的旧字符串，参数count是要替换的最大数量，默认值为0，表示不限制替换数量
import re


p = r'\d+'
text = 'AC123MBN097NJIVDI'
repace_text1 = re.sub(p, ' ', text)
print(repace_text1)
repace_text2 = re.sub(p, ' ', text, count=1)
print(repace_text2)
repace_text3 = re.sub(p, ' ', text, count=2)
print(repace_text3)

# 3.4 字符串分割 re.split()函数进行字符串分割，返回的是字符串列表对象
# re.split(pattern,string,maxsplit=0)
# 参数pattern是正则表达式，参数string是要分割的字符串，参数maxsplit是最大分割次数，默认值为0，表示分割次数没有限制
import re


p = r'\d+'
text = 'AC123MBN097NJIVDI'
clist = re.split(p, text)
print(clist)
clist1 = re.split(p, text, maxsplit=1)
print(clist1)
clist2 = re.split(p, text, maxsplit=2)
print(clist2)

