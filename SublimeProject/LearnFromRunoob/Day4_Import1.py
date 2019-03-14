# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-14 17:08:40
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-14 17:36:06
print('this is import1')
def print_func(str):
 print('hello:',str)
 return
print('__name__=',__name__)#每个模块都有的内置属性__name__
if __name__=='__main__':
 print('程序在自身运行')
else:
 print("来自另一个模块")
mylist=[1,2,3,4]
def myfun2():
 print("myfun2")