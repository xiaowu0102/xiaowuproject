"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

# 定义一个fight函数
def fight():

# 定义四个变量，分别为我的血量，我的攻击力，你的血量，你的攻击力
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 100
# while True死循环， 若不退出，命令会一直执行
    while True:

        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
# if..elif语句判断
        if my_hp <= 0:
# 当我的血量小于等于0时，打印我的血量，你的血量和结果
            print("我的血量为：",my_hp)
            print("你的血量为：",your_hp)
            print("你赢了！")
# break 退出循环
            break
# 当你的血量小于等于0时，打印我的血量，你的血量和结果
        elif your_hp <= 0:
            print("我的血量为：", my_hp)
            print("你的血量为：", your_hp)
            print("我赢了！")
# break 退出循环
            break

# 调用fight函数
fight()


