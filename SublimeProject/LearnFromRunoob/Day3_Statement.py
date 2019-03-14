#while statement
import random
var=0
while var!=1:
 #num=int(input("输入一个数字:")) sublime无法正常运行输入程序
 var=random.randrange(0,10)
 print('你输入的数字是:',var)
print("good bye")

#for statement
mylist=["C", "C++", "Perl", "Python"]
for x in mylist:
 print('x=',x,end=' ')
print()
for i in range(1,8,1):#内涵函数range(start,end,len) 可以直接range(end) 默认从0开始 len=1
 print('i=',i,end=' ')
print(range(5)[4])
for x in range(10):
 print('x=%d'%(x))
var=10
while var>0:
 var=var-1
 if(var==5):
  continue
 print('var=',var)
#查找质数
for n in range(2,10):
 for x in range(2,n):
  if n%x==0:
   print(n, '等于', x, '*', n//x)
   break;
 else:
  print(n,'是质数')

#if statement
var=0
if var:
 print('var!=0')
else:
 print('var==0')
#age=int(input('请输入你的年龄'))
#print('输入age=',age)

#while statement
n=100
sum,counter=0,1
while counter<=n:
 sum=sum+counter
 counter+=1
print('1到%d之和为:%d'%(n,sum))

print('-------------------------')

#test while else
count=2
while count<5:
 print('count=',count)
 if(count==3):
  print('跳出while')
  break;
 count+=1
else:
 print('while else count>=5')
#test for else
site=[1,2,3,4,'runoob',5]
for x in site:
 if x=='runoob':
  print('得到',x)
  break;
 print('item=',x)
else:#执行到最后的时候 执行该else 如果提前跳出循环 不会执行else
 print('else=',x)

 #pass语句块
for x in  'runoob':
 if x=='o':
   pass
   print('执行pass快')
 print('当前字母:',x)
print('good bye')

#迭代器iter() 字符串、列表、元组都可以创建迭代器
mylist=[1,2,3,4]
myiter=iter(mylist)#创建迭代器 参数可以是字符串、列表、元组
print(next(myiter))#获取迭代器的下一个元素
print(next(myiter))
for x in myiter:
 print('for.x=',x,end= "|")

print('\n--------------------------------')
#函数function 关键字def
def arena(width,height):
 return width*height
print('arena=',arena(4,5))
#不可变类型做参数
def ChangeInt(a):
 a=666
a=1
ChangeInt(a)
print('a=',a)
#传可变对象做参数
def changelist(list2):
 list2.append([4,3,2,1])
 print('函数内取值',list2)
 return
list2=['1234']
changelist(list2=[1,4])
print("函数外取值",list2 )

#关键字参数
def printme(guanjianzi):
 print(guanjianzi)
 return
printme(guanjianzi='666fasd')#关键字参数 函数调用使用关键字参数来确定传入的参数值。
def printInfo(name,age):
 print('name=',name)
 print('age=',age)
printInfo(age=4,name='韩')

#默认参数
def printInfo(name,age=35):
 print('name=',name)
 print('age=',age)
 return
printInfo(name='我的名',age=6)
#不定长参数 ①*该参数变量类型为元组 ②使用**表示导入为字典
def printinfo(arg1,**vartuple):
 print('输出:',end=' ')
 print(arg1)
 print(vartuple,'type=',type(vartuple))
#printinfo(70,60,50)
printinfo(2,a=3,b=4)
#函数参数--*单独出现 *后的参数必须都使用关键字传入
def add(a,b,*,c,d):
 return a+b+c+d
print('add=',add(1,2,c=3,d=4))
#匿名函数 用lambda创建匿名函数
sum=lambda arg1,arg2:arg1+arg2
print('sum=',sum(4,5))
#变量作用域 局部变量->闭包函数外的函数中->全局作用域->内置作用域
myint=0#全局变量
def test():
  myint=111#myint在这里是局部变量
  print('内部',myint)
test()
print('外部',myint)
#使用global和nonlocal关键字 分别修饰局部修改全局  闭包内修改闭包外的变量
myint=0#全局变量
def test():
  global myint#myint在这里是全局变量 不能同时赋值 会报错 无效语法
  myint=111
  print('内部',myint)
test()
print('外部',myint)

def outer():
  myint=5#myint在这里是局部变量
  def inner():
   nonlocal myint
   myint=555
   print('222内部',myint)
  inner()
  print('222外部',myint)
outer()

a=10
def test(b):
 b=b+1
 print(b)
test(a)
print(a)


#数据结构--列表
#通过pop()把列表当作栈使用
mylist=[1,2,3,4]
mylist2=['6','5']
mylist.extend(mylist2)
print(mylist)
print('pop(0)',mylist.pop(0))#移除并返回指定元素
print('栈首元素即最后一个元素出栈,',mylist.pop())
print(mylist)
print(mylist[0])
#print(mylist.index('61'))#获取指定元素的下标 若不存在该元素 则报错:not in list
#通过导入collections的deque模块创建列表 把列表当作队列使用
from collections import deque
mylist=deque([1,2,3,4,'5'])
print(mylist)
mylist.popleft()#popleft()去除队首
print(mylist)

#列表推导式
mylist=[2,4,6]
mylist=[3*x for x in mylist]#mylist的每个元素*3 赋值给mylist
print('mylist=',mylist)
mylist=[[x,x**2] for x in mylist]
print('mylist=',mylist)
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit= [weapon.strip() for weapon in freshfruit]
print(freshfruit)
#if语句作为列表推导式的过滤器
mylist=[2,4,6]
mylist=[3*x for x in mylist if x<3]
print('mylist过滤后=',mylist)
#同时使用两个列表作为推导式的操作对象
mylist=[2,4,6]
mylist2=[-1,2,3]
mylist3=[x*y for x in mylist for y in mylist2]
print(mylist3)
#嵌套列表解析 即矩阵
matrix= [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
print([[i,j] for i in range(4)for j in range(5,9)])
print([row[0] for row in matrix])
print([[row[i] for row in matrix] for i in range(4)])#转置矩阵

#set集合也支持推导式
a={x for x in 'abcder' if x not in 'abc'}
print('a=',a)
#字典
tel={'guido': 4127, 'irv': 4127, 'jack': 4098}
print(tel.keys())
print(tel.values())
print(tel.items())#返回类型字符串  内容是键值对元组列表[(,),(,)]
#同时遍历两个序列 可通过使用zip()组合
mylist=[1,2,3,4]
mylist2=['a','b','c','d']
for a,b in zip(mylist,mylist2):
 print('a={0},b={1}'.format(b,a))#字符串的format和C#类似
print('my name is {0},age={1}'.format("韩",66))
#反向遍历一个序列通过 reversed()函数 sort()正向排序
for i in reversed(range(1,10,2)):
 print('i=',i,end=' ')
print()
