# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/7  13:38

# 学习重点部分
# 类(class)与对象
# 1，定义类
# 语法：  class 类名(父类):
#              类体
# 在python中任何一个类，除了父类外，都直接或间接继承父类，直接继承父类时，部分代码可以省略
# pass语句只用于维持程序结构的完整，我们在编程时若不想马上编写某些代码，又不想有语法错误，就可以使用pass语句占位

# 2，创建对象
# 类相当于一个模板，依据模板来创建对象，就是类的实例化，所以对象也称“实例”
class Car(object):
    pass


car = Car()  # 创建对象


# 3,类的成员
# 成员变量（数据成员）：保存了类与对象的数据------（实例变量，类变量）
# 构造方法：是一种特殊的函数，用于初始化类的成员变量
# 成员方法: 在类中定义的函数-------（实例方法，类方法）
# 属性：对类进行封装而提供的特殊方法
# 实例变量，实例方法属于对象，通过对象调用。 类变量，类方法属于类，通过类调用
# __init__()方法是构造方法，用来初始化实例变量
class Dog:
    def __init__(self, name, age):
        self.name = name  # 创建和初始化实例变量name
        self.age = age  # 创建和初始化实例变量age


d = Dog('球球', 2)  # 创建对象调用构造方法
print('我家狗狗的名叫{0}，{1}岁了'.format(d.name, d.age))  # 对实例变量通过‘对象.实例变量’形式访问


# 类中的self表示当前对象，构造方法中的self参数说明这个方法属于实例，self.age表示age属于实例，即实例成员变量

class Dog:
    def __init__(self, name, age, sex='雌性'):
        self.name = name
        self.age = age
        self.sex = sex


d1 = Dog('球球', 2)
d2 = Dog('旺财', 3, '雄性')
d3 = Dog(name='大黄', sex='雄性', age=1)  # 使用关键字参数调用构造方法

print('狗狗的名叫{0}，{1}岁了,是{2}'.format(d1.name, d1.age, d1.sex))
print('狗狗的名叫{0}，{1}岁了,是{2}'.format(d2.name, d2.age, d2.sex))
print('狗狗的名叫{0}，{1}岁了,是{2}'.format(d3.name, d3.age, d3.sex))


# 实例方法
class Dog:
    # 构造方法
    def __init__(self, name, age, sex='雌性'):
        self.name = name
        self.age = age
        self.sex = sex

    # 实例方法1
    def run(self):
        print('{}在跑...'.format(self.name))

    # 实例方法2
    def speak(self, sound):
        print('{}在叫，"{}"!'.format(self.name, sound))


dog = Dog('球球', 2)  # 创建对象调用构造方法
dog.run()  # 在调用时采用‘对象.实例方法’形式，不需要传递参数
dog.speak('汪，汪，汪')  # 需要传递一个参数sound


# 类变量
class Account:
    interset_rate = 0.0568  # 类变量 利率interest_rate

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount


