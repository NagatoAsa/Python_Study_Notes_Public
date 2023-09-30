# 列表
# 字面量
# [元素1,元素2,元素3,元素4,...]
# 定义变量
# 变量名称 = [元素1,元素2,元素3,元素4,...]
# 定义空列表
# 变量名称 = []
# 变量名称 = list()

# 列表的下标索引
# test = [114, 514, 1919, 810]  # 正向索引
# print(test[0])
# print(test[1])
# print(test[2])
# print(test[3])
# print(test[-1])  # 反向索引
# print(test[-2])
# print(test[-3])
# print(test[-4])
# 嵌套列表的索引
# test = [[114, 514], [1919, 810]]
# print(test[0][0])
# print(test[0][1])
# print(test[1][0])
# print(test[1][1])

# 方法
# def add(x,y):  # 函数
#     return x + y
#
#
# num = add(1, 2)
# print(num)
# class Student:
#     def add(self, x, y):
#         return x + y
#
#
# student = Student()
# num = student.add(1, 2)
# print(num)

# 列表的查询功能
# test = [114, 514, 1919, 810]
# print(test.index(114))
# print(test.index(514))
# print(test.index(1919))
# print(test.index(810))
# 列表修改元素（重新赋值）
# test = [114, 514, 1919, 810]
# test[2] = 114
# print(test)
# 列表插入元素
# test = [114, 514, 1919, 810]
# test.insert(1, 514)
# print(test)
# 列表追加元素
# test = [114, 514, 1919, 810]  # 单个追加元素
# test.append(114)
# print(test)
# test1 = [114, 514, 1919, 810]  #追加其他数据容器
# test2 = [514, 114, 810, 1919]
# test1.extend(test2)
# print(test1)
# 列表删除元素
# 通过下标索引
# test = [114, 514, 1919, 810]  # 方法一
# del test[2]
# print(test)
# test = [114, 514, 1919, 810]  # 方法二
# del_element = test.pop(2)  # 该方法能够返回被移出的值
# print(test)
# print(del_element)
# 通过元素索引
# test = [114, 114, 514, 1919, 810]
# test.remove(114)  # remove语句会索引匹配的第一个元素进行删除
# print(test)
# 清空列表
# test = [114, 514, 1919, 810]
# test.clear()
# print(test)
# 统计列表在列表内的数量
# test = [114, 114, 114, 514, 1919, 810]
# print(test.count(114))
# 统计列表内有多少个元素
# test = [114, 514, 1919, 810]
# print(len(test))
# print(len("NagatoAsa"))  # 同样的，len函数也能统计字符串字数

# 元组的定义
# 变量名 = (元素1,元素2,元素3,...)
# 定义空元组
# 变量名 = ()
# 变量名 = tuple()
# 注意当定义的元组只有元素时，该元素的后面要加逗号
# test = ("hello", )
# 元组操作与列表同理
# 元组不可更改，但是元组内的列表可以更改
# test = ([1, 2, 3],[3, 4, 5])
# test[1][2] = 6
# print(test)

# 字符串的定义与操作（字符串也是数据容器）
# 字符串的操作与列表同理，但是字符串是和元组一样无法修改的数据容器
# 字符串的检索
# test = "Hello World!"
# print(test.index("World"))  # 索引结果会显示该字符串的第一个字符所在下标
# print(test.index("Hello"))
# 字符串的替换（注意：这个功能会返回数据，而且不会更改原字符串，而是生成一个新的字符串）
# 字符串.replace(原字符串, 新字符串)（替换指的是替换所有匹配的字符）
# test = "Hello World!"
# test2 = test.replace("World", "Python")
# print(test)
# print(test2)
# 字符串的分割（按指定的分隔符分割字符串，将字符串分为多个字符串，并存入列表对象中，字符串本身不变，而是得到了一个字符对象）
# 字符串.split(分隔符字符串)（字符串将会以输入的分隔符为界进行分割）
# test = "Hello World!"
# test2 = test.split(" ")
# print(test2)
# 字符串的规整操作（去前后空格）
# 字符串.strip()
# test = "          Hello World!         "
# test2 = test.strip()
# print(test2)
# 字符串的规整操作（去前后指定字符串）
# 字符串.strip(字符串)
# test = "21212112Hello World!21122211111111"
# test2 = test.strip("12")  # 注意，传入的是“12”其实就是：“1”和“2”都会移除，是按照单个字符
# print(test2)

# 数据容器（序列）的切片
# 序列是指：内容连续、有序，可以使用下标索引的索引的一类数据容器
# 如列表、元组、字符串
# 序列[起始下标:结束下标:步长][起始下标:结束下标:步长]...
# 起始和结束下标可以省略，默认从头到尾（不会取到结束下标的位置）
# 步长表示依次取元素的间隔（默认为1，可以省略）
# 步长1表示，一个个取元素
# 步长2表示，每次跳过1个元素取
# 步长N表示，每次跳过N-1个元素取
# 步长为负数表示反向取（注意，起始下标和结束下标也要反向标记）
# 切片操作不会影响原序列，而是重新生成一个序列
# 当全部参数使用默认选项时记得在中括号内加“:”  （序列[:]）同样的，省略起始和结束下标需要在其中加两个“：”  （序列[::步长]）

