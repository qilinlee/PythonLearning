#!/usr/local/bin/python3
#filename:Python_Day_7.py

#模块
#--模块是一个包含所有你定义的函数和变量的文件，后缀名为.py。
#--模块可以被别的程序引入，以使用该模块中的函数等功能，这也是使用python标准库的方法。
#--引入模块语句：import [module1[,module2[,...moduleN]]]
#--当解释器遇到import语句，如果模块在当前搜索路径中就会被导入。一个模块只会导入一次，不管执行了多少次import。
#--搜索路径是一个解释器会先进行搜索的所有目录的列表。搜素路径是在python安装或编译的时候确定的，安装新的库应该
#  也会修改。搜索路径存储在sys模块中的path变量
#--每个模块都有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用。被导入的模块的名称将被放入当前操作的模块的符号表中
import sys
print("console args:")
for i in sys.argv:
    print(i)

print("python path:", sys.path)
#--from...import语句可以从模块中导入一个指定的部分到当前命名空间
#--from...import *语句可以将一个模块的所有内容导入到当前命名空间中

#包
#--包是一种管理python模块命名空间的形式，采用“点模块名称”，如：A.B表示一个包A中的子模块B
#--在导入一个包的时候，python会更具sys.path中的目录来搜素这个包中包含的子目录
#--目录只有包含一个叫做__init__.py的文件才会被认做是一个包。最简单的情况，放入一个空的——__init__.py就可以了。
#  但让这个文件中也可以包含一些初始化代码或者为—__all__变量赋值
#--用户可以每次只导入一个包里面的特定模块
import sound.effects.echo
from sound.effects import echo
