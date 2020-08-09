def func1():
    print("This is first func")

    def func2():
        print("This is second func")

    return func2

# func1执行本函数里的语句，并返回func2的函数对象，赋值给a
a = func1()
print("=======")
# a就是一个函数对象，加上圆括号，就是调用函数
a()
# output:
# This is first func
# =======
# This is second func

