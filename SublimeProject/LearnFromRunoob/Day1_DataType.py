# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-08 11:32:44
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-08 19:54:26

print("hello,world222");#注释1

print("hello,world333");#单行注释1

"""#多行注释也可以用'''
6a
azxc
print("haha")
"""

if True:#python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}
 print("True")
else:
 print("false")#缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数 不同会报错

#int numbers1 3;
print(r"this is \n 666");#r相当于C#中的@
print("""abm.GetAllDependencies
 asd""")
num=3;
print(num);
str='abcdefghijklmn'
print(str)
print(str[2:-3])#str两种索引方式①从左到右从0开始 ②从右到做从-1开始
print(str[-1])
print(str[2:4])
print(str*2)
print(str+"\t哈哈哈")

#input("\n\n 按下enter后退出")
import sys;x='runoob';sys.stdout.write(x+'\n')

#控制输出不换行
print(2,end="|")
print(21)

#测试导入
#print('===========python import mode')
'''
import sys
print('命令行参数为')
for x in sys.argv:
 print(x)
pass
#print('路径为:',sys.path)
'''
print("-----------------------------------------")
from sys import argv,path;
#print(argv,path)
#基本数据类型
a=b=c=1#为多个变量赋一个值
print(a,b,c)
a,b,c,d=1,2.5,False,1+2j #同事为多个变量分别赋值
print(a,b,c,d)
print(type(a),type(b),type(c),type(d))

a=111
print(isinstance(a,float));
del a;
#print(a)
print(4/2);
print(4//2);
print(2%4)
print(2**2)


#List类型
list=['abc',123,"666",False]
print(list[1:2])
list[0:2]=[]
print(list)
letters=['1',"2","3","4","5","6"]
print(letters[1:6:1])

#Tuple元组
tup=(1,)
print(tup[0])
#print(tup[1:3])
#tup[0]='a'
tup2=(2,3)
print(tup+tup2)

#Set集合
set1=set()
print(type(set1))
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉
if "Rose" in student:
 print("rose在其中")
else:
 print("rose不在")
 print("rose不在2")
a = {'a','b','d','c'}
#set(a)
#b = set('alacazam')
print(type(a))
# set可以进行集合运算
a = set('abcde')
b = set('abcl')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

#字典
myDict={}
myDict['one']=1
myDict[2]="two"
myDict[('1','2')]=('11234',"112")#元组作为key和value
myDict["set集合"]={"set1","set2","set2"}#set集合作为value
myDict["Dict字典"]={"name":"汉就业","age":12}#字典作为字典的value
print("myDict=",myDict)
print("myDict.keys=",myDict.keys())
print("myDict.values=",myDict.values())
print(type(myDict[('1','2')]))
print(type(myDict["set集合"]))
print(type(myDict["Dict字典"]))
a=()
print("()的类型是",type(a))
b={}
print("{}的类型是",type(b))
c=set()
print("set()的类型是",type(c))
myDict=dict([('one',"value1"),("two","value2")])
print(myDict)
a=()
print(a)
print(type(a))

#数据类型转换
x='3.5'
x=float(x)
print('字符1的调用int转换类型:',type(x))
x=int('35',16)#第一个参数是输入的整数 第二个参数是第一个参数的进制 即(12,8)12是8进制 返回值是10进制
print('x=',x)
x=set('abc')
print('x的类型:',type(x))