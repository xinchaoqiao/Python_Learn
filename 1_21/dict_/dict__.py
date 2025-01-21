# 字典
"""
空字典
mydict = {}
or
mydict = dict()

"""
# 成绩单
my_dict = {
    "王力宏" : {
        "语文":99,
        "数学":98,
        "英语":77
    },"周杰伦":{
        "语文":100,
        "数学":88,
        "英语":77
    }
}
print(f"王力宏：{my_dict['王力宏']['语文']}")

keys = my_dict.keys()
print(f"all keys : {keys}")
# 遍历
for key in keys:
    print(my_dict[key])


# 移除元素
content = my_dict.pop("周杰伦")
print(f"移除的元素内容是：{content}")
keys = my_dict.keys()
print(keys)
# 清空元素
my_dict.clear()
print(len(my_dict))