'''
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
'''
# 1.定义一个Dog类
class Dog:
    # 属性： 颜色是黑色，品种是阿拉斯加
    color = "black"
    breed = "阿拉斯加"
    # 方法： 吃、喝、睡
    def eat(self):
        print("eating...")

    def drink(self):
        print("drinking...")

    def sleep(self):
        print("sleeping...")
# 打印狗的属性
print(Dog.color, Dog.breed)

# 实例化类
dog = Dog()
#调用类的方法
dog.eat()
dog.drink()
dog.sleep()

# 2.定义一个LiJing类
class LiJing:
    # 定义类的属性
    height = 190
    weight = 210
    # 定义类的方法
    def fight_ta(self):
        print("看我宝塔！")

    def fight_fight(self):
        print("近身搏斗！")

# 打印类的属性
print(LiJing.height,LiJing.weight)
# 实例化类并且调用类方法
people = LiJing()
people.fight_ta()
people.fight_fight()

# 3.定义一个NeZha子类，继承LiJing父类
class NeZha(LiJing):
    # 定义哪吒的属性
    appearance = "三头六臂"
    # 定义哪吒自己的方法
    def pk(self):
        print("看我混天绫，看我乾坤圈！")
    def fight_fight(self):
        print("找打")
# 直接调用父类的方法
        super().fight_fight()
nz = NeZha()
nz.pk()
nz.fight_fight()


# 4.定义一个People类，他需要吃、喝，吃和喝的东西用参数传入
class People:
    # 构造方法
    def eat(self,food):
        self.food = food
        print(f"他吃了{food}")

    def drink(self,drinkk):
        self.drinkk = drinkk
        print(f"他喝了{drinkk}")
# 实例化类，并且传入参数
person = People()
person.eat("KFC")
person.drink("可乐")
# 5.定义一个HuGe类，继承People类，并且有自己的方法
class HuGe(People):
    def acting(self):
        print("他出演仙剑奇侠传。")
#实例化类
huge = HuGe()
huge.acting()