# 定义一个fight函数，传入当前回合我的血量，我的攻击力，敌人的血量，敌人的攻击力
# 返回这次回合之后，我的血量，敌人的血量
def fight(my_hp, my_power, your_hp, your_power):
    my_hp = my_hp - your_power
    your_hp = your_hp - my_power
    return my_hp, your_hp


# 定义游戏
def game():
    # 初始化
    my_hp = 1200
    my_power = 11
    your_hp = 1000
    your_power = 12
    # 回合开始
    i= 0
    while True:
        i += 1
        a = fight(my_hp, my_power, your_hp, your_power)
        my_hp = a[0]
        your_hp = a[1]
        print(my_hp, your_hp)
        # 当前回合之后，判断胜负
        if my_hp > your_hp:
            print("第%d局我赢了" % i)
        elif my_hp < your_hp:
            print("第%d局你赢了" % i)
        else:
            print("第%d局打平了" % i)
        # 如果我活着敌人某一方血量小于等于0，退出战斗
        if my_hp <= 0 or your_hp <= 0:
            break

# 调用游戏，开始战斗
game()
