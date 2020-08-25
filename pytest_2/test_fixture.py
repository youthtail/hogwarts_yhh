
class TestFixture:
    def test_fun1(self,login):
        print(f"测试方法1--需要登陆,用户名：{login[0]}，密码：{login[1]}")

    def test_fun2(self):
        print(f"测试方法2--")

    def test_fun3(self):
        print("测试方法3--需要登陆")
