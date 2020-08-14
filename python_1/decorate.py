
# # 闭包函数就是一个装饰器
# # 函数调用装饰器，需要形参
# def func3(trier, cc):
#     def func1(func):
#         def func2(bb):
#             if trier:
#                 print("I am doing some boring work before executing a_func()")
#                 func(bb)
#                 print("I am doing some boring work after executing a_func()")
#             else:
#                 print(f"开关关了{cc}")
#
#         return func2
#
#     return func1
#
#
# #
#
# @func3(False, 2)
# def be_decorate(aa):
#     print(f"我就是需要装饰的函数{aa}")
#
#
# be_decorate("lily")
def func0(trigger):
    def func1(func):
        def func2(a):
            print("aaa")
            func(a)
            print(f'trigger{trigger}')
        return func2
    return func1


@func0('kaiguan')
def target(a):
    print(f"我需要装饰{a}")


target("被装饰函数的参数")
# # 装饰器的实际运行过程
# # 装饰器需要传值fun0，被装饰函数需要传值fun1
# f0=func0("开关")
# # 把函数对象传给func1,返回func2的函数对象
# f1=f0(target)
# # 运行func2的函数对象
# f1("lily")
