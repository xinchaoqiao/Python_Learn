import json

data = {"age" : 20,"name":"小王"}
print(data)
print(f"data的类型{type(data)}")

data_str = json.dumps(data)
print(data)
print(f"data_str类型{type(data_str)}") # json

# json 转 python类型
lists = [{'age': 20, 'name': '小王'}]
print(lists)
print(type(lists))