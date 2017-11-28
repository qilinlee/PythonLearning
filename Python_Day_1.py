import platform
import keyword
print("Hello world")
print(2+3)
#输出python版本号
#--需要improt platform
print(platform.python_version())

#输出python的关键字
#--需要import keyword
print(keyword.kwlist)


#行与缩进
#--同一个代码块必须使用相同的缩进
#--否则将导致错误
if True:
    print("true")
else:
    print("false")
print("End")

#多行语句
#--python通常一行写完一条语句，若写不完，使用\来换行
total = 1+ 2+\
    3+4+\
    5+6+7
print(total)
#--在[],{},()中不用\,也能实现多行语句
array = ['item_one',
'item_two','item_three',
'item_four']
print(array)

#字符串
#--用单引号或者双引号表示字符串，字符串是不可变的
print('abcd')
print("efg")
#--连续3个引号可以指定一个多行字符串
print("""abcd
efg
hijk""")
#--转移符师'\'
print('\nabc')
#--以r或R开始的字符串表示自然字符串，转移符将失效
print(r"abcd\nefg")
#--以u或U开头的字符串表示unicode字符串
print(u"abcdefg")

#等待用户输入
#input("\n\n按下任意键退出")

#同一行显示多条语句
#--语句间使用分号（;）分隔
print("abcd");print("efg")

#print输出
#--print默认输出换行，若要不换行，在变量末尾添加 end=""
print("abc");print("efg", end="");print("hijk")

#import与from...import
#在 python 用 import 或者 from...import 来导入相应的模块。
#将整个模块(somemodule)导入，格式为： import somemodule
#从某个模块中导入某个函数,格式为： from somemodule import somefunction
#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为： from somemodule import *
from sys import argv,path
print("==========python from...import============")
print('path:',path)# 因为已经导入path成员，所以此处引用时不需要加sys.path

#注释
#--以#开头表示单行注释
#--多行注释用三个单引号'''或者三个双引号"""将注释内容包围起来
#e.g.
'''
这是一个多行注释
这是一个多行注释
这是一个多行注释
‘’‘
"""
这是一个多行注释
这是一个多行注释
这是一个多行注释
"""