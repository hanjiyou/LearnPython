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