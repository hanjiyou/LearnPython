# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-09 10:11:09
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-09 11:47:22

#数据类型复习
######1.Number:不可变
myInt1=111111111111111111
print("myInt1",myInt1)
myFloat1=1.1

myStr1='1.1'
myFloat2= float(myStr1)
print('myFloat2',type(myFloat2))
#数值运算
myInt1,myInt2=5,3
print('5/3=',myInt1/myInt2) #除法  得到一个浮点数
print('5//3=',myInt1//myInt2) #除法取整'//'
print('5%3=',myInt1%myInt2) #除法取余 '%'
print('myInt2的立方',myInt2**3)
myBool1=True;#bool值首字母大写
print('true*2=',myBool1*2)
#复数
myComplex1=1+2j;
print('myComplex1**2=',myComplex1*myComplex1)

del myInt1,myFloat1,myFloat2,myBool1,myComplex1,myStr1 #删除对象的引用
#print(myStr1) myStr1已经被删除引用 需要重新赋值

######2.字符串:不可变
#python中单双引号意义相同
myStr1,myStr2='strValue1','strValue2'
print('myStr1+myStr2=',myStr1+'-'+myStr2)#字符串拼接
print('myStr1[0]=',myStr1[0])#字符串从左到右索引从0开始 向右+1
print('myStr1[-1]=',myStr1[-1])#字符串从右到做索引从-1开始 向左-1
#字符串的截取
myStr1='abcdefghij'
print('myStr1[1:3]',myStr1[1:3])
print('myStr1[1:]',myStr1[1:])
print('myStr1[1:9:3',myStr1[1:9:3]) #截图1-9  步长为3 结果为beh
print('myStr1[1:-1]',myStr1[1:-1])
print('myStr1[-1:-4]',myStr1[-1:-4])#头衔必须在尾下标前面才截取得到内容
print('myStr1[-4:-1]',myStr1[-4:-1])
print('myStr1*2',myStr1*2)
#r字符取消特殊字符
print('第一行\n第二行')
print(r'第一行\n还是第1行')
#字符串不可以改变
#myStr1[0:4]='dcba'#修改字符串内容会报错 str不支持assingnment
print(myStr1)
del myStr1,myStr2

######3.List列表:可变 用[]创建
myList=[1,'2',"Three",'d']
print(myList)
#列表同样可以被索引和截取 以及通过'+'拼接
print('mylist[0=]',myList[0])
print('myList+myList',myList+myList)
myList2=myList*2;
print(myList2)
#列表中的元素可以改变
myList2[0:4]='dcbaaa'#通过字符串给挨个元素赋值 如果字符串长度超过指定的范围会从范围后面插入
print(myList2)
print(myList2[0:4],'myList2[0:4].type=',type(myList2[0:4]))
myList2[0:4]=['d','c','b','aaaaa','多余']#通过列表赋值 如果元素长度超过范围也会按顺序插入
print('myList2',myList2)
print('myList2[0:4].type=',type(myList2[0:4]))
del myList,myList2

###### 4.元组tuple:不可变 用()创建
myTuple1=()#空元组
print('myTuple1.type=',type(myTuple1))
myTuple1=('元1',)#一个元素时 需要后接',' 否则变成了字符串
print('myTuple1.type=',type(myTuple1))
myTuple1=('1',2,'c',"Four")
#元组的操作与字符串类似，可以被索引，可以把字符串看成特殊的元组
#虽然元组不可变，但可以包含可变元素，如list
myTuple1=(1,'2',['3'])
#myTuple1[0]=0 元组不可变
del myTuple1

###### 5.Set集合:可变 用set()/{}都可创建
mySet1=set() #空集合需要使用set()创建 因为{}是用来创建空字典的
print('mySet1.type=',type(mySet1))
mySet1=set("111234aaabc")
print(mySet1)#无序的 自动去重
print('mySet1.type=',type(mySet1))
mySet2=set('abccccd')
#set集合的- | & ^操作
mySet3=mySet1-mySet2
print('1-2后set3=',mySet3)
mySet3=mySet1|mySet2;
print('1|2后set3=',mySet3)
mySet3=mySet1&mySet2
print('1&2后set3=',mySet3)
mySet3=mySet1^mySet2
print('1^2后set3=',mySet3)
del mySet1,mySet2,mySet3

###### 6.字典:可变 用{}创建
myDict={}#空字典
myDict['1']='one'
print('myDict.type=',type(myDict))
print('myDict=',myDict)
myDict={"one":1,"key2":"Two"}
#通过dict函数创建字典
myDict=dict(r=1, Google="googole", Taobao=3)#key只能是字符串 且不能用""
print('myDict=',myDict)
myDict=dict([("Run",1),("Two",2)]) #列表作为字典的唯一一个元素 列表内用()包裹键值对
print('myDict=',myDict)

#数据类型转换
myChar=chr(97) #将10进制的整数转换为对应的字符 0:48 A:65 a:97
print(myChar)