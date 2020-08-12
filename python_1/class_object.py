class House:
    door = 'red'
    floor = 'white'

    # 构造函数在实例化对象的时候直接调用
    def __init__(self):
        # 实例变量，作用于整个类，但是必须以self.的方式引。而且必须先声明
        self.pillow = '枕头'


    def sleep(self):
        desk = '桌子'
        self.bed = '舒服的床'
        # 类变量在方法里通过self.的方式调用
        print(f'睡觉{self.door}')

    def cook(self):
        print('做饭')
        print(self.pillow)


north_house = House()
china_house = House()
north_house.sleep()
# 实例变量可以被对象使用
north_house.pillow

# # 类的属性修改，所有类的实例化对象都生效，实力化对象的属性修改，只是局限在对象里。对类和其他对象无影响
# House.door = "yellow"
# print(f'中国风的房子{china_house.door}')
# china_house.door = 'pink'
# print(f'中国风的房子{china_house.door}')
# print(f'北欧风的房子{north_house.door}')
# print(f'类的属性{House.door}')
# # # output:
# # 中国风的房子yellow
# # 中国风的房子pink
# # 北欧风的房子yellow
# # 类的属性yellow
#
