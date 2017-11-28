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
