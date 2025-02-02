from idlelib.iomenu import encoding

f = open("测试.txt","r",encoding="UTF-8")

lists = f.readlines()
for line in lists:
    print(line)
#
# for line in f:
#     print(line)
f.close()

# 自动关闭文件流
# with open("测试.txt","r",encoding = "UTf-8") as f:
#     for line in f:
#         print(line)


