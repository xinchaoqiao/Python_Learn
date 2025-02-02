def func01():
    print(1/0)
def func02():
    func01()

def main():# 最高层 异常具有传递性  会从最底层穿到最高层 可以在最高层捕获异常
    try:
        func02()
    except Exception as e:
        print(f"出现异常了,{e}")


main()