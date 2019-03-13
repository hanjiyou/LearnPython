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

#数据结构--列表 
#通过pop()把列表当作堆栈使用
mylist=[1,2,3,4]
mylist2=['6','5']
mylist.extend(mylist2)
print(mylist)
mylist.pop(0)#移除并返回指定元素的下标
print('栈首元素即最后一个元素出栈,',mylist.pop())
print(mylist)
print(mylist[0])
#print(mylist.index('61'))#获取指定元素的下标 若不存在该元素 则报错:not in list
#通过导入collections 的deque模块创建列表 把列表当作队列使用
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