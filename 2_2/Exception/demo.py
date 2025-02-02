try:
    print(1/0)
except Exception as e:
    print(f"出现异常了{e}")
else :
    print("没有出现异常")
finally:
    print("都会打印")