#!/usr/local/bin/python3
#filename:Python_Day_6.py

def GetCurPath():
    file_path = __file__
    print(file_path)
    rindex = file_path.rindex('/')
    if-1 != rindex:
        return file_path[0:rindex]
    return ""


#错误
#--python有两种错误：语法错误和异常
#--语法错误又称为解析错误
#--异常：运行期检测到的错误。大多数异常都不会被程序处理。
#--异常处理try:...except:...,首先执行try子句，如果没有异常发生，忽略except子句，try子句执行后结束
#  如果在执行try子句发生异常，那么try子句余下部分将忽略。如果异常类型和except之后的名称一致，那么
#  对应的except子句将被执行，最后执行try语句之后的代码
#  如果一个异常没有与任何except子句匹配，那么这个异常将会传递给上层
#--一个try语句可以包含多个except子句，分别处理不同的特定异常，最大只有一个分支被执行
#--一个except子句可以同时处理多个异常，这些异常将被放在一个大括号里面成为一个元组
#--最后一个except子句可以忽略异常名称，将被当作通配符使用。可以使用这种方法打印一个错误信息，然后再
#  次把异常0抛出
import sys
try:
    f = open(GetCurPath()+'/myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer")
except:
    print("Unexcpeted error:", sys.exc_info()[0])
    raise            
#--try except语句还有一个else子句，如果使用这个子句，那么必须放在所有except子句之后。这个子句奖在try子
#  句没有发生任何异常的时候执行
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except IOError:
        print("cannot open", arg)
    else:
        print(arg, "has", len(f.readlines()),'lines')
        f.close()
#--使用else子句比吧所有语句都放在try子句中要好，这样可以避免一些意想不到的，而except又无法捕获的异常
#--异常处理不仅仅处理那些直接发生在try子句中的异常，而且还可以处理子句中调用的函数（甚至间接调用的函数）里
#  抛出的异常
def this_fails():
    x = 1/0
    return

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)    
#--python使用raise语句抛出一个指定的异常，唯一的一个参数指定要抛出的异常，它必须是一个异常的实例或者异
#  常的类（Exception的子类）
#raise NameError("HiThree")

#用户自定义异常
#--可以创建一个新的Exception类，或者直接继承，或者间接继承
#--当创建一个模块有可能抛出多种不同的异常，一种通常的做法是为这个包创建一个基础异常类，然后基于这个类为不
#  同的错误情况创建不同的子类
#--大多数异常的名字都以Error结尾，就跟标准命名一样
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print("My exception occured, value:", e.value)            
#raise MyError("oops!")

#定义清理行为
#--try子句还有另外一个可选子句finally，他定义无论任何情况下都会执行的清理行为
#--如果异常在try子句（或者在excpet子句或else子句）被抛出，而又没有任何excpet
#  捕获，那么这个异常会在finally子句执行后再次被抛出
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print("catch exception")
finally:
    print("goodbye, world!")    
 
 #预定义的清理行为
 #--一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它，那么这
 #  个标准的清理行为就会执行
 #--关键词with语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行清理方法
with open(GetCurPath()+'/myfile.txt') as f:
     for line in f:
        print(line, end=" ")
    