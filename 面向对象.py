# 初识对象
# 使用字符串、列表、字典等数据容器来管理数据往往会造成组织的混乱与不统一
# 使用对象组织数据
# 这种方法就像生活中发放统一的表进行填写，从而提高数据组织的效率
# 在程序中设计表格，我们称之为：设置类（class）
# class Student:
#     name = None
#     gender = None
#     nationality = None
#     native_place = None
#     age = None
#


# 在程序中打印生产表格，我们称之为：创建对象
# 基于类创建对象
# stu_1 = Student()
# 在程序中填写表格，我们称之为：对象属性赋值
# stu_1.name = "林军杰"
# stu_1.gender = "男"
# stu_1.nationality = "中国"
# stu_1.native_place = "山东省"
# stu_1.age = 31
# print(stu_1.name)
# print(stu_1.gender)
# print(stu_1.nationality)
# print(stu_1.native_place)
# print(stu_1.age)

# 类的成员方法
# class是关键字，表示要定义类了
# 类的属性，即定义在类中的变量（成员变量）
# 类的行为，及定义在类中的函数（成员方法）
# 类中的内容就分为两种：属性（成员变量），行为（成员方法）
# 创建类对象的语法：对象 = 类名称()
# 成员方法的定义语法
# def 方法名(self, 形参1, ......, 形参N):
#     方法体
# self关键字是成员方法定义的时候，必须填写的
# self关键字用来表示类对象自身的意思
# 当我们使用类对象调用方法时，self会自动被传入
# 在方法内部，想要访问类的成员变量，必须使用self
# 在传入参数时，可以当self不存在
# class Student:
#     name = None
#     age = None
#     def say_hi(self):
#         print(f"Hi大家好，我是{self.name}")
#
#
# stu_1 = Student()
# stu_1.name = "周杰轮"
# stu_1.say_hi()

# 类和对象
# 现实生活中无论是事还是物，都具有相应的属性和行为
# 虽然程序中的类已经能够完美表现现实中的事物，但类只是一种程序内的“设计图纸”，需要基于图纸生产实体（对象），才能正常工作
# 这种编程思想，称之为：面向对象编程
# 面向对象编程：设计类，基于类创建对象，由对象做具体的工作
# 设计一个闹钟类
# class Clock:
#     id = None  # 序列化
#     price = None  # 价格
#
#
#     def ring(self):
#         import winsound
#         winsound.Beep(2000, 3000)  # 2000指声音频率，3000指持续时间(ms)
#
#
# clock1 = Clock()
# clock1.id = "003032"
# clock1.price = 19.99
# print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
# clock1.ring()
#
# clock2 = Clock()
# clock2.id = "003033"
# clock2.price = 21.9
# print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
# clock2.ring()

# 构造方法
# 属性（成员变量）的赋值
# Python类可以使用：__init__()，称之为构造方法
# __init__()可以实现：在创建类对象（构造类）的时候，会自动执行（无需自行输入代码）；在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
# class Student:
#     name = None  # 在使用构造方法的情况下，无需提前声明变量
#     age = None
#     tel = None
#
#     def __init__(self, nane, age, tel):
#         self.name = nane
#         self.age = age
#         self.tel = tel
#         print("Student类创建了一个对象")
#
#
# stu = Student("周杰轮", 31, "18500006666")
# print(stu.name)
# print(stu.age)
# print(stu.tel)

# 其他内置方法
# 上文学习的__init__构造方法，是Python类类内置的方法之一
# 这些内置的类方法，各自有各自特殊的功能，这些内置方法我们称之为：魔术方法
# 魔术方法：__init__构造方法；__str__字符串方法；__lt__小于、大于符号比较；__le__小于等于、大于等于符号比较；__eq__==符号比较
# 当我们直接print类对象时，一般都会直接打印出该类对象所在的内存地址
# 内存地址没多大作用，我们可以通过__str__方法，控制转换为字符串的行为
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def __str__(self):
#         return f"Student类对象，name={self.name}，age={self.age}"
#
#
# student = Student("周杰轮", 11)
# print(student)
# print(type(student))
# print(str(student))
# __lt__小于符号比较方法
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def __lt__(self, other):
#         return self.age < other.age  #此处需要写小于号
#
#
# stu1 = Student("周杰轮", 11)
# stu2 = Student("林军杰", 13)
# print(stu1 < stu2)  # 此处大于号，小于号都可以写
# print(stu1 > stu2)
# __le__小于等于比较符号方法
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def __le__(self, other):
#         return self.age <= other.age  #此处需要写小于等于号
#
#
# stu1 = Student("周杰轮", 11)
# stu2 = Student("林军杰", 13)
# print(stu1 <= stu2)  # 此处大于等于号，小于等于号都可以写
# print(stu1 >= stu2)
# __eq__比较运算符实现方法
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#
#
# stu1 = Student("周杰轮", 11)
# stu2 = Student("林军杰", 11)
# print(stu1 == stu2)
# 当__eq__方法不进行实现直接比较的话，比较的将会是内存地址

