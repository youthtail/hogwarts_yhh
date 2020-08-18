def div(a, b):
    return a / b


a = 1
b = 0
""" 
try:{}
except Exception as e:{}
except 
"""
class zero(Exception):
    print("我定义的类")


try:
    c = div(1, 0)
except Exception as e:
    print(e.__class__.__name__)
    print(b)
try:
    if b == 0:
        raise zero
except Exception as e:
    pass

