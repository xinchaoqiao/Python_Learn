
def test_main(com):
    rel = com(1,2)
    print(rel)
def com(x,y):
    return x + y

test_main(com)