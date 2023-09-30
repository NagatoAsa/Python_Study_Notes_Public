# 基础地图
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
# map = Map()  # 创建地图对象
# data = [
#     ("北京", 99),
#     ("上海", 199),
#     ("湖南", 299),
#     ("台湾", 399),
#     ("广东", 499)
# ]
# map.add("测试地图", data, "china")  # 向地图输入数据：map.add(地图名称, 传入的数据, 地图类型（默认中国地图）)
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(  # 在全局配置内开启视觉映射器，并允许手动校准
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
#             {"min":10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
#             {"min":100, "max": 499, "label": "100-499人", "color": "#FF9966"},
#             {"min":500, "max": 999, "label": "500-999人", "color": "#FF6666"},
#             {"min":1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
#             {"min":10000, "label": "10000以上", "color": "#990033"}
#         ]
#
#     )
# )
# map.render()  # 绘制地图
