# # 第一种import模块的方法
# # import python_1.baidu
# # python_1.baidu.search()
#
# # 第2种import模块的方法
# # from sys import path
# # from python_1.baidu import search
# # search()
# # 当前目录下的所有能够使用的变量和函数
# # print(dir())
# # print(path)
#
# # 定义列表list、元组tuple、集合set、字典dict.
# # 其中字典、集合是同一种数据类型，都是无需的，不支持下表索引。区别是集合是唯一的，用于列表、元组的去重。有并集、交集等函数。集合不可重复
list1 = ["lily",1]
tuple1 = ("lily",1)
# set0 = set() # 定义一个集合
# set00 = {} # 定义一个字典，无序的，
dict1 = {"name":"lily", "gender":1}
print(dict1['name'])
# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))
# print(dict1)
#
# # 字面量 format() 方法 ： str.format(*listdata,**dictdata,data)
# print("data:my name is {},my phone is {}".format("lily",1))
#
# # 解包 *listdata
# print("list:my name is {},my phone is {}".format(*list1))
# print("tuple:my name is {},my phone is {}".format(*tuple1))
# # 解包，**dict，str{}一定要写字典的key.因为字典是无需的集合，是通过key来查找value
# print("dict:my name is {name},my phone is {gender}".format(**dict1))
#
# # list_A = [1,2,2,3,4,3] # 列表
# # a = set(list_A)  # set()去重变成集合
# # print(type(list(a))) # list（）把集合变成列表
#
#
# # f-格式化字符串
name = "lily"
gender = 1
# dict的key必须使用单引号
# {}里面的值可以是常量、变量、函数，但是不能有转义\
print(f"my tuple is {tuple1[0]}, my list is {list1[0]}, my dict is {dict1['gender']}")
print(f"my tuple is {name}, my list is {list1[0]}, my dict is {dict1['gender'].__float__()}")
# 当有:,可以使用（）括起来
print(f"我的字面量插值 \n {(lambda x:x+1)(2)}")
# {}里面也可以是单引号
print(f'我的字面量插值 \n {2}')

