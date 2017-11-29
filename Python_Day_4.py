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

