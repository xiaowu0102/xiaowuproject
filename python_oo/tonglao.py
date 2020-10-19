'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
# 定义一个TongLao类
class TongLao:
    # 定义童姥的两个属性，血量和武力值，通过参数传入
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
    # 定义童姥的see_people方法，传入一个name参数
    def see_people(self, name):
        # 如果传入"无崖子"，打印“师弟！！！！”
        if name == "无崖子":
            print("师弟！！！！")
        # 如果传入“李秋水”，打印“呸，贱人”
        elif name == "李秋水":
            print("呸，贱人")
        # 如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif name == "丁春秋":
            print("叛徒！我杀了你")
    # 定义fight_zms方法，敌人的血量和武力值通过参数传入
    def fight_zms(self,enemy_hp,enemy_power):
        # 调用天山折梅手方法，将童姥的血量减半，武力值提升10倍
        self.hp = int(self.hp / 2)
        self.power = self.power * 10
        # 进行一回合制打斗后童姥的血量和敌人的血量
        my_final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        # 判断打斗结果
        if my_final_hp < enemy_final_hp:
            print(f"童姥最后的血量是{my_final_hp},敌人最后的血量是{enemy_final_hp}")
            print("童姥输了")
        elif my_final_hp > enemy_final_hp:
            print(f"童姥最后的血量是{my_final_hp},敌人最后的血量是{enemy_final_hp}")
            print("童姥赢了")
        else:
            print("平局，下次再战。")

# 实例化类，传入童姥的hp和power
tonglao = TongLao(1000, 100)
# 调用TongLao的see_people方法，传入“李秋水”
tonglao.see_people("李秋水")
# 调用TongLao的fight_zms方法，传入敌人的hp和power
tonglao.fight_zms(1000, 100)
