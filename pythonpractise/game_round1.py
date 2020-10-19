"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp少，那么谁就输了
"""
#  定义一个fight函数
def fight():
#  定义四个变量，分别为我的血量，我的攻击力，你的血量，你的攻击力
    my_hp = 1000
    your_hp = 1000
    my_power = 200
    your_power = 200
# 经过一个回合后，我的血量和你的血量
    my_final_hp = my_hp - your_power
    your_final_hp = your_hp - my_power

# 通过if...elif...else语句来进行剩余血量及胜负的判断
    if my_final_hp > your_final_hp:
        print("我的剩余血量是：", my_final_hp)
        print("你的剩余血量是：", your_final_hp)
        print("我赢了！")
    elif my_final_hp < your_final_hp:
        print("我的剩余血量是：", my_final_hp)
        print("你的剩余血量是：", your_final_hp)
        print("你赢了！")
    else:
        print("我的剩余血量是：", my_final_hp)
        print("你的剩余血量是：", your_final_hp)
        print("我们这次打平，下次再分胜负")

# 调用fight函数
fight()


