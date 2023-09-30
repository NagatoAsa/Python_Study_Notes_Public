# i = 1
# p = 0
# while i <= 100:
#     p += i
#     i += 1
# print(p)
# import random
# num = random.randint(1, 100)
# count = 1
# guess_num = int(input("请输入你猜的数字："))
# while guess_num != num:
#     if guess_num > num:
#         print("猜的数字大了")
#     else:
#         print("猜的数字小了")
#     guess_num = int(input("再猜一次："))
#     count += 1
# print(f"恭喜猜对了！你猜了{count}次。")

# 多个print语句不换行，在print中加入end=''
# print("Hello", end='')
# print("World", end='')

# \t制表符，与tab键相同，可以对多行字符串进行对齐 \n为换行符
# print("Hello\tWorld")
# print("Mother\tFucker")

# while循环打印九九乘法表
i = 1
while i <= 9:
    t = 1  # 注意把变量t放在第一个循环内，使其能够在第一个循环的每个循环内被重置为1
    while t <= i:
        print(f"{t} * {i} = {t * i}\t", end='')  # 利用\t制表符对齐，end=''来取消换行
        t += 1
    i += 1
    print()  # print空字符即为换行

# for循环
# 遍历字符串
# name = "1145141919810"
# for i in name:
#     print(i)

# range语句
"""
    1.range(num) 从零开始遍历数字（除了num本身）
    2.range(num1, num2)遍历num1到num2的数字（除了num2本身）
    3.range(num1, num2, step)遍历num1到num2的数字,步长由step决定（除了num2本身）
"""

# for循环打印九九乘法表
# for i in range(1, 10):
#     for t in range(1, i + 1):
#         print(f"{t} * {i}={i * t}\t", end='')
#     print()

# continue 中断本次循环，进行下一次循环 break 中断循环，且不再继续