# 封装
# 面向对象包含三大特征：封装、继承、多态
# 封装表示的是：将现实事物的属性和行为封装到类中并描述为成员变量和成员方法，从而完成程序对现实世界的描述
# 对用户隐藏的属性和行为
# 现实中的事物有属性和行为，但并不代表这些都是对用户开放的
# 而作为显示事物在程序中映射的类，也应该支持
# 类中提供了私有成员来支持：私有成员变量、私有成员方法
# 定义方式：私有成员变量：变量名以__开头；私有成员方法：方法名以__开头
# 私有方法无法直接被类对象使用
# class Phone:
#     IMEI = None
#     producer = None
#     __current_voltage = None
#     def call_by_5g(self):
#         print("5g通话已开启")
#
#
#     def __keep_single_core(self):
#         print("让CPU以单核模式运行以节省电量")
#
#
# phone = Phone()
# phone.__keep_single_core()  # 程序将在此报错
# 私有变量无法赋值，也无法获取值
#
#
# class Phone:
#     IMEI = None
#     producer = None
#     __current_voltage = None
#
#
# def call_by_5g(self):
#         print("5g通话已开启")
#
#
#     def __keep_single_core(self):
#         print("让CPU以单核模式运行以节省电量")
#
#
# phone = Phone()
# phone.__current_voltage = 33  # 不报错，但无效
# print(phone.__current_voltage)  # 程序报错
# 私有成员无法被类对象使用，但是可以被其他的成员使用
# class Phone:
#     __current_voltage = 0.5
#     def __keep_single_core(self):
#         print("让CPU以单核模式运行")
#     def call_by_5g(self):
#         if self.__current_voltage >= 1:
#             print("5g通话已开启")
#         else:
#             self.__keep_single_core()
#             print("电量不足，无法使用5g通话，并以设置为单核模式运行进行省电")
#
#
# phone = Phone()
# phone.call_by_5g()

# 继承的基础语法
# 继承的作用：无需重新定义类，而直接从已有的类中继承相同内容
# 单继承
# class 类名(父类名)
#     类内容体
# class Phone:
#     IMEI = None
#     producer = "HM"
#
#     def call_by_4g(self):
#         print("4g通话")
#
#
# class Phone2022(Phone):
#     face_id = "10001"
#
#     def call_by_5g(self):
#         print("2002年新功能：5g通话")
#
#
# phone = Phone2022()
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()
# 多继承
# class 类名(父类1, 父类2, ......, 父类N):
#     类内容体
# class Phone:
#     IMEI = None
#     producer = "HM"
#
#     def call_by_4g(self):
#         print("4g通话")
#
#
# class NFCReader:
#     nfc_type = "第五代"
#     producer = "HM"
#
#     def read_card(self):
#         print("NFC读卡")
#
#     def write_card(self):
#         print("NFC写卡")
#
#
# class RemoteControl:
#     tc_type = "红外线"
#
#     def control(self):
#         print("红外遥控开启")
#
#
# class MyPhone(Phone, NFCReader, RemoteControl):
#     pass  # 使类仅继承父对象而不再添加新的成员
#
#
# phone = MyPhone()
# phone.call_by_4g()
# phone.read_card()
# phone.write_card()
# phone.control()
# pass关键字能够保证函数（方法）或定义类的完整性，表示无内容、空的意思
# 多继承注意事项：多个父类中，如果有同名的成员，那么默认以继承顺序（从左到右）为优先级
# 即：先继承的保留，后继承的被覆盖

