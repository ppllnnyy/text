# 所谓函数嵌套调用指的是一个函数里面又调用了另一个函数
def func_b():
    print("---2---")

def func_a():
    print("---1---")

    func_b()

    print("---3---")

func_a()