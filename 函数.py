# def hello():
#     print("欢迎来到黑马程序员！")
#     print("请出示您的健康码以及72小时核酸证明！")
# hello()

# def check(t):
#     print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温")
#     if t <=37.5:
#         print(f"体温测量中，您的体温是：{t}度，体温正常请进！")
#     else:
#         print(f"体温测量中，您的体温是：{t}度，需要隔离！")
# check(37.3)
# check(39.3)

# 注：def 内定义的临时变量不能用于定义该函数外
# 错误示范
# def test():
#     num = 200
#     print(num)
# test()
# print(num)

# 正确示范1
# num = 100
#
#
# def test1():
#     print(num)
#
#
# def test2():
#     num = 200
#     print(num)
#
#
# test1()
# test2()
# print(num)

# 此时定义函数内对变量的修改不会对全局产生影响

# 正确示范2
# num = 100
#
#
# def test1():
#     print(num)
#
#
# def test2():
#     global num
#     num = 200
#     print(num)
#
#
# test1()
# test2()
# print(num)

# 利用global关键字来声明该变量为全局变量（加在使用变量之前）
def test(num1,num2):
    i = num1 + num2
    return i


a = test(1, 1)
print(a)
