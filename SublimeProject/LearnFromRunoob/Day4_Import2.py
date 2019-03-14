# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-14 17:08:40
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-14 20:01:15
import Day4_Import1#导入自定义的py文件
Day4_Import1.print_func("传入参数")#调用自定义的方法
import sys
#print('sys.path=',sys.path)
#import sys
print(dir(Day4_Import1))#内置函数dir()可以找到指定模块内定义的所有名称
print(dir())#不指定参数返回当前模块的所有名称