# 复写父类成员和调用父类成员
# 子类继承父类的成员属性和成员方法后，如果对其”不满意“，那么可以进行复写
# 语法：在子类中重新定义同名的属性或方法即可
# class Phone:
#     IMEI = None
#     producer = "ITCAST"
#
#     def call_by_5g(self):
#         print("父类的5g通话")
#
#
# class MyPhone(Phone):
#     producer = "ITHEIMA"
#
#     def call_by_5g(self):
#         print("子类的5g通话")
#
#
# phone = MyPhone()
# phone.call_by_5g()
# print(phone.producer)
# 一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员
# 如果需要使用被复写的父类的成员，需要特殊的调用方式
# 方式一
# 使用成员变量：父类名.成员变量
# 使用成员方法：父类名.成员方法(self)
# 方式二
# 使用成员变量：super().成员变量
# 使用成员方法：super().成员方法()
# class Phone:
#     IMEI = None
#     producer = "ITCAST"
#
#     def call_by_5g(self):
#         print("父类的5g通话")
#
#
# class MyPhone(Phone):
#     producer = "ITHEIMA"
#
#     def call_by_5g(self):
#         print("子类的5g通话")
#         Phone.call_by_5g(self)
#         super().call_by_5g()
#         print(Phone.producer)
#         print(super().producer)
#
#
# phone = MyPhone()
# phone.call_by_5g()
# print(phone.producer)
# 注意：只可以在子类内部调用父类的同名成员，子类的实体类对象调用默认是调用子类复写的

# 变量的类型注解
# 大多数方法在使用的时候，都会提示传参的数据类型，这时候就要通过类型注解来实现了
# 主要功能
# 1、帮助第三方IDE工具对代码类型进行推断，协助做代码提示
# 2、帮助开发者自身对变量进行类型注释
# 支持：变量的类型注解、函数（方法）形参列表和返回值的类型注解
# 为变量设置类型注解
# 基础语法：变量: 类型
# 基础数据类型注解
# var_1: int = 10
# var_2: float = 3.1415926
# var_3: bool = True
# var_4: str = "itheima"
# 类对象类型注解
# class Student:
#     pass
# stu: Student = Student()
# 基础容器类型注解
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_set: set = {1, 2, 3}
# my_dict: dict = {"itheima": 666}
# my_str: str = "itheima"
# 容器类型详细注解
# my_list: list[int] = [1, 2, 3]
# my_tuple: tuple[str, int, bool] = ("itheima", 666, True)
# my_set: set[int] = {1, 2, 3}
# my_dict: dict[str, int] = {"itheima": 666}
# 除了使用变量: 类型这种语法进行注解外，也可以在注释中进行类型注解
## type: 类型
# var_1 = random.randint(1, 10)  # type: int
#
#
# def func():
#     return 10
#
#
# var_2 = func()  # type: int  # 对函数的返回值进行类型注解
# 一般，无法直接看出变量的类型的时候才会添加变量的类型注解
# 类型注解仅仅是提示性的，不是决定性的

# 函数和方法的类型注解
# 形参注解
# def 函数方法名(形参名: 类型, 形参名: 类型, ......):
#     pass
# 返回值注解
# def 函数方法名(形参名: 类型, 形参名: 类型, ......) -> 返回值类型:
#     pass

# Union联合类型注解
# # 当我们遇到需要注解的数据有多种类型时，我们可以使用Union类型注解
# from typing import Union
# my_list: list[Union[str, int]] = [1, 2, "itheima", "itcast"]
# my_dict: dict[str, [str, int]] = {"name": "周杰轮", "age": 31}
# 使用Union[类型, ......, 类型]可以定义联合类型注解
# 同样的，Union联合类型注解也可以在函数（方法）形参和返回值注解中使用

# 多态
# 多态指的是多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
# 同样的行为（函数），传入不同的对象，得到不同的状态
# 多态常作用在继承关系上
# 以父类做定义声明，以子类做实际工作，用以获得同意行为，不同状态
# class Animal:
#     def speak(self):
#         pass
#
#
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
#
#
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")
#
#
# def make_noise(animal: Animal):
#     animal.speak()
#
#
# dog = Dog()
# cat = Cat()
# make_noise(dog)
# make_noise(cat)
# 可以发现，这些子类的父类Animal的speak方法，是空实现
# 这种设计的含义是用父类来确定哪些方法。具体的方法实现，由子类自行决定
# 这种写法，就叫做抽象类（也可以称之为接口）
# 抽象类：含有抽象方法的类称之为抽象类
# 抽象方法：方法体是空实现的（pass）称之为抽象方法
# 抽象类就好比定义了一个标准，包含了一些抽象的方法，要求子类必须实现
