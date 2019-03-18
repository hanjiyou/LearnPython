# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-15 17:24:31
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-18 19:50:14

def this_fails():
 x=1/0
try:
 this_fails()
except ZeroDivisionError as err:
 print("Handling run-time error:",err)
 #raise#抛出异常
else:
 print('执行else')
finally:#定义了无论在任何情况下都会执行的清理行为
 print('finally')

def divide(x,y):
 print('--------------')
 try:
  result=x/y
 except ZeroDivisionError:
  print('division by zero')
 else:
  print('没有异常 result is',result)
 finally:
  print('执行finally')
divide(2,1)
divide(2,0)
#divide('2','1')

#预定义清理行为
with open('fist.txt') as f:#with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
 for line in f:
  print(line,end=' ')
print('end')

