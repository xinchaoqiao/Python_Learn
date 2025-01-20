# 字符串不允许修改

# 1.分割字符串
str1 = "itcast itheima python"
new_str1 = str1.split()
print(new_str1)
# 2.去除前后空格
str2 = "      itcast itheima python   "
print(str2.strip())
# 去除 12
str3 = "12itcast itheima python21"

print(str3.strip("12"))

# 字符出现次数
str4 = "itcast itheima python"
print("it出现次数为:",str4.count("it"),"字符串总长度为:",len(str4))
# replace
str5 = "itcast itheima python"
print(str5.replace("it","It"))

