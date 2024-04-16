# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/11  16:00
# 文件读写
# 1，打开文件
# open()函数实现，open(file, mode='r', encoding=None, errors=None)
"""
file参数表示要打开的文件，可以是字符串或整数，若是字符串，则表示文件名，文件名既可以是当前目录的相对路径，也可以是绝对路径，若是整数，则表示是一个已经打开的文件

mode参数是设置文件打开模式，用字符串表示
t：以文本文件模式打开文件
b：以二进制文件模式打开文件
r：以只读模式打开文件
w：以只写模式打开文件，不能读文件，如果文件不存在，则创建文件，如果文件存在，则覆盖其内容
x：以独占创建模式打开文件，如果文件不存在，则创建并以写入模式打开，如果文件存在，则引发FileExistsError异常
a：以追加模式打开文件，不能读内容，如果文件不存在，则创建文件，如果文件存在，则在文件末尾追加
+：以更新（读写）模式打开文件，必须与r，w或a组合使用，才能设置文件为读写模式
这些字符可以组合：
字符串               说明
rt或r               以只读模式打开文本文件
wt或w               以只写模式打开文本文件
xt或x               以独占创建模式打开文本文件
at或a               以追加模式打开文本文件
rb                  二进制文件模式，类似于rt
wb                  二进制文件模式，类似于wt
xb                  二进制文件模式，类似于xt
ab                  二进制文件模式，类似于at
r+                  以读写模式打开文本文件，如果文件不存在，则抛出异常
w+                  以读写模式打开文本文件，如果文件不存在，则创建文件
a+                  以读追加文本文件模式打开文件，不能读内容，如果文件不存在，则创建文件
rb+                 二进制文件模式，类似于r+
wb+                 二进制文件模式，类似于w+
ab+                 二进制文件模式，类似于a+

encoding参数用来指定打开文件时文件编码，默认是UTF-8编码，主要用于打开文本文件

errors参数用来指定文本文件发生编码错误时如何处理。推荐errors参数值为‘ignore’，表示遇到编码错误时忽略该错误，程序继续执行
"""

# 示例：
f = open('text.txt', 'w+')
f.write('hello,world')
print('1,创建文件，写入文件')

f = open('text.txt', 'r+')
f.write('money')
print('2,创建文件，覆盖文件内容')

f = open('text.txt', 'a')
f.write(' ')
print('3,创建文件，在文件尾部追加空格')

fname = 'D:/桌面文件/text.txt'
f = open(fname, 'a+')
f.write('王秉崟')
print('4,创建文件，在文件尾部追加王秉崟')

# 2，关闭文件
# 打开文件后，不再使用该文件，将其关闭会用到close()方法
# close()方法接收一个文件对象作为参数，表示要关闭的文件
# 在finally语句块中调用close()方法，确保文件被关闭
# 示例：
f_name = 'text.txt'
f = None
try:
    f = open(f_name)
    print('文件打开成功')
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print('文件不存在,请先创建文件')
except OSError as e:
    print('处理OSError异常')
finally:
    if f is not None:
        f.close()
        print('文件已关闭')

# 在with as代码块中关闭文件
# 使用with as自动管理资源
# 示例：
f_name = 'text.txt'
with open(f_name) as f:
    content = f.read()
    print(content)

# 3，读写文本文件
# 读写文本文件，需要用到read()和write()方法
# read(size=-1):从文件中读取字符串，size参数表示要读取的字符数，如果size为-1，则表示读取的字符数没有限制
# readline(size=-1):在读取到换行符或文件尾时返回单行字符串，如果已经到文件尾，则返回一个空字符串，size参数表示要读取的字符数，如果size为-1，则表示读取的字符数没有限制
# readlines(): 读取文件数据到一个字符串列表中，每一行数据都是列表的一个元素
# write(s): 将字符串s写入文件，并返回写入的字符数
# writelines(lines): 向文件中写入一个字符串列表。不添加行分隔符，因此通常为每一行末尾都提供行分隔符
# flush(): 刷新写缓冲区，将缓冲区中的数据写入文件

# 示例：
f_name = 'src_file.txt'
with open(f_name, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    copy_f_name = 'dest_file.txt'
    with open(copy_f_name, 'w', encoding='gbk') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')


# 4，读写二进制文件
# 读写二进制文件，需要用到read()和write()方法
# read(size=-1):从文件中读取二进制数据（字节），size参数表示要读取的字节数，如果size为-1，则表示读取的字节数没有限制
# readline(size=-1):从文件中读取并返回一行。size参数表示限制读取的行数，如果size为-1，则表示读取的字节数没有限制
# readlines(): 读取文件数据到一个字节字符串列表中，每一行数据都是列表的一个元素
# write(b): 写入b字节，并返回写入的字节数
# writelines(lines): 向文件中写入一个字节字符串列表。不添加行分隔符，因此通常为每一行末尾都提供行分隔符
# flush(): 刷新写缓冲区，将缓冲区中的数据写入文件

# 示例：
f_name = '动漫人物1.jpg'
with open(f_name, 'rb') as f:
    b = f.read()
    copy_f_name = '动漫人物2.jpg'
    with open(copy_f_name, 'wb') as copy_f:
        copy_f.write(b)
        print('文件复制成功')
