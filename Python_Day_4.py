#Day 4

#if语句
#--一般形式：
#   if condition_1:
#       statement_block_1
#   elif condition_2:
#       statement_block_2
#   else:
#       statement_block_3

#--python中用elif替代了else if
#--pyton中没有switch - case
#--使用缩紧来划分语句块，相同缩紧数的语句在一起组成一个语句块
#--可以嵌套if语句
num = 4#int(input("输入一个数字："))
if(num % 2 == 0):
    if(num % 3 == 0):
        print(num,"可以整除2和3")
    else:
        print(num, "可以整除2，但不能整除3")
else:
    if(num % 3 == 0):
        print(num, "可以整除3，但不能整除2")
    else:
        print(num, "不能整除2和3")            

#循环语句
#--while循环
#--一般形式：
#   while condition:
#       语句块
#--python中没有do...while循环
#--通过设置condition永远为true来实现无限循环，无限循环在服务器和客户端的实时请求非常有用
n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
print("1到%d之和为：%d"%(n, sum))    

#--while循环使用else语句，在condition为false时执行else的语句块,并终止循环
count = 0
while count < 5:
    print(count,"< 5")
    count += 1
else:
    print(count, ">= 5")    
#--如果while循环体中只有一条语句，可以将该语句和while写在同一行中

#--for循环
#--一般形式：
#   for <variable> in <sequence>:
#       <statements>
#   else:
#       <statements>
#--for循环中，可以使用break跳出当前循环体
sites = ["baidu","google", "runoob", "taobao"]
for site in sites:
    if site == "runoob":
        print("菜鸟教程")
        break
    print(site)
else:
    print("没有循环数据")
print("完成循环")        
#--结合range()和len()可以遍历一个序列
for i in range(len(sites)):
    print(sites[i])

#--break语句可以跳出for循环与while循环的循环体
#--如果从for循环或while循环中终止，任何对应的循环else块将不执行
#--continue语句被用来告诉python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
for letter in "runoob":
    if letter == 'o':
        continue
    print(letter)
#--循环语句可以有else子句，它在穷尽列表（for循环）或条件变为false（while循环）导致循环终止时被执行，
#  但循环被break终止时不执行
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", n//x)
            break
    else:
        print(n, "是质数")        

#pass语句
#--pass语句时空语句，是为了保持程序结构的完整性，防止语法错误
#--pass不做任何事情，一般用做占位语句
for letter in 'runoob':
    if letter == 'o':
        pass
        print("执行pass块")
    print('当前字母：', letter)
print("loop done")        

#迭代器
#--迭代器时访问集合元素的一种方式
#--迭代器只能往前不能后退
#--迭代器两个基本方法iter()和next()
#--字符串、列表或元组都可以用于创建迭代器
array = [1, 2, 3, 4]
it = iter(array)
print(next(it))
print(next(it))

it2 = iter(array)
for x in it2:
    print(x, end=" ")

import sys
it3 = iter(array)
while True:
    try:
        print(next(it3),end=" ")
    except StopIteration:
        #sys.exit()
        break

#生成器
#--python中，使用了yield的函数被称为生成器（generator）
#--生成器是一个返回迭代器的函数，只能用于迭代操作
#--在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，
#  并在下次执行next()方法时从当前位置继续运行
def fibonacci(n):
    a, b, counter = 0, 1,0
    while True:
        if(counter > n):
            return 
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)
print("\n",type(f))

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        #sys.exit()            
        break

#函数
#--函数是组织好的，可重复使用的，用来实现单一功能，或相关联功能的代码段
#--函数能提高应用的模块性，和代码的重复利用率
#--函数代码块以def关键字开头，后接函数标识符和圆括号()
#--任何传入参数和自变量必须放在圆括号内，圆括号之间可以用于定义参数
#--函数的第一行可以选择性地实用文档字符串，用于存放函数说明
#--函数内容以冒号开始，并且缩紧
#--return [表达式]结束函数，选择性地返回一个值给调用方，不带表达式的return相当于返回None
#--一般格式：
#   def functionname(arguments):
#       fuction block
#--默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配
def Hello():
    print("Hello, world!")

Hello()#调用Hello函数

def area(width, height):
    return width * height

print(area(10, 5))#调用area函数并输出返回值

#参数传递：
#   按值传递：不可变类型，字符串、数字、元组
#   按引用传递：可变类型，列表，字典、集合
def changeInt(args):
    args = 10

temp = 2
print("temp = ", temp, end=" ")
changeInt(temp)
print("temp = ", temp)

#--函数参数类型：必需参数、关键字参数、默认参数、不定长参数
#--必需参数：必须以正确的顺序传人函数，调用时的数量必须和声明时的一样
#--关键字参数：关键字参数与函数调用关系紧密，函数调用使用关键字参数来确定传人的参数值
#  使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为python解释器能够用参数名匹配参数
def printme(str, str2):
    print(str, str2);
    return ;
printme(str2="google", str = "runoob")
#--默认参数：调用函数时，如果没有传递参数，则会使用默认参数。在声明的参数列表中，使用等号进行指定默认值
#  默认参数必须放在函数参数列表的最后
def printinfo(name, age = 100):
    print("Name : ", name, " \t age : ", age)
    return
printinfo("google", 10)
printinfo("baidu")
#--不定长参数：参数个数不时固定的。声明时不会命名
#   def fuctionname([formal_args],*var_args_tuple)
#       function_suite
#       return [expression]
#--加了星号的变量名会存放所有未命名的变量参数。如果函数调用时没有指定参数，它将是一个空元组。也可以不向
#  函数传递未命名的变量
def printinfo(arg1, *vartuple):
    print("output:")
    print(arg1);
    for var in vartuple:
        print(var)
    return;
printinfo(10)
printinfo(70, 60, 50)

#匿名函数
#--python使用lambda表达式来创建匿名函数
#--lambda表达式只是一个表达式，函数体比def简单很多
#--lambda表达式主体是一个表达式，不是代码块，仅仅能在lamda表达式中封装有限的逻辑
#--lambda表达式拥有自己命名空间，且不能访问子句参数列表以外或全局命名空间里的参数
#--一般形式：
#   lambda 【arg1，[arg2, ... , argn]]:expression
s = lambda arg1, arg2: arg1 + arg2;
print(s(10, 11))

#return语句
#--return [表达式]语句用于退出函数

#变量作用域
#--变量的访问权限取决于变量在哪里赋值，即变量的作用域决定了哪一部分程序可以访问哪个特定的变量名称
#--python的作用域有4中：Local(局部作用域)、Enclosing(闭包函数外的函数中)、Global(全局作用域)、Built-in(内建作用域)
#--python变量查找规则：L->E->G->B。
#--python中只有模块(module)、类（class）以及函数（def、lambda）才会引入新的作用域，其他代码块不会引入新的作用域
#--局部变量：定义在函数内部的变量拥有一个局部作用域。局部变量只能在其被声明的函数内访问
#--全局变量：可以在整个程序范围内访问。

#global与nonlocal关键字
#--当内部作用域修改外部作用域的变量时，就要用到glocal和nonlocal关键字
num = 1
def fun1():
    global num #需要使用global关键字声明
    print(num)
    num = 123
    print(num)
    return
fun1()
#--如果要修改嵌套作用域中变量则需要nonlocal关键字
def outer():
    n = 10
    def inner():
        nonlocal n
        print(n)
        n = 100
        print(n)
        return
    inner()
    print(n)
    return
outer()

