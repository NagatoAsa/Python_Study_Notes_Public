# 查询数据类别
# name = "张三"
# print(type(name))
# num = 114514
# print(type(num))
# flt = 14.51
# print(type(flt))

# 字符串的定义
# name1 = "'张‘三"
# name2 = '"张“三'
# name3 = "\"张三"
# print(name1, name2, name3)

# 字符串格式化
# %s将内容转化为字符串插入 %d将内容转化为整数插入 %f将内容转化为浮点数插入
# phone = 1145141919810
# num = 114514
# massage = "Phone:%s Number:%s" % (phone, num)
# print(massage)
# phone = 1145141919810
# num = 114514
# massage = "Phone:%d Number:%d" % (phone, num)
# print(massage)
# phone = 1145141919810
# num = 114514
# massage = "Phone:%f Number:%f" % (phone, num)
# print(massage)

# 字符串格式化的精度控制
# “m.n”可以控制数字的精度，m控制的是数字的宽度（几位数，包括小数点、小数），n可以控制保留小数点后几位(四舍五入)
# 当m设置的宽度小于数字自身，不生效
# phone = 1145141919810
# num = 114514
# massage = "Phone:%.2f Number:%.2f" % (phone, num)
# print(massage)
# phone = 1145141919810
# num = 114514
# massage = "Phone:%14d Number:%14d" % (phone, num)
# print(massage)
# phone = 1145141919810
# num = 114514
# massage = "Phone:%5d Number:%5d" % (phone, num)
# print(massage)
# num2 = 14.13
# massage2 = "Number2:%6.2f" % num2
# print(massage2)

# 快速字符串格式化 f"内容{变量}" （不做精度控制）
# name = "张三"
# phone = 1145141919810
# num = 114514
# num2 = 14.13
# print(f"Name:{name} Phone:{phone} Number:{num} Number2:{num2}")

# 表达式格式化
print("1 * 1的结果为：%d" % (1 * 1))
print(f"1 * 1的结果为：{1 * 1}")
print("字符串在Python中的数据类型为：%s" % type("字符串"))

