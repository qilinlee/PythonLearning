#!/usr/local/bin/python3
#filename:Python_Day_8.py

#Python3标准库

#操作系统接口：os模块
#--os模块提供了不少与操作系统相关的函数
import os
print(os.getcwd()) #返回当前的工作目录
print(dir(os))
if not os.path.exists("Data"):
    os.system("mkdir Data") #执行系统命令 mkdir
else:
    print("Data is exist")    
#--针对日常文件和目录管理任务，shutil模块提供了一个抑郁使用的高级接口
import shutil
shutil.copyfile("myfile.txt", "Data/myfile.txt")

#文件通配符：glob模块
#--glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
import glob
print(glob.glob("*.py"))

#错误输出重定向和程序终止
#--sys还有stdin、stdout和stderr属性，即使在stdout被重定向时，stderr也可以用于显示警告和错误信息
import sys
#sys.stderr.write("Warning,log file not found starting a new one\n")
#--大多脚本的定向终止都使用“sys.exit()”

#字符串正则匹配：re模块
#--re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配处理，正则表达式提供了简洁、优化的解决方案
import re
print(re.findall(r"\bf[a-z]*", "which foot or hand fell fastest"))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

#数学：math模块
#--math模块为浮点数运算提供了底层c函数库的访问
import math
print(math.cos(math.pi/4))
print(math.log(1024,2))

#随机数：random模块
#--random模块提供了随机数生成工具
import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)
random.random()
print(random.randrange(6))

#访问互联网
#--urllib.request：用于处理urls接受的数据
# from urllib.request import urlopen
# urls = urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl')
# print(urls)
# for line in urls:
#     line = line.decode('utf-8')
#     if 'EST'in line or 'EDT' in line:
#         print(line)
#--smtplib:发送电子邮件
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
r"""To:jcaesar@example.org
From:soothsayer@example.org
Beware tthe ideas of march.""")
server.quit()        
