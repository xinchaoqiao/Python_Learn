
my_list = [1,"it",True]
print(my_list)

print()
my_list2 = [[1,1],[2]]
print(my_list2)

my_list3 = ["Tom","Rose","Tim"]
# 倒序输出 最后一个-1 递减
print(my_list3[-1])
print(my_list3[-2])
print(my_list3[-3])

# 列表常用方法
# 1.append(元素) 末尾追加一个元素
list1  = [1, 2, 3, 4, 5, 6]
list1.append(7)
print(list1)
# 2.extend(容器) 末尾追加一批元素
list2 = ["Tom","Tim"]
list1.extend(list1)
print("extend",list2)
# 3.insert(下标,元素)
list1.insert(2,"TT")
print("insert",list1)
# 4.del 列表[下标]删除元素
#   pop(下标) ->element
del list1[1]
element = list1.pop(1)
print(element)
# 5.remove(元素) 删除指定元素
list1.remove(4)
print("remove :",list1)
# 6.count(元素)列表元素个数
count1 = list1.count("3")
print("count",count1)
# 7.index(元素) 元素下标
index = list1.index(2)
print("index",index)
# 8.列表长度
len1 = len(list1)
print("len",len1)
# 9.clear()清空列表
list1.clear()
print(list1)
