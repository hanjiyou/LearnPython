#import requests
#Number类型的常用函数
myInt1=abs(-10)
print('abs(-10)=',myInt1)
import math
print('ceil(5.1)返回上入整数=',math.ceil(5.1))#返回参数的上入整数
x,y=2,3
print((x>y)-(x<y)) #相当于py2种的cmp函数 x>y返回1 x<y返回-1 x=y返回0
print("fabs-1.1",math.fabs(-1.1))#float类型的绝对值
print('floor -1.1',math.floor(-1.1))#返回参数的下入整数
print('max=',max(1,2,3,4,99,-99.9))#去最大值 参数可为序列或字符串
print('max=',max('abcZ'))
print('modf 1.3333',math.modf(1.3))#返回一个两元素的元组 第一个元素是小数部分 第二个是整数部分
print('mode.result of typf=',type(math.modf(1.3)))
print('pow x**y',pow(x,y))#返回x的y次方
print('round x=',round(1.666))#返回参数的四舍五入值
import random
print('randrange',random.randrange(2,4,2))#randrange.([start,] stop [,step]) start默认0 step默认为1
print('random',random.random())#返回一个[0,1)之间的随机值
myList1=[1,2,3,4,5,6,7,8,9,10]
myList1=(1,2,)
#myList1={1:"haha",2:111,3:222}
print('choice',random.choice(myList1))#返回一个序列的随机值 字典和set不是序列 不能用在此处
print('pi=',math.pi)

#字符串类型常用函数
#in/not in
myStr1='hello'
myStr2='world'
if 'h' in myStr1:
	print('h在myStr1种')
else:
	print('h不在')
myStr3="""
只是
在
"""
print('myStr3=',myStr3)
#内建函数
print(myStr1.capitalize())#返回当前字符串首字母大写的字符串
print(myStr1.count('he',0))#查看当前字符串指定位置(默认为s=0 e=最后)出现的指定字符串的覅书
myStr1="WWW.p1234pab"
print(myStr1.center(20,'-'))
print(myStr1.endswith('www',0,3))#当前字符串是否以指定字符为结尾左包右开 end可直接写真实位置 而不是下标 startswith
print(myStr1.find('p',6,10))#返回字符第一次出现在当前字符串的下标不存在返回-1 index相同  但是不存在则报错 还有个rfind()是从右边开始查找 返回字符串最后一次出现的位置
print('mystr1.len',len(myStr1))
myList1=['12','cd','56']
print('myStr1.join(list)',myStr1.join(myList1))#将序列用当前字符串拼接起来
print('lower',myStr1.upper())#upper返回大写 lower返回小写
myStr2='1234'
print('myStr1.isdecimal=',myStr2.isdecimal())#判断当前字符串是否只包含10进制
myStr2='  1234 '
print(myStr2)
print('mystr2.lstrip()=',myStr2.lstrip())

intab = "aeiou"
outtab = "12345"
myStr4=''
trantab = myStr4.maketrans(intab, outtab)   # 制作翻译表

myStr2 = "1this is string example....wow!!!"
print (myStr2.translate(trantab))#开始转换


#列表
mylist=[1,2,3,4]
print('mylist=',mylist)
del mylist[0]
print('del删除0后mylist=',mylist)
mylist[0:2]=[]
print('0:2替换空列表后mylist=',mylist)
print("mylist.len=",len(mylist))
#列表嵌套
a,b=['dddd','z'],['a','b','c']
c=[a,b]
print('嵌套两个列表a b后',c)
print('c00=',c[1][0])#嵌套列表 相当于二维数组
print('列表len=',len(c))#如果是嵌套数组 则只看第一维的长度
print('列表最大值=',max(c))#如果是嵌套数组不能同时包括数字和字符串
a.append({"name":"haha"})#将参数拼接到列表尾部
print('append',a)
mylist=[1,2,3,4]
mylist.sort(reverse=True)#sort给列表排序 可以指定倒序 即reverse=True
print('list.sort',mylist)
mylist.clear();#情况列表种的元素
print(mylist)

#元组
#内置函数:len/max/min/tuple
print(tuple([1,2,3]))
myTup=(1,2,3,[4,5])
#myTup.append([1,2,3]) 不能直接调用append
print("myTup.append",myTup)

#字典
myDict={'key1':1,'key2':[1,2,3]}
myStr=type(str(myDict))
print(myStr)
print(str(myDict))
myDict1=myDict.copy()#浅拷贝:一级目录深拷贝(修改隔离) 二级目录子对象不拷贝，还是引用同一块内存
myDict1['key1']=2
myDict1['key2'].remove(1)
print('修改后myD=',myDict)
print('修改后myD1=',myDict1)
myDict={'key1':1,'key2':[1,2,3]}
myDict1=myDict#浅拷贝 引用对象
myDict1['key1']=2
print(myDict)
print(myDict1)
#深拷贝 需要引入copy模块
import copy;
myDict2=copy.deepcopy(myDict)
myDict2['key1']=1
print(myDict)
print(myDict2)

#set集合
#add和update都可以添加元素 update可添加多个元素 用','隔开
myset1=set(('111','222','333'))
myset1.update(['444','555'])
print(myset1)
myset1.remove('111')#移除元素 不存在会报错
myset1.discard('111')#移除元素 不存在不会报错
#myset1.clear()
myset1.pop()#随机删除一个元素
print(myset1)
myset1=set(('1',6))
myset2=set(('2',7))
myset1=myset1.union(myset2)
print(myset1)#返回两个集合的并集
