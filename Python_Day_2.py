#python默认文件编码是utf-8，也可以通过一下方式指定文件编码：# -*- coding: 编码 -*-


#标识符
#--以字母或者_开头，其余部分由字母、数字、_组成
#--标识符对大小写敏感
#--python3中，非ASCII标识符也是允许的
a=5
_a=10
_1 = 12


#保留字/关键字
#--不能用关键字作为标识符
#--python的标准库提供了一个keyword模块，可以输出当前版本的所有关键字
import keyword
print("output Python3 key words:\n",keyword.kwlist)

#变量
#--python中变量不需要声明，使用前必须赋，只有赋值后该变量才会被创建
#--python中变量没有类型，类型是指内存中对象的类型
#--等号（=）用来给变量赋值，变量名=值
count = 3       #整型
name = "runoob" #字符串
miles = 100.0   #浮点数
print(count, name, miles)
#--python允许同时给多变量赋值
a=b=c=5
print(a, b, c)#a、b、c三个变量被分配到相同的内存空间上，即a、b、c指向同一块内存空间
#--可以为多个对象指定多个变量
a,b,c = 1, 2, "runoob"
print(a, b, c)
#--一个变量可以通过赋值指向不同类型的对象
a = c
print(a)
#--指定一个值时，对象会被创建
#--可以使用del语句来删除对象引用
del a
del b, c
#print(a, b, c)#实用已经del的变量将导致错误

#标准数据类型
#--python中有6个标准的数据类型
#   Number      数字
#   String      字符串
#   List        列表
#   Tuple      元组
#   Sets        集合
#   Dictionary  字典
#--String、List、Tuple都属于sequence(序列)

print('-'*8, "Nmuber", '-'*8)
#Number（数字）
#--python3支持int（整形）、float(浮点数)、bool（布尔型）、complex（复数）
#--python3中，只有一种整形int，表示未长整形，没有python2中的Long
#--内置的type()函数来查询变量所指的对象类型,也可以用isinstance来判断
aa, bb, cc, dd = 20, 5.5, True, 4 + 3j
print(type(aa), type(bb), type(cc), type(dd))
print(isinstance(aa, int))

#--type()与isinstance的区别：type()不会认为子类是一种父类类型，isinstance()会认为子类是一种父类类型
class A:
    pass

class B(A):
    pass
