# 函数的多返回值
# 对于函数有多个返回值
# def test_return():
#     return 1, 2
#
#
# x, y = test_return()
# print(x)
# print(y)

# 函数的多种参数使用形式
# 四种常用的函数参数：位置参数、关键字参数、缺省参数、不定长参数
# 位置参数：调用参数时根据函数定义的参数位置来传递参数
# def user_info(name, age, gander):
#     print(f"您的名字是{name}，年龄是{age}，性别是{gander}")
# user_info('TOM', 20, "男")
# 此时传递的参数和定义的参数顺序及个数必须一致
# 关键字参数：调用时通过“键=值”形式传递参数（使函数更清晰易用，清除了参数的顺序需求）
# def user_info(name, age, gander):
#     print(f"您的名字是{name}，年龄是{age}，性别是{gander}")
#
#
# user_info(name="小明", age=20, gander="男")
# user_info(age=20, gander="男", name="小明")  # 可以不按照固定顺序
# user_info("小明", age=20, gander="男")  # 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
# 缺省函数：即默认参数，用于定义函数，为函数提供默认值，调用时可以不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）
# def user_info(name, age, gander = '男'):
#     print(f"您的名字是{name}，年龄是{age}，性别是{gander}")
#
#
# user_info('TOM', 20)
# user_info('Rose', 18, '女')
# 不定长参数：即可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
# 不定长参数的类型：位置传递、关键字传递
# 位置传递
# def user_info(*args):
#     print(args)
#
#
# user_info('TOM')
# user_info('TOM', 18)
# 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组，args是元组类型
# 关键字传递
# def user_info(**kwargs):
#     print(kwargs)
#
#
# user_info(name="TOM", age=18, id=110)
# 参数是“键=值”的形式的情况下，所有的“键=值”都会被kwargs接受，同时会根据“键=值”组成字典

# 函数作为参数传递
# def test_func(process):
#     result = process(1, 2)
#     print(result)
#
#
# def compute(x, y):
#     return x + y
#
#
# test_func(compute)
# 所以这是一种计算逻辑的传递，而非数据的传递，任何计算逻辑都可以自行定义并作为函数传入（相当于将整个定义函数的代码放进另一个函数的定义函数代码内）
# 函数的嵌套调用
# def compute(x, y):
#     return x + y
#
#
# def test_func():
#     result = compute(1, 2)
#     print(result)
#
#
# test_func()
# 区别：函数的嵌套调用需要让内部的函数写在外部的函数进行定义，而函数作为参数传入则不需要

# lambda匿名函数
# def关键字可以定义带有名称、可重复使用的函数，lambda关键字可以定义只可临时使用一次的匿名函数（无名称）
# lambda 传入参数: 函数定义代码（只能有一行代码）
# def test_func(compute):
#     result = compute(1, 2)
#     print(result)
#
#
# test_func(lambda x, y: x + y)