account = Account('WBY', 9999999999999.0)
print('账户名：{0}'.format(account.owner))
print('账户金额：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interset_rate))  # 对类变量通过‘类名.类变量’形式访问


# 类方法，定义类方法时，第一个参数不是self，而是类本身
class Account:
    interset_rate = 0.0568  # 类变量 利率interest_rate

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    # 类方法
    @classmethod  # 定义类方法需要的装饰器，装饰器以@为开头，修饰函数，方法和类，用来约束他们
    def interest_by(cls, amt):  # cls 代表类自身，即Account类
        return cls.interset_rate * amt  # cls可以直接使用Account替换，所以cls.interset_rate表达式可以改为Account.interset_rate


interest = Account.interest_by(12000.0)  # 对类方法可以通过‘类名.类方法’形式访问
print('计算利息：{0:.4f}'.format(interest))


# 注：类方法可以访问类变量和其他类方法，但不能访问其他实例方法和实例变量

# 4，封装性：封装性是面对对象重要的基本特征之一。封装隐藏了对象的内部细节，，只保留了有限的对外接口，外部调用者不用关心对象的内部细节，使得操作对象变得简单
# 私有变量：为了防止外部调用者随意存取类的内部数据（成员变量），内部数据（成员变量）会被封装为私有变量。外部调用者只能通过方法调用私有变量

# 变为私有变量是，在变量前加上双下划线 __ 即可。
class Account:
    __interset_rate = 0.0568  # 私有类变量 利率interest_rate

    def __init__(self, owner, amount):
        self.owner = owner  # 创建并初始化公有实例变量
        self.__amount = amount  # 创建并初始化私有实例变量

    def desc(self):  # 在类的内部可以访问私有变量
        print('{0} 金额：{1} 利率：{2}'.format(self.owner, self.__amount, self.__interset_rate))


account = Account('WBY', 9999999999999.0)
account.desc()
print('账户名：{0}'.format(account.owner))


# print('账户金额：{0}'.format(account.__amount))
# print('利率：{0}'.format(Account.__interset_rate)) # 在类的外部不可以访问私有变量

# 变为私有方法是，在方法前加上双下划线 __ 即可
class Account:
    __interset_rate = 0.0568  # 私有类变量 利率interest_rate

    def __init__(self, owner, amount):
        self.owner = owner  # 创建并初始化公有实例变量
        self.__amount = amount  # 创建并初始化私有实例变量

    def __get_info(self):  # 定义私有方法
        return '{0} 金额：{1} 利率：{2}'.format(self.owner, self.__amount, self.__interset_rate)

    def desc(self):  # 在类的内部可以调用私有方法
        print(self.__get_info())


account = Account('WBY', 9999999999999.0)
account.desc()


# account.__get_info()     # 在类的外部调用私有方法，会发生错误

# 使用属性，为了实现对象的封装，在一个类中不应该有公有的成员变量，这些成员变量应该被设计为私有的，然后通过公有的set(赋值)和get(取值)方法访问
class Dog:
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 实例方法
    def run(self):
        print('{}在跑...'.format(self.name))

    # get方法
    def get_age(self):
        return self.__age

    # set方法
    def set_age(self, age):
        self.__age = age


dog = Dog('球球', 2)  # 创建对象调用构造方法
print('狗狗年龄：{}'.format(dog.get_age()))
dog.set_age(3)
print('修改后狗狗年龄：{}'.format(dog.get_age()))


# 使用属性方式修改上个代码
class Dog:
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 实例方法
    def run(self):
        print('{}在跑...'.format(self.name))

    @property  # 使用@property装饰器修饰，方法名就是属性名，即age
    def age(self):  # age(self)代替get_age(self)
        return self.__age

    @age.setter  # 使用@age.setter装饰器修饰，age是属性名
    def age(self, age):  # age(self, age)代替set_age(self, age)
        self.__age = age


dog = Dog('球球', 2)  # 创建对象调用构造方法
print('狗狗年龄：{}'.format(dog.age))  # 可以通过属性取值，访问形式为‘实例.属性’
dog.age = 3  # 可以通过属性赋值，访问形式为‘实例.属性’
print('修改后狗狗年龄：{}'.format(dog.age))


# 5,继承性
# 子类继承父类
class Animal:  # 定义父类

    def __init__(self, name):
        self.name = name

    def show_info(self):
        return '动物的名字：{0}'.format(self.name)

    def move(self):
        print('动一动。。。')


class Cat(Animal):  # 定义子类
    def __init__(self, name, age):
        super().__init__(name)  # 调用父类构造方法，初始化父类成员变量
        self.age = age


cat = Cat('旺财', 3)
cat.move()
print(cat.show_info())


# 注：子类继承父类时，只有那些公有的成员变量和方法才可以被继承
# 在继承多个父类时，若有相同的成员方法或成员变量，优先继承左边，从左至右，继承级别从高到低
class Horse:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return '马的名字：{0}'.format(self.name)

    def run(self):
        print('赤兔骏马，跑得贼快')


class Donkey:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return '驴的名字：{0}'.format(self.name)

    def run(self):
        print('小飞马，驾驾驾')

    def roll(self):
        print('驴打滚。。。。。。。。')

    def s_s(self):
        return '名：{0}'.format(self.name)


class Mule(Horse, Donkey):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def s_s(self):  # 方法重写，子类方法名和父类方法名相同，则在这种情况下，子类方法会重写（Override）父类的同名方法
        return '名：{0}, 年龄：{1}岁'.format(self.name, self.age)


m = Mule('骡儿', 3)
m.run()  # 继承父类Horse的方法
m.roll()  # 继承父类Donkey的方法
print(m.show_info())  # 继承父类Horse的方法
print(m.s_s())  # 子类Mule自己的方法


# 6，多态性，指的是对象可以表现出多种形态
# 继承与多态，在多个子类继承父类，并重写父类方法后，这些子类所创建的对象之间就是多态的，这些对象采用不同的方式实现父类的方法
class Animal:
    def speak(self):
        print('动物叫，但不知道是哪种动物叫')


class Dog(Animal):
    def speak(self):
        print('小狗：汪汪叫...')


class Cat(Animal):
    def speak(self):
        print('小猫：喵喵叫...')


an1 = Dog()
an2 = Cat()
an1.speak()
an2.speak()

print('**********************************************************')


# 鸭子类型测试与多态
def start(obj):
    obj.speak()


class Animal:
    def speak(self):
        print('动物叫，但不知道是哪种动物叫')


class Dog(Animal):
    def speak(self):
        print('小狗：汪汪叫...')


class Cat(Animal):
    def speak(self):
        print('小猫：喵喵叫...')


class Yoo:
    def speak(self):
        print('大黄：嗷嗷叫...')


start(Dog())
start(Cat())
start(Yoo())





