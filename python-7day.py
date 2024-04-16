# 开发人：wby
# 类型：python
# 开发时间：2024/4/3  17:58

# python中有四种数据结构，列表，字典，元组，集合
# 列表（list）: list = [val1,val2,val3,val4]
# 字典（dict）: dict = {key1:val1,key2:val2}
# 元组（tuple）: tuple = (val1,val2,val3,val4)
# 集合（set）: set = {val1,val2,val3,val4}

# 1，列表
# 列表中的每一个元素都是可变的，（添加，修改，删除）
# 列表中的元素是有序的，也就是说每一个元素都有一个位置
# 列表可以容纳Python中的任何对象
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekday[0])
all_in_list = [1, 1.0, 'a word', print(1), True, [1, 2],   (1, 2), {'key': 'value'}]
#             整数，浮点数，字符串，  函数，  布尔值, 列表中套列表, 元组          字典
# 插入元素:insert  添加多元素：extend 或 使用运算符：+=
fruit = ['apple', 'pear']
fruit.insert(1, 'grape')
print(fruit)

fruit[0:0] = ['Orange']
print(fruit)

# 删除元素：remove
fruit.remove('apple')
print(fruit)

# 修改元素
fruit[0] = 'Orangefruit'
print(fruit)

# 还有一种办法删除：del关键字
del fruit[0:2]
print(fruit)
# 列表的索引和字符串的索引是一样的

# 2，字典
# 字典中数据必须是以键值对的形式出现的
# 逻辑上讲，键是不能重复的，而值可以重复
# 字典中的键（key）是不可变的，也是无法修改的；而值（value）是可变的，可修改的，可以是任何对象
code = {'BD': 'BaiDu','AQY': 'AiQiYi','YK':'YouKu'}
print(code)
# 字典中的键值不会有重复,只会生效一次
a = {'wby':123,'wby':123}
print(a)

# 字典的增删改查
# 添加元素
code['CN'] = 'China'
print(code)

# 字典添加多元素：update
code.update({'w':'wang','b':'bing','y':'yin'})
print(code)

# 删除也是使用del
del code['w']
print(code)

# 字典是不能够切片的
# 访问字典视图，三种方法
# item(),返回字典的所有的键值对视图
# keys(),返回字典键视图
# values(),返回字典值视图


# 3，元组（Tuple）
# 元组不可修改，但是可以被查看索引
letters = ('a','b','c','d','e','f','g')
print(letters[0])
print(letters[3])

# 4,集合（Set）
# 集合可以做运算，添加和删除，不能被切片也不能索引
a_set = {1,2,3,4,5}
a_set.add(6)             # 添加
a_set.discard(3)         # 删除，还可以用remove
a_set.clear()            # 清除集合
print(a_set)

# 5,数据结构中的一些技巧
# 多重循环
num_list = [5,3,2,6,9,1,7]
# print(sorted(num_list))  # 正序
print(sorted(num_list,reverse=True))   # 逆序

# 需要两个列表时，用到zip函数
# for a, b in zip(num_list, str):
# print(b, 'is', a)

# 推导式（列表中的解析式）
import time

q = []
t0 = time.perf_counter()
for i in range(1, 20000):
    q.append(i)
print(time.perf_counter() - t0, 'seconds process time')

t0 = time.perf_counter()
b = [i for i in range(1, 20000)]
print(time.perf_counter() - t0, 'seconds process time')

m1 = [i**1 for i in range(1, 10)]
n1 = [j+1 for j in range(1, 10)]
k1 = [n for n in range(1,10) if n % 2 == 0]

m2 = {i:i+1 for i in range(4)}
n2 = {i:j for i,j in zip(range(1,6),'abcde')}
k2 = {i:j.upper() for i,j in zip(range(1,6),'abcde')}

print(m1)
print(n1)
print(k1)
print(m2)
print(n2)
print(k2)

letter = ['a','b','c','d','e','f','g']
for num,letter in enumerate(letter):
    print(letter,'is',num + 1)

# 综合项目 ：词频统计
import string

path = "D:\桌面文件\Walden.txt"
with open(path,'r',encoding='utf-8') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}


for words in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
        print('{}-{} times'.format(words,counts_dict[words]))





























































