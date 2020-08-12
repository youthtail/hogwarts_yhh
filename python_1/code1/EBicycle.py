from code1.Bicycle import Bicycle


class EBicycle(Bicycle):
    # def __init__(self, volume):
    #     self.volume = volume
    # 初始化的数据放在构造函数
    def __init__(self, volume, km):
        self.volume = volume
        self.km = km

    def charge(self, vol):
        self.volume = self.volume + vol
        print(f"冲了{vol}度电，我的电瓶有{self.volume}度电了")

    def run(self):
        e_miles = self.volume * 10
        if e_miles >= self.km:
            print(f'我骑电瓶车走完全程，骑了{self.km}km')
        else:
            m_miles = self.km - e_miles
            print(f'我骑电瓶车骑了{e_miles}km')
            # 继承父类的方法 super().方法名
            super().run(m_miles)
