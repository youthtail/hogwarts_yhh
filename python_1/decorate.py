# 闭包函数就是一个装饰器
# 函数调用装饰器，需要形参
# 装饰器
def func1(func):
    def func2():
        print("I am doing some boring work before executing a_func()")
        func()
        print("I am doing some boring work after executing a_func()")

    return func2


@func1
def be_decorate():
    print("我就是需要装饰的函数")


be_decorate()
# output：
# I am doing some boring work before executing a_func()
# 我就是需要装饰的函数
# I am doing some boring work after executing a_func()
