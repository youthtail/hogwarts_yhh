class Person:
    name = "default"
    age = 0

    def __init__(self, name, age):
        print("我是构造函数")
        self.name = name
        self.age = age

    @classmethod
    def get_name(cls):
        cls.name = "改名字"
        print(f"我的名字是：{cls.name}")

    def get_age(self):
        print(f"我的年龄是：{self.age}")


a = Person('lily', 10)
# 类变量可以直接被类引用
Person.get_name()
print(Person.name, Person.age)

print(a.name, a.age)
a.get_name()
a.get_age()
