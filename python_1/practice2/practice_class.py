class Dog:
    category = '狗狗'

    def __init__(self, name, bone):
        self.bone = bone
        self.name = name

    @staticmethod
    def eat(bone):
        print(f"我爱吃{bone}")

    def get_name(self):
        print(f"我的名字叫{self.name}")


class Car:
    category = '汽车'
    max_vol = 100

    def __init__(self, color, vol):
        self.color = color
        self.vol = vol

    def get_color(self):
        print(f"我的名字叫{self.color}")

    def charge(self, hour):
        self.vol = self.vol + hour * 5
        if self.vol >= self.max_vol:
            print(f"我的电量是{self.max_vol},我充满电了")
        else:
            print(f"我的电量是{self.vol},还没充满电")
