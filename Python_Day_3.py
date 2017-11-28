#Day 3

a, b = 10, 21
c = 2

print('-'*15, "算数运算符", '-'*15)
#算数运算符
#--加（+）、减（-）、乘（*）、除（/）、取模（%）、幂（**）、取整取法（//）
print(a + b, a - b, a * b, a / b, b % a, a ** b, a // b)

print('-'*15, "比较运算符", '-'*15)
#比较运算符
#-- 等于（==）、不等于（!=）、大于（>）、小于（<）、大于等于（>=）、小于等于（<=）
print( a == b, a != b, a > b, a < b, a >= b, a <= b)

print('-'*15, "赋值运算符", '-'*15)
#赋值运算符
#-- =、+=、-=、*=、/=、%=、**=、//=
c += a
print(c)
c -= a
print(c)
c *= a
print(c)
c /= a
print(c)
c %= a
print(c)
c //= a
print(c)

print('-'*15, "赋值运算符", '-'*15)
#位运算符
#-- 按位与（&）、按位或（|）、按位异或（^）、按位取反（～）、左移（<<）、右移（>>）
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
print(a&b, a|b, a^b, ~a, a<<2, a>>2)

print('-'*15, "逻辑运算符", '-'*15)
#逻辑运算符
#--逻辑与（and）、逻辑或（or）、逻辑非（not）
print(a and b, False and True, False and False, True and True, True and False)
print(a or b, False or True, False or False, True or True, True or False)
print(not a, not False, not True)

print('-'*15, "成员运算符", '-'*15)
#成员运算符
#-- in：如果在指定的序列中找到值返回True，否则返回False
#-- not in：如果在指定的序列中没有找到值返回True，否则返回False
array = [1, 2, 3, 4, 5]
if(a in array):
    print(a,"在序列", array, "中")
else:
    print(a,"不在序列", array, "中")
a = 2
if(a in array):
    print(a,"在序列", array, "中")
else:
    print(a,"不在序列", array, "中")

print('-'*15, "身份运算符", '-'*15)
#身份运算符
#-- is：判断两个标识符是不是引用自同一个对象，相当于id(x) == id(y)
#-- is not：判断两个标识符是不是引用自不同对象，相当于id(x) != id(y)
#-- id()函数用于获取对象的内存地址
#-- is是判断两个变量引用对象是否为同一个，==判断引用变量的值是否相等
if(a is b):
    print("a与b指向同一个对象")
else:
    print("a与b指向不同的对象")

if(a is not b):
    print("a与b指向不同的对象")
else:
    print("a与b指向同一个对象")    

if(id(a) == id(b)):
    print("a与b指向同一个对象")
else:
    print("a与b指向不同的对象")

print('-'*15, "运算符优先级", '-'*15)
#运算符优先级
#-- 优先级         运算符                 描述
#--   1             **                  指数（幂）               --最高优先级          
#--   2            ～+-                 按位取反、正负号   
#--   3            */%//                乘、除、取模、取整除法
#--   4             +-                  加、减
#--   5            >><<                 左移、右移
#--   6             &                   按位与
#--   7             ^|                  按位异或、按位或
#--   8           <=<>>=                比较运算符
#--   9            == !=                等于、不等于
#--   10        = %= /= //= +=          赋值运算符
#                 -= *= **=                 
#--   11          is is not             身份运算符
#--   12         in not in              成员运算符
#--   13         not or and             逻辑运算符               