# 闭包函数
# 变量的作用域
name = "鲸鱼"
# 定义是的参数叫做形参，传递是的参数叫做实参
# 闭包函数被调用，需要j

def func1(func):
    print(name)

    def func2():
        name = "虾米"
        print(name)
        print("闭包函数")

    return func2


# 调用func1函数实际上调用func2的函数对象，因为返回的就是func2
# func1()
# print(func1())
# func22 = func1()
# func22()

@func1
def be_decorate():
    print("被装饰器装饰的函数")


be_decorate()
