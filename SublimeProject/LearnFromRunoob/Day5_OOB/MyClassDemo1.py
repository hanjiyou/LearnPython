# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-15 10:18:37
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-15 17:24:15
class MyClassDemo1:#一个简单的类
 i=1234
 def f(self):
  print(self.__class__)
  return self

x=MyClassDemo1()
print('Myclass的属性i=',x.i)
print('调用myclass的方法:',x.f())

class Complex:
 def __init__(self,var1,var2):#构造函数__init__ self相当于this 不需要传入实参
  print('hhh 调用complex类的构造')
  self.var1=var1
  self.var2=var2
complex=Complex(6,7)
print(complex.var1,complex.var2)
print('----------------------------')
class People:
 name=''#定义基本属性
 age=0
 __weight=0#定义私有属性
 def __init__(self,n,a,w):
  print("hhh people的构造函数")
  self.name=n
  self.age=a
  __weight=w
 def speak(self):
  print("{0}说，我{1}岁".format(self.name,self.age))
  print("%s说:我%d岁。"%(self.name,self.age))
#peo=People("han",16,123)
#peo.speak()
#print("weight",peo.__weight)#报错 实例反问私有变量
#继承
class Student(People):#单继承
 grade=''
 def __init__(self,n,a,w,g):#构造函数
  People.__init__(self,n,a,w)
  print("hhh Student的构造函数")
  self.grade=g
 def speak(self):#覆盖父类中的speak()方法
  print('%s说:我%d岁了，我在读%d年级'%(self.name,self.age,self.grade))
#s=Student('ken',10,60,3)
#s.speak()
class speaker():
 topic=''
 name=''
 def __init__(self,n,t):
  print("hhh speaker的构造函数")
  self.name=n
  self.topic=t
 def speak(self):
  print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
class sample(speaker,Student):#多重继承
 a=''
 def __init__(self,n,a,w,g,t):
  Student.__init__(self,n,a,w,g)
  speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法

print('--------------------------方法重写')
class parent:
 def __init__(self):#
  print('p con')
 def myMethod(self):
  print('调用父类方法')
class Child(parent):#定义子类
 def __init__(self):
  parent.__init__(self)
  print('s con')
 def myMethod(self,str):
  print('调用子类方法',str)
c=Child()
c.myMethod('666')
#super(Child,c).myMethod()#super关键字用于调用父类(超类)的一个方法。
#c=parent.__init__(Child())
p=parent()
p.myMethod()

print('--------------------------私有')
class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):          # 私有方法
        print('这是私有方法')

    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出 私有方法可以间接调用
#x.__foo()      # 报错
print('--------------------------运算符重载')
class Vector:
 def __init__(self,a,b):
  self.a=a
  self.b=b
 def __str__(self):
  print('调用str')
  return '111vector(%d,%d)'%(self.a,self.b)
 def __add__(self,other):
  print('调用add')
  return Vector(self.a+other.a,self.b+other.b)
v1=Vector(2,10)
v2=Vector(5,-2)
print(v1+v2)

class myvector:
 def __init__(self,a,b):
   self.a=a
   self.b=b
 def __str__(self):
  print('调用str')
  return 'vector(%d,%d)'%(self.a,self.b)
 def __add__(self,other):
  print('调用add')
  if other.__class__ is myvector:
   return myvector(other.a+self.a,other.a+self.b)
v3=myvector(1,2)
v4=myvector(2,3)
print(v3+v4)
#mystr='aaa'+'bbb'+'7'
#print(mystr)