print(isinstance(A(), A), type(A()) == A)
print(isinstance(B(), B), type(B()) == A)
#--python2中没有布尔型，用数字1表示True，0表示False.
#--python3中，True和False定义为关键字，但它们的值还是1和0，可以和数字相加
print(True+2)
#--数值的除法总是返回一个浮点数，要获取整数实用//操作符
print(3/2)
print(3//2)
#在混合计算时，python会吧整形转换为浮点数
print(5.0 + 4/1.5 + 5)
#python还支持复数，可以用a+bj或者complex(a,b)表示，复数的实部和虚部都是浮点数
print(3+0.5j, 3.14j, 1+0j)

print('-'*8, "String", '-'*8)
#String（字符串）
#--以单引号（'）或者双引号（"）括起来，同时使用反斜杠（\）转义特殊字符
#--字符串截取格式：变量名[开始下标:结束下标]，索引值以0开始，-1表示从末尾开始
#--加号（+）是字符串的链接符
#--星号（*）表示复制当前字符串，紧跟的数字表示复制的次数
str = "rundoo"
print(str)
print(str[0:-1])    #输出第一个到倒数第二个的所有字符
print(str[0])       #输出字符串的第一个字符
print(str[2:5])     #输出从第三个开始到第五个字符
print(str[2:])      #输出从第三个开始后的所有字符
print(str*2)        #复制str2次
print(str+'test')   #连接字符串
#--在字符串前添加一个r，表示原始字符串，原始字符串中的转义字符失效
print(r"run\ndoo")
#--python没有单独的字符类型，一个字符就是长度为1的字符串
#--python中字符串不能被改变，向一个索引位置赋值，比如word[0]='m'，会导致错误
#--python字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
#--3个单引号或3个双引号允许一个字符串跨多行，且字符串中可以包含换行符、制表符以及其他特殊符号
#--3个引号表示的字符串自始至终保持字符串的格式（所见即所得）
para_str = """这个是多行字符串\n
这个是多行字符串
这个是多行字符串
"""
print(para_str)

print('-'*8, "List", '-'*8)
#List（列表）
#--使用最频繁的数据类型
#--列表中元素的类型可以不相同，支持数字、字符串甚至可以包含列表（嵌套）
#--列表是写在方括号（[]）之间，用逗号（,）分隔元素
#--列表可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
#--列表截取语法格式：变量名[开始下标:结束下标]，索引从0开始，-1表示末尾的开始位置
#--加号（+）是列表连接运算符，星号（*）是重复操作
#--列表的元素可以被改变
#--List内置了很多方法，例如append(), pop()等等
#--List使用del来删除元素
list = ['abc', 89, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list + tinylist)
list[1] = 100
del list[4]
print(list)

print('-'*8, "Tuple", '-'*8)
#Tuple（元组）
#--元组写在小括号（()）里，元素之间用逗号隔开
#--元组中的元素不能被改变，元素可以是不同的类型，可以包含可变的对象，比如列表
#--元组可以被索引和截取，方式同字符串和列表
list = [3+1j, 'abcdefg']
tuple = ('abc', 789, 2.23, 'runoob', 60.5, list)
tinytuple = (123, 'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)
list[1] = 'xyz'
print(tuple)
#--构造包含0个或1个元素的元组比较特殊
tup1 = () #空元组
tup2 = (20,) #一个元素，需要在元素后添加逗号
#--一般来说，函数返回值为一个，需要返回多个值时，可以用元组方式返回
def exampleReturnTuple(a,b):
    return (a,b)
print(type(exampleReturnTuple(3, 4)))
#--python中函数可以接受可变长参数，比如以*开头的参数名，会将所有参数收集到一个元组中
def testParam(*args):
    print(args)
    return args
print(type(testParam(1,2,3,4)))

print('-'*8, "Set", '-'*8)
#Set（集合）
#--集合时一个无序不重复元素的序列
#--基本功能时进行成员关系测试和删除重复元素
#--可以使用大括号{}或set()函数构造创建集合
#--创建一个空集合必须用set()，而不是{ }，因为{ }用来创建一个空字典
student = {'Tom', 'Jim', 'Mary', "Jack", 'Rose'}
print(student)

#成员测试
if('Rose' in student):
    print("Rose在集合中")
else:
    print("Rose不在集合中")

#set可以进行集合运算
setA = set('abcdefg')
setB = set('adgkjl')
print(setA, '\t', setB)
print(setA - setB) #差集
print(setA | setB) #并集
print(setA & setB) #交集
print(setA ^ setB) #两个集合中不同时存在的元素

print('-'*8, "Dictionary", '-'*8)
#Dictionary（字典）
#--字典是无序的对象集合，通过键来存取，不是通过偏移存取
#--字典是一种映射，用大括号{}标识，是一个无序的键(key):值(value)对集合
#--键必须使用不可变类型
#--同一个字典中，key必须时唯一的
#--使用del可以删除一个字典，clear()可以清空字典
dicti = {}
dicti['one'] = '1 - 菜鸟工具'
dicti[2] = "2 - 菜鸟教程"
tinydict = {'name' : "runoob", 'code' : 1, "site" : 'www.runoob.com'}
print(dicti['one'])
print(dicti[2])
print(tinydict)
print(tinydict.keys())      # 输出所有key
print(tinydict.values())    # 输出所有值
#--构造函数dict()可以直接从键值对序列中构建字典
print(dict([('runoob', 1), ('google', 2), ("taobao", 3)]))
print(dict(runoob = 1, goole = 2, taobao = 3))
dicti.clear()
print(dicti)
#--字典内部使用了散列表（hashtable）的算法，不管字典有多少项，in操作符花费的时间都差不多

print('-'*8, "数据类型转换", '-'*8)
#数据类型转换
#--只需要将数据类型作为函数名即可
del str
print(int(2.5))
print(str(3))
print(str(3.5))
print(str([3,'2aa', 4.5]))
print(hex(15))#转换为十六进制
print(oct(15))#转换为八进制
print(bin(3))#转换未二进制