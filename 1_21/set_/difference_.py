set1 = {1,2,3,5}
set2 = {1,2,4}
set3 = set1.difference(set2) # 输出差集
print(set3)

# 消除差集 集合1发生变化， 集合2不发生变化
set1.difference_update(set2)
print(set1)

# 并集
set3 = set1.union(set2)
print(set3)

# 遍历
for element in set3:
    print(element)

str1 = ("111")
str1[1] = "0"