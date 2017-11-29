#!/usr/local/bin/python3
#filename:Python_Day_t.py

#类（class）
#--定义格式：
#   class classname[(modulename.baseclassname, baseclassname2,...baseclassnamen)]:
#        <statement_1>
#           ...
#       <statement_n>
#--类的属性默认都是公开的(public)，私有属性都是以__开头的属性，私有属性不能在类外部使用
#--类对象支持两种操作：属性引用和实例化
#--属性引用语法：obj.name
#--类的方法使用def关键字定义
#--类的方法必须有一个额外的第一个参数名称，按照惯例它的名称是self，这个名称可以改为其他任意名字
#--构造函数：__init__(),可以有参数，参数通过__init__()传递到类的实例化操作上
#--析构函数：__del__()
#--私有方法：以__开头的函数
class Pepole:
    name = ""
    age = 0
    __weigth = 0#私有属性
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁"%(self.name, self.age))
    def __del__(self):
        name = ""
        age = 0
        __weight = 0
    def __walk(self):#私有方法
        print(self.name,"在走路")    

p = Pepole("runoob", 10, 30)
p.speak()
del p

#--类继承：python支持单继承和多继承
#--方法重写：在子类重覆盖父类的方法
#--类专有方法：
#   __init__ __del__ __repr__ __setitem__ __getitem__ __len__ __cmp__ 
#   __call__ __add__ __sub__ __mul__ __div__ __mod__ __pow__
class Human:
    gender = 0
    def __init__(self,g):
        self.gender = g
class Male(Human):
    def __init__(self):
        Human.__init__(self, 1)
m = Male()
print(m.gender)        

class Behavior:
    type = ""
    def __init__(self,t):
        self.type = t
    def printinfo(self):
        print("behavior:", type)

class Student(Human,Behavior):
    name = ""
    def __init__(self,n,g,t):
        self.name = n
        Human.__init__(self, g)
        Behavior.__init__(self, t)        
    def printinfo(self):#重写父类方法
        print(self.name, "gender:", self.gender, "behavior:", self.type)
    def __str__(self):
        return "%s gender:%d behavior:%s"%(self.name, self.gender, self.type)        


stu = Student("Bob", 1, "walking")
stu.printinfo()
print(stu)



