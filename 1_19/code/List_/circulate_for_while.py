my_list = [1,2,3,4,5]
# for 循环
def c_for():
    print("for circulate:")
    for element in my_list:
        print(element)

def c_while():
    print("while circulate")
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index+=1

c_for()
c_while()

# exercise
list2 = [1,2,3,4,5,6,7,8,9,10]
list3 = []
index = 0
for ele in list2:
    if ele % 2 == 0 :
        list3.append(ele)
        index+=1

print(list3)