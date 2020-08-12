class Game:
    def __init__(self, my_hp, your_hp):
        # 初始化
        self.my_hp = my_hp
        self.my_power = 20
        self.your_hp = your_hp
        self.your_power = 22

    def fight(self):
        self.my_hp = self.my_hp - self.your_power
        self.your_hp = self.your_hp - self.my_power

    def round(self):
        i = 0
        while True:
            self.fight()
            i += 1
            print(self.my_hp, self.your_hp)
            # 当前回合之后，判断胜负
            if self.my_hp > self.your_hp:
                print(f"第{i}局我赢了")
            elif self.my_hp < self.your_hp:
                print(f"第{i}局你赢了")
            else:
                print(f"第{i}局打平了")
            # 如果我活着敌人某一方血量小于等于0，退出战斗
            if self.my_hp <= 0 or self.your_hp <= 0:
                break


class houyi(Game):
    def __init__(self, my_defense, my_hp, your_hp):
        self.my_defense = my_defense
        # 继承父类的构造函数，若父类构造函数有形参，需要传参
        # 若子类需要使用父类的变量，需要继承这些参数
        super().__init__(my_hp, your_hp)

    # 重新父类的fight()方法
    def fight(self):
        self.my_hp = self.my_hp + self.my_defense - self.your_power
        self.your_hp = self.your_hp - self.my_power
