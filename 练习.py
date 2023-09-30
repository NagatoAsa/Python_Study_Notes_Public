# 字符串
# 定义变量
# name = "传智播客"
# stock_price = 19.99
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# 计算并输出结果
# print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
# print("每日增长系数为：%.1f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor ** growth_days))
# 判断语句
# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("您已成年，游玩需要补票10元。")
# print("祝您游玩愉快。")

# print("欢迎来到黑马动物园")
# height = int(input("请输入你的身高（cm）："))
# if height > 120:
#     print("您的身高超出120cm，游玩需要购票10元。")
# else:
#     print("您的身高未超出120cm，可以免费游玩。")
# print("祝您游玩愉快。")
# import random
# num = random.randint(1, 10)
# if判断条件可以直接插入input语句
# if int(input("请输入第一次猜想的数字：")) == num:
#     print("恭喜你猜对了！")
# elif int(input("不对，再猜一次：")) == num:
#     print("恭喜你猜对了！")
# elif int(input("不对，再猜最后一次：")) == num:
#     print("恭喜你猜对了！")
# else:
#     print(f"Sorry，全部猜错啦，我想的是{num}")

# count = 0
# nm = "itheima is a brand of itcast"
# for i in nm:
#     if i == "a":
#         count += 1
# print("itheima is brand of itcast中含有：%d个字母a" % count)

# import random
# salary = 10000
# for i in range(1, 21):
#     score = random.randint(1, 10)
#     if salary > 0:
#         if score >= 5:
#             salary -= 1000
#             print(f"向员工{i}发放工资1000元，账户还剩余{salary}。")
#         else:
#             print(f"员工{i}，绩效分{score}，低于5，不发工资，换下一位。")
#             continue
#     else:
#         print("工资发完了，下个月领取吧。")
#         break

# 函数的综合应用
# 模拟ATM
# money = 5000000
# name = input("请输入你的姓名：")
#
#
# def main():
#     print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     i = int(input("请输入你的选择："))
#     return i
#
#
# def save(num):
#     global money
#     money += num
#     print("----------------存款----------------")
#     print(f"{name}，您好，您存款{num}元成功")
#     print(f"{name}，您好，您的余额剩余：{money}元")
#
#
# def withdraw(num):
#     global money
#     money -= num
#     print("----------------取款----------------")
#     print(f"{name}，您好，您取款{num}元成功")
#     print(f"{name}，您好，您的余额剩余：{money}元")
#
#
# def check():
#     print("----------------查询余额----------------")
#     print(f"{name}，您好，您的余额剩余：{money}元")
#
#
# while True:
#     choice = main()
#     if choice == 1 or choice == 2 or choice == 3:
#         pwd = int(input("请输入你的密码："))
#         if pwd == 114514:
#             if choice == 1:
#                 check()
#             elif choice == 2:
#                 s_money = int(input("请输入要存钱的数目："))
#                 save(s_money)
#             elif choice == 3:
#                 w_money = int(input("请输入要取钱的数目："))
#                 withdraw(w_money)
#             else:
#                 print()
#         else:
#             print("密码错误！")
#             break
#     elif choice == 4:
#         print()
#         break
#     else:
#         print("无对应操作，请重新输入！")

# 数据容器
# 列表的常用功能
# age = [21, 25, 21, 23, 22, 20]
# age.append(31)
# age.extend([29, 33, 30])
# a = age.pop(0)
# b = age.pop(8)
# print(a)
# print(b)
# print(age.index(31))

# 列表的循环遍历
# index = 0  # while方法
# test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# test2 = list()
# while index <= len(test) - 1:
#     element = test[index]
#     index += 1
#     if element % 2 == 0:
#         test2.append(element)
# print(test2)
# test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# test2 = list()
# for i in test:
#     if i % 2 == 0:
#         test2.append(i)
# print(test2)

# 字符串的定义和操作
# test = "itheima itcast boxuegu"
# print(test.count("it"))
# test2 = test.replace(" ", "|")
# print(test2)
# print(test2.split("|"))

# 数据容器（序列）的切片
# test = "万过薪月，员序程马黑来，nohtyP学"  #方法一
# test2 = test[::-1]
# print(test2)
# test3 = test2[9:14]
# print(test3)
# test = "万过薪月，员序程马黑来，nohtyP学"  # 方法二
# test2 = test[::-1]
# test3 = test2.split("，")
# test4 = test3[1]
# test5 = test4.replace("来", "")
# print(test5)
# 简化
# test = "万过薪月，员序程马黑来，nohtyP学"
# test2 = test[::-1][9:14]
# print(test2)
# test2 = test[5:10][::-1]
# print(test2)
# test2 = test.split("，")[1].replace("来", "")[::-1]
# print(test2)

# 集合的定义与操作
# my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast']
# test = set()
# for i in my_list:
#     test.add(i)
# print(test)

# 字典的常用操作
# test = {"王力鸿": {"部门": "科技部",
#                    "工资": 3000,
#                    "级别": 1
#                    },
#         "周杰轮": {"部门": "市场部",
#                    "工资": 5000,
#                    "级别": 2
#                    },
#         "林俊节": {"部门": "市场部",
#                    "工资": 7000,
#                    "级别": 3
#                    },
#         "张学油": {"部门": "科技部",
#                    "工资": 4000,
#                    "级别": 1
#                    },
#         "刘德滑": {"部门": "市场部",
#                    "工资": 6000,
#                    "级别": 2
#                    }
# }
# print(test)
# for i in test:
#     if test[i]["级别"] == 1:
#         test[i]["级别"] += 1
#         test[i]["工资"] += 1000
# print(test)

# 文件的读取操作
# my_list = []  # 方法一
# count = 0
# for line in open("word.txt", "r", encoding="UTF-8"):
#     my_list.append(line.split(" "))
# for i in my_list:
#     temp_count = i.count("itheima")
#     count += temp_count
#     temp_count = i.count("itheima\n")
#     count += temp_count
# print(count)
# f.close()
# f = open('word.txt', 'r', encoding='UTF-8')  # 方法二
# r = f.read()
# print(r)
# print(r.count("itheima"))
# f.close()
# my_list = []  # 方法一改进
# count = 0
# for line in open("word.txt", "r", encoding="UTF-8"):
#     line = line.strip()  # 字符串的规整去除开头和结尾的空格和换行符
#     my_list.append(line.split(" "))
# for i in my_list:
#     temp_count = i.count("itheima")
#     count += temp_count
# print(count)
# f.close()

# 异常、模块与包综合案例
# from my_utils import *
# print(str_util.str_reverse("Hello World!"))
# print(str_util.substr("Hello World!", 0, 6))
# file_util.print_file_info("test.txt")
# file_util.append_to_file("test.txt", "Hello World!\n1145141919810\n")

# 构造方法
# class Student:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# for i in range(1, 11):
#     print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
#     name = input("请输入学生姓名：")
#     age = input("请输入学生年龄：")
#     address = input("请输入学生地址：")
#     stu = Student(name, age, address)
#     print(f"学生{i}信息录入完成，信息为【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}】")

# 封装
class Phone:
    __is_5g_enable = False
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")


    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
