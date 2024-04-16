# 开发人：wby
# 类型：python
# 开发时间：2024/3/28  14:30
# 1，变量，赋值 例，a=12

# 2，print()   打印

# file = open('D:/桌面文件/file.txt','w')       #在桌面上打开file.txt文件，如果没有这个文件，自动创建一个
# file.write('hello,world!')                  #并写入内容“hello，world！”

# 3，字符串，双引号和单引号之间的文字
# 字符串基本用法
# 例：
# who_name = 'YY'
# what = ' plays '
# do = 'guitar'
# art_in = who_name + what + do
# print(art_in)

# num = 1
# string ='1'
# print(num+string) #不同变量类型不能进行合并

# num1 = 1
# string = '1'
# num2 = int(string)
# print(num1 + num2)  # 转换成相同类型，可以合并

# print(type())     # 查看变量类型

# words = 'words '*3  # 字符串相乘
# print(words)

# word = 'a loooooong word'
# num = 12
# string = 'bang!'
# total = string*(len(word) - num)
# print(total)                       # 字符串计算

# 字符串通过string[x]的方式进行索引，分片
# 例：
# name = 'My name is YYDS'
# print(name[0])   # 结果为 M 第一个
# print(name[-4])  # 结果为 Y 倒数第四个
# print(name[11:15])  # 结果为 YYDS
# print(name[5:])     # 结果为 me is YYDS
# print(name[:5])     # 结果为 My na     : 两边代表着字符串的分割，从哪里开始，到哪里结束

# 文字小游戏，找到朋友中的魔鬼
# word = 'friends'
# find = word[0] + word[2:4] + word[-3:-1]
# print(find)

# 实际操作中的分片操作
# 找到一个图片网址
# url = 'http://wwx.site.cn/dcjsodvhjosddvjasdjdohcjfosdj.png'  # 只是例子，非真实网址，瞎写的
# file_name = url[-10:]
# print(file_name)       #打印结果为 jfosdj.png

# 字符串方法
# 隐藏号码相关信息
# phone_number = '1386-666-0006'
# hiding_number = phone_number.replace(phone_number[:9],'*'*9)
# print(hiding_number)  # 打印结果为 *********0006

# 字符串格式化符  .format()进行批处理
# city = input("写下城市名字：")
# url = "http://apis.baidu.com/microservice/weather?citypinyin={}".format(city)







