def div(a, b):
    return a / b

""" 
try:{}
except Exception as e:{}
except 
"""
class ZeroDiv(Exception): # 继承Exception类
    print("我定义的类")

class Test1:

    def test_method1(self,a,b):
        self.b=b
        try:
            div(a, b)
        except Exception as e:
            print(e.__class__.__name__)

    def test_method2(self,b):
        try:
            if b == 0:
                raise ZeroDiv
        except Exception as e:
            print(e.__class__.__name__)

if __name__=="__main__":
    test1=Test1()
    test1.test_method1(1,0)
    a=test1.b
    test1.test_method2(a)