# JSON数据格式
# JSON是一种轻量级的数据交互格式，可以按照JSON指定的格式去组织和封装数据
# JSON本质上是一个带有特定格式的字符串
# JSON是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递与交互
# 各种编程语言储存数据的容器不尽相同，在Python中有字典这样的数据类型，而其他语言可能没有对应类型
# 而JSON就是一种很好的中转数据格式
# JSON格式数据转化
# JSON数据的格式可以是：
# {"name":"admin", "age":18}
# 或者：
# [{"name":"admin", "age":18}, {"name":"root", "age":16],{"name":"张三", "age":20}]
# JSON格式的数据要么是列表要么是字典
# JSON格式要求列表内的数据必须是字典，而字典的规定和Python语法一致
# import json  # 导入JSON模块
# data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]  # 准备符合JSON格式要求的Python数据
# data = json.dumps(data)  # 把Python数据转化为JSON数据
# print(data)
# print(type(data))
# data = json.loads(data)  # 把JSON数据转化为Python
# print(data)
# print(type(data))
# data = json.dumps(data, ensure_ascii=False)  # 在将Python数据转化为JSON数据的基础上对中文编码进行修正
# print(data)
# print(type(data))

# pyecharts模块简介
# 官网：pyecharts.org
# 画廊地址：gallery.pyecharts.org/#/README

# pyecharts的入门使用
# 基础折线图
# from pyecharts.charts import Line  # 导包，导入Line功能构建折线图对象
# from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# line = Line()  # 得到折线图对象
# line.add_xaxis(["中国", "美国", "英国"])  # 添加x轴数据
# line.add_yaxis("GDP", [30, 20, 10])  # 添加y轴数据
# # 全局配置
# # 可以通过set_global_opts方法来对全局配置选项进行配置，例如标题、图例、鼠标移动效果、工具栏等整体配置项
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),  # 设置标题
#     # 修改标题与左侧边界的距离，center即为居中
#     # 修改标题距离底部边界的距离，1%表示只有1%纵向长度的距离
#     legend_opts=LegendOpts(is_show=True),   # 设置图例
#     toolbox_opts=ToolboxOpts(is_show=True),   # 设置工具箱
#     visualmap_opts=VisualMapOpts(is_show=True)  # 设置视觉映射
# )
# line.render()  # 生成图表
# 此时目录下会生成一个html文件，其中内容即为生成的图表

# 通过JSON模块对数据的准备与处理;生成折线图
# JSON数据格式化网站：json.cn
# 处理数据
# import json
# f_us = open("./data/美国.txt", "r", encoding="UTF-8")  # 打开并读取文件
# f_in = open("./data/印度.txt", "r", encoding="UTF-8")
# f_jp = open("./data/日本.txt", "r", encoding="UTF-8")
# us_data = f_us.read()
# in_data = f_in.read()
# jp_data = f_jp.read()
# us_data = us_data.replace("jsonp_1629344292311_69436(", "")  # 去除不符合JSON规范的开头
# in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
# us_data = us_data[:-2]  # 去除不合JSON规范的结尾（为防止去除掉规范内容，可以使用字符串的切片）
# in_data = in_data[:-2]
# jp_data = jp_data[:-2]
# us_data = json.loads(us_data)  # 将JSON数据转化为Python字典
# in_data = json.loads(in_data)
# jp_data = json.loads(jp_data)
# us_trend_data = us_data["data"][0]["trend"]  # 在字典内找到trend数据
# in_trend_data = in_data["data"][0]["trend"]
# jp_trend_data = jp_data["data"][0]["trend"]
# us_x_data = us_trend_data["updateDate"][:314]  # X轴数据：在trend中取得updateDate数据并进行切片（只取到2020年12月31日）
# in_x_data = in_trend_data["updateDate"][:314]
# jp_x_data = jp_trend_data["updateDate"][:314]
# us_y_data = us_trend_data["list"][0]["data"][:314]  # Y轴数据：在trend中取得确诊人数数据并切片
# in_y_data = in_trend_data["list"][0]["data"][:314]
# jp_y_data = jp_trend_data["list"][0]["data"][:314]
# 开始生成图表
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LabelOpts
# line = Line()  # 构建折线图对象
# line.add_xaxis(us_x_data)  # 添加x轴数据，x轴是共用的，所以只需要取一个国家的
# line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))  # 添加y轴数据，并使用系列配置调整图表
# line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))
# line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
# line.set_global_opts(
#     title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
# )
# line.render()  # 生成图表
# f_us.close()  # 关闭文件
# f_in.close()
# f_jp.close()