# 集合的定义与操作（集合中的元素没有顺序，且不可重复）（集合即为数学意义上的集合，列表不是）
# 变量名 = {元素1, 元素2, 元素3, ...}
# 定义空集合
# 变量名 = set()
# 集合添加新元素
# test = {"Hello", "World"}
# test.add("114514")
# print(test)
# 集合删除元素
# test = {"Hello", "World"}
# test.remove("World")
# print(test)
# 从集合中随机取出元素（随机得到一个元素的结果，并将该元素从集合中移除）
# test = {"Hello", "World", "Python"}
# element = test.pop()
# print(element)
# print(test)
# 清空集合
# test = {"Hello", "World"}
# test.clear()
# print(test)
# 取出2个集合的差集
# 集合1.difference(集合2) 功能：取出集合1和集合2的差集（集合1有而集合2没有的）
# test = {1, 2, 3}
# test2 = {3, 4, 5}
# test3 = test.difference(test2)
# print(test3)
# 消除2个集合的交集
# 集合1.difference_update(集合2)
# 功能：对比集合1和集合2，在集合1内删除与集合2相同的元素，结果是集合1被修改，集合2不变
# test = {1, 2, 3}
# test2 = {3, 4, 5}
# test.difference_update(test2)
# print(test)
# print(test2)
# 2个集合合并
# 集合1.union(集合2)
# 功能：得到新集合，原集合不变
# test = {1, 2, 3}
# test2 = {3, 4, 5}
# test3 = test.union(test2)
# print(test3)
# print(test)
# print(test2)
# 集合元素数量的统计使用len()函数
# 集合的遍历
# test = {1, 2, 3, 4, 5}
# for i in test:
#     print(i)

# 字典的定义（key值不可重复，排列在后的重复内容会覆盖前面的内容）
# 变量名 = {key: value, key: value, ..., key: value}
# 定义空字典
# 变量名 = {}
# 变量名 = dict()
# 字典同集合一样，不可以使用下标索引
# 输入字典的key值来取得对应的value值
# test_dict = {114: 514, 1919: 810}
# print(test_dict[114])
# print(test_dict[1919])
# 字典的Key和Value可以是任何数据类型（Key不可为字典）
# 对于字典、列表等这种数据容器而言，是可以在元素定义中换行的
# test_dict = {
#     "键1": {"副键1": "副值1",
#             "副键2": "副值2",
#             "副键3": "副值3", }, "键2": {"副键1": "副值1",
#                                          "副键2": "副值2",
#                                          "副键3": "副值3", }, "键3": {"副键1": "副值1",
#                                                                       "副键2": "副值2",
#                                                                       "副键3": "副值3", }
# }
# print(test_dict["键2"]["副键2"])

# 字典的常用操作
# 新增元素（更新元素）
# 字典[Key] = Value
# 当Key值存在时，Value值会被更新，而Key值不存在时，键值对将会被添加到字典
# test_dict = {"键1": "值1", "键2": "值2", "键3": "值3"}
# test_dict["键4"] = "值4"
# test_dict["键2"] = "值5"
# print(test_dict)
# 删除元素（同时也会取出Key对应的Value）
# 字典.pop(Key)
# test_dict = {"键1": "值1", "键2": "值2", "键3": "值3"}
# a = test_dict.pop("键1")
# print(a)
# print(test_dict)
# 清空字典
# test_dict = {"键1": "值1", "键2": "值2", "键3": "值3"}
# test_dict.clear()
# print(test_dict)
# 获取字典内所有的Key
# 字典.keys()
# test_dict = {"键1": "值1", "键2": "值2", "键3": "值3"}
# keys = test_dict.keys()
# print(keys)
# print(type(keys))
# for key in keys:  # 在此为基础上，可以实现对字典的遍历
#     print(key)
#     print(test_dict[key])
# 同样的，也可以直接使用for循环来对字典进行遍历
# test_dict = {"键1": "值1", "键2": "值2", "键3": "值3"}
# for key in test_dict:
#     print(key)
#     print(test_dict[key])
# 统计字典内元素数量可以使用len()函数

# 数据容器的总结对比
# 是否支持下标索引：
# 支持：列表、元组、字符串 - 序列类型
# 不支持：集合、字典 - 非序列类型
# 是否支持重复元素：
# 支持：列表、元组、字符串 - 序列类型
# 不支持：集合、字典 - 非序列类型
# 是否可以修改：
# 支持：列表、集合、字典
# 不支持：元组、字符串
# 比较元素的大小
# test_str = "abcdefg"
# test_list = [1, 2, 3, 4, 5]
# test_dict = {"key1": 1, "key2": 2, "key3": 3}
# print(max(test_str))
# print(max(test_list))
# print(max(test_dict))  # 涉及字符串的大小比较
# print(min(test_str))
# print(min(test_list))
# print(min(test_dict))
# 类型转化：list()转为列表 str()转为字符串 tuple()转为元组 set()转为集合
# 字符串转列表时会将字符串的每一个字符作为单独的元素加入列表，而字典转列表只会将key值加入列表（元组、集合同理）
# 转化为字符串相当在两端加双引号
# 容器的排序功能
# sorted(容器, [reverse=True]) 通过reverse后的布尔数值来控制数据从小到大还是从大到小（默认为False）

# 扩展 字符串大小比较的方式
# 字符串进行比较就是基于数字的ASCII码的码值大小进行比较的
# 字符串是按位比较，也就是一位一位进行比较，所以只要有一个字符串内的某一个字符大于其他字符串的同位字符，那么前者将大于其他字符串
# 字符串会逐位进行比较，前面的字符一旦比较结果为不等于，那么后面的字符比较结果将作废，最终结果以最先出现不等于的字符为准
