# 函数的定义
def game():
    my_hp = 2000
    your_hp = 2001
    while True:
        my_power = 200
        your_power = 199
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        print(my_hp)
        print(your_hp)
        if my_hp <= 0:
            print("你赢了")
            break
        elif your_hp <= 0:
            print("我赢了")
            break

# 函数的调用
game()
