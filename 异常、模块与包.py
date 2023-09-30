# 捕获异常
# 当程序遇到异常有两种情况：1、整个程序停止运行；2、对异常进行提醒，程序继续运行
# 而捕获异常作用在于：提前假设某处会出现异常，做好提前准备，当真的出现异常时，可以有后续手段
# try:
#     可能出现异常执行的代码
# except:
#     如果出现一场执行的代码
# try:
#     print(i)
# except:
#     print("出现异常，变量未定义！")
# 捕获指定的异常
# try:
#     print(i)
# except NameError as e:  # as后面可以跟一个新的变量名，来储存错误信息
#     print("变量未定义！")
#     print(e)
#     print(type(e))
# 捕获多个异常
# try:
#     print(1 / 0)
#     print(i)
# except(NameError, ZeroDivisionError):
#     print("出现异常")
# 捕获所有的异常并储存错误信息到变量
# try:
#     print(1 / 0)
#     print(i)
# except Exception as e:
#     print("出现异常")
#     print(e)
# 异常的else和finally语法
# else表示的是如果没有异常要执行的代码
# try:
#     print(1)
# except Exception as e:
#     print(e)
# else:
#     print("没有异常")
# finally表示的是无论是否异常都需要执行的代码，例如关闭文件
# try:
#     f = open('test0.txt', 'r')
# except Exception as e:
#     f = open('test.txt', 'r')
# else:
#     print('没有异常')
# finally:
#     f.close()
# else和finally是可选的，写不写无所谓
# import my_module0
# 模块的概念和导入
# 模块就是一个.py文件，里面有类、函数、变量等，我们可以导入进行使用
# 模块的导入方式
# [from 模块名] import [模块|类|变量|函数|*] [as 别名]
# import 模块名
# import 模块名1, 模块名2
# 模块名.功能名()
# import 模块名
# import time
# print("开始")
# time.sleep(5)
# print("结束")
# from 模块名 import 功能名（只导入某个模块的某个功能）
# from time import sleep
# print("开始")
# sleep(5)
# print("结束")
# from 模块名 import *（导入模块的所有功能，此种导入方式使用功能时无需加模块名）
# from time import *
# print("开始")
# sleep(5)
# print("结束")
# 使用as给特定功能加上别名
# import time as tt
# print("开始")
# tt.sleep(5)
# print("结束")
# from time import sleep as sl
# print("开始")
# sl(5)
# print("结束")
# import my_module0
# 自定义模块并导入
# import my_module
# my_module.test(5, 5)
# 注意当导入的两个模块存在相同的函数、变量名等，生效的是最后导入的模块
# from my_module import test
# from my_module0 import test
# test(1, 1)
# 测试模块
# 有时为了为了测试代码而会添加一些测试信息，但是无论是当前文件还是其它已经导入了该模块的文件，在运行时都会自动执行‘test函数的调用
# 为了应对这种情况，我们可以使用__main__变量
# from my_module import test
# 当程序作为主程序被运行时__name__变量会自动被命名为"__main__"，当程序作为模块被导入时，__name__变量则不会被命名为"__main__"
# 如果一个模块文件中有”__all__“变量，当使用”from xxx import *“导入时，只能导入这个列表中的元素
# from my_module import *
# test(1, 2)
# test_A()
# test_B()  #程序将在此报错
# import my_module0
# 自定义Python包
# 从物理上看，包就是一个文件夹，在该文件夹下包含了一个__init__.py文件，该文件夹可用于包含多个模块文件 ，但包的本质依然是模块
# 导入包
# import 包名称.模块名.目标名
# import my_package.my_module  #方法一
# my_package.my_module.test(1, 2)
# 使用from进行导入
# from my_package import my_module  # 方法二
# my_module.test(1, 2)
# from my_package.my_module import test
# test(1, 2)
# from 包名 import *
# 必须再”__init__.py“文件中添加”all = []“控制允许导入的模块列表
# from my_package import *
# my_module.test(1, 2)
# my_module0.test(1, 2)  # 程序将在此报错

# 安装第三方包
# 在终端输入pip install 包名称即可在线安装第三方包
