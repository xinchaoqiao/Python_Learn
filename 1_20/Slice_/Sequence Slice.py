# 序列切片
#语法: 序列[起始下标:结束下标:步长] 元素不包括结束下标元素
# 1.对list切片
my_list = [0,1,2,3,4,5,6]
rel = my_list[1:4]
print(rel)
# 2.对tuple切片
my_tuple = (1,2,3,4,5,6,7)
rel = my_tuple[:] #起始和结束都留空 代表 从头到尾 步长留空 默认1
print(rel)
# 3.对str切片
my_str = "01234567"
rel = my_str[::2] # 隔步长减一 获取元素
