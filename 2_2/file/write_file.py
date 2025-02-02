from idlelib.iomenu import encoding

with open('测试.txt','w',encoding = "UTF-8") as f:
    f.write("hello world")
    f.write("你好")
    f.flush()

with open('测试.txt','a',encoding = "UTF-8") as f:
    f.writelines("\n111")
    f.write("111")


f = open('测试.txt','r',encoding="UTF-8")


for line in f:
    print(line)

f.close()
