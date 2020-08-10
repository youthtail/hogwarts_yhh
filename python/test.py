# 列表的定义 []
# list_hogwarts = [1, 2, 3]
# list_hogwarts.append(4)
# list_hogwarts.insert(1, 33)
# # list_hogwarts.remove(2)
# a = list_hogwarts.pop(0) # 返回被删除的值
# list_hogwarts.sort(reverse=True)
# print(list_hogwarts)
# list_hogwarts.index(33, 0, len(list_hogwarts))

# 列表推导式
# list_squre = []
# for i in range(1,4):
#     list_squre.append(i**2)
# print(list_squre)
# list_squre2 = [i**2 for i in range(1, 4)]
# print(list_squre2)
# list_squre3 = [i**2 for i in range(1, 4) if i != 1]
# print(list_squre3)
# list_squre4 = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         list_squre4.append(i*j)
#
# print(list_squre4)
# list_squre4 = [i*j for i in range(1,4) for j in range(1,4) if j!=2]
# print(list_squre4)

# 元组的定义 ()
# tuple_1 = (1, 2, 3)
# tuple_2 = 1, 2, 3
# print(tuple_1, tuple_2)
# # 元组不可变性, 元组里的元素数据类型不能改变，list作为元组元素例外。因为元组元素对应的指针没变
# list_1 = [1, 2, 3]
# list_1[0] = "a"
# print(list_1)
# output ['a', 2, 3]
# tuple_2[0] = "a"
# 报错TypeError: 'tuple' object does not support item assignment
# tuple_1 = (1, 2, 3, [1, 2, 3])
# tuple_1[3][0] = "a"
# print(tuple_1)
# output :(1, 2, 3, ['a', 2, 3])
# tuple_2 = (1, 2, 2, "a", [1, 2, 3])
# print(tuple_2.count(2))
# print(tuple_2.index("a"))

# 集合的定义




