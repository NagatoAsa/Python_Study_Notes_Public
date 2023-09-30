# 文件的读取操作
# open()打开函数
# cpen(name, mode, encoding)
# 由于encoding变量并不在定义函数的第三位，所以必须使用关键字传参
# name：是要打开的文件名的字符串（可以包含文件所在的具体路径,路径级别的分隔可以用正斜杠“/”）
# mode:：设置打开文件的模式（访问模式）：只读、写入、追加等
# encoding：编码格式（一般、默认选择UTF-8）
# f = open('test.txt', 'r', encoding='UTF-8')
# 此时的“f”是open()函数的文件对象，对象是Python中一种特殊的数据类型，拥有属性和方法可以使用“对象.属性”或“对象.方法”对其进行访问
# mode常用的三种访问模式
# r只读，文件的指针将会放在文件的开头，默认模式
# w写入，如果文件存在则打开文件，从头开始编辑，原有内容会被删除。如果文件不存在，创建新文件
# a追加，如果文件存在则打开文件，新的内容会被写到已有内容以后。如果文件不存在，创建新文件
# read()方法
# 文件对象.read(num)
# num表示要从文件中读取的数据的长度（单位是字节，如果没有传入num，那么就表示读取文件中所有的数据）
# f = open('test.txt', 'r', encoding='UTF-8')
# r = f.read(12)
# print(r)
# readlines方法，readline可以按照行的方式把整个文件中的内容进行一次性读取，并返回一个列表，每一行的数据为一个元素
# f = open('test.txt', 'r', encoding='UTF-8')
# r = f.readlines()
# print(r)
# print(type(r))
# 注意：文件读取是存在文件指针的，后续运行读取会在原有读取的进度上继续读取
# readline()方法，一次读取一行内容，调用一次读取一行
# f = open('test.txt', 'r', encoding='UTF-8')
# r1 = f.readline()
# r2 = f.readline()
# print(r1)
# print(r2)
# for循环读取文件行
# for line in open("test.txt", "r", encoding="UTF-8"):
#     print(line)
# 关闭文件
# f = open('test.txt', 'r', encoding='UTF-8')
# f.close()
# 关闭对文件的占用，若程序未停止运行，且不调用close，文件将会被一直占用
# 拓展：time.sleep(秒数)可以使程序暂停运行一定时间
# with open语法
# with open('test.txt', 'r', encoding='UTF-8')as f:
#     r = f.readlines()
#     print(r)
# 通过再with open的语句块中对文件进行操作
# 可以在操作完成后自动关闭文件，避免遗忘

# 文件的写出操作
# f = open("test.txt", "w", encoding="UTF-8")  # 打开文件
# f.write("Hello World!\n1145141919810")  # 写入文件
# f.flush()  # 刷新文件
# f.close()  # 关闭文件
# 直接调用write，内容不会真正写入文件，而会储存于缓冲区中
# 当调用flush或者close关闭文件的时候，内容才会真正地被写入，从而避免频繁的磁盘操作导致效率下降

# 文件的追加写入操作
# f = open("test.txt", "a", encoding="UTF-8")  # 打开文件
# f.write("Hello World!\n1145141919810\n")  # 文件写入
# f.flush()  # 内容刷新
# f.close()  # 关闭文件

# 文件操作的综合案例
# f = open("bill.txt", "r", encoding="UTF-8")
# w = open("bill.txt.bak", "a", encoding="UTF-8")
# count = 1
# for i in f:
#     i = i.strip()
#     if count == 1:
#         count += 1
#         continue
#     else:
#         count += 1
#         j = i.split("，")
#         if j[4] == "正式":
#             w.write(f"{i}\n")
#         else:
#             continue
# w.flush()
# w.close()
