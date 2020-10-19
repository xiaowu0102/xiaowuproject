'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
# 模块化，导入TongLao类
from python_oo.tonglao import TongLao

# 定义一个XuZhu类，继承TongLao
class XuZhu(TongLao):

    #定义一个read方法
    def read(self):
        print("罪过罪过")
# 实例化类XuZhu，传入父类的参数
xuzhu = XuZhu(1000,100)
# 调用子类XuZhu的read方法
xuzhu.read()
# 为什么调用子类的read方法，执行命令后父类的所有方法都被调用了？？？