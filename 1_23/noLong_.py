# 位置不定长 以元组形式接收参数
def user_info(*args):
    print(f"类型是:{type(args)},内容是:{args}")

# 关键字不定长,以字典形式dict 接收参数
def user__info(**kwargs):
    print(f"类型是{type(kwargs)},内容是: {kwargs}")

user_info(1,2,3,4,5,"小明")
user__info(name="小明",gender = "男",age = 12)

