# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-19 19:45:37
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-19 19:58:53
print('-------------------------判断质数')
for i in range(2,15):
 for j in range(2,i):
  if i%j==0:
   print(i,'不是质数')
   break
 else:#如果内层循环走完了也没找到可除尽的数，则是质数
  print(i,'是质数')

print('-------------------------try-catch')
def is_number(s):
 try:
  print(float(s))#float()构造函数 将指定参数解析并返回为float类型，如果参数不匹配转换错误会报错并中断
  return True
 except ValueError as err:
  print('try1捕获到异常:',err)
  pass
 print('继续执行try2')
 try:
  import unicodedata
  print(unicodedata.numeric(s))#解析指定字符串返回其对应的float类型的数字
  print('s.type=',type(unicodedata.numeric(s)))
  return True#使用unicodedata模块的numberic函数
 except(TypeError ,ValueError ) as err:
  print('try2捕获到异常:',err)
 return False

print(is_number('啊'))
print(is_number('二'))

print('-------------------------闰年')
for i in [1900,2000,2004,2010]:
    if i%100==0:
      if i%400==0:#百整年能被400整除是闰
        print('{0}是闰年'.format(i))
      else:
        print('{0}不是闰年'.format(i))
    else:#非百整年
      if i%4==0:
        print('%d是闰年'%(i))
      else:
        print('%d不是'%(i))

print('-------------------------阶乘')
sourcenum=5
num=1
for x in range(1,sourcenum+1):
    num=num*x
print('num的阶乘为=',num)

print('-------------------------进制转换')
dec=15
print('十进制dec=',dec)
print('二进制bin()',bin(dec))
print('8进制oct()',oct(dec))
print('16进制hex()',hex(dec))
oct=0o7#python8进制表示方式
hex=0xaaa#16进制
bin=0b1#二进制

print('-------------------------递归函数')
def myfunc(num):
  result=1
  if(num>1):
    result=num*myfunc(num-1)
  return result
print(myfunc(5))