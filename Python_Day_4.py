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