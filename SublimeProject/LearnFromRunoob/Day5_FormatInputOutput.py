print(str(1/4))
print(type(str(1/4)))#返回一个用户易读的表达式
print(repr(1/4))#返回解释器易懂的表达形式
print(type(repr(1/4)))
x=4
print(repr(x).rjust(4),end=' ')#rjust是在当前字符串串靠右, 并在左边填充空格。
print(repr(x*x*10).rjust(1))
print('12'.zfill(2))#在数字左边填充0 参数为字符串总长度 如果参数<=字符串长度 则不填充
print("{}网站,age={}".format('www.baidu',4))
import math
print('PI保留3位数{0:.3},保留4位小数{1:.4f}'.format(math.pi,1.56789))
myDic={'goold':1,'Runoob':2,'Taobao':3}
for name,number in myDic.items():
 print('{0:12}==>{1:10}'.format(name,number))
print('---------------------字典格式化输出')
#字典输出格式化
myDic={'googld':666,'baidu':'垃圾','key3':'three'}
print('googld:{0[googld]:d},baidu:{0[key3]:s}'.format(myDic))#方法1 :d用于修饰int类型 :f用于修饰浮点数 :s用于修饰str
print('{1:f}哈哈'.format(2,1.1,2))

print('---------------------旧式字符串格式化%')
print('pi的旧式格式化:%12.9f'%math.pi)
print('---------------------input控制台输入')
#str=input('请输入：')
#print('你输入的是',str)




print('---------------------读写文件')
#file1=open('first.txt','a')#追加一个文件 如果不存在 则创建
#file1.write('我随便写点东西222')
#file1.close()#关闭打开的文件
file=open('fist.txt','r+')#读文件 如果文件不存在 则直接中断程序 且不报错 r+为可读可写
print('文件指针位置默认是',file.tell())#文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
#str=file.read()#read()不指定参数 则默认读取全部
str=file.readline()#readline()读取一行 且文件指针会移向下一行
print('读取到第一行',str)
print('读取一行指针是:',file.tell())

print('写入字符数:',file.write('写入0'))#写入都是从文件尾部接着写入 除非seek()  跟指针位置无关
print('写入0后文件指针是:',file.tell())

#str=file.readline()#
#print('读取到第2行',str)

#str=file.readlines()#readlines()从当前文件指针一下继续读取所有行
#print('读取全部',str)
#for line in file:#通过for循环迭代读取每一行 返回的item就是每一行的字符串 方法很简单, 但是并没有提供一个很好的控制。 因为两者的处理机制不同, 最好不要混用。
    #print('迭代读取:',line,end=' ')
file.write('写入1')
file.seek(1,0)#(pos,start0/cur1/end2) pos<0会报错
file.write('写入2')

print('使用seek移动文件指针后为,',file.tell())
file.close()
print("end")

#写一个文件
#myfile=open('write.txt','w')#写入一个文件 如果不存在则创建 存在则内容会删除重新写入
#number=myfile.write('第一行\n第二行\n第三个')
#print('总写入字符数:',number)
#myfile.close()
myDic={'key1111':111,2:"value2"}
import pickle
#output=open('data1.pk1','wb')
#pickle.dump(myDic,output)
output=open('data1.pk1','rb')#如果是以二进制写入的话 必须以二进制读取
myDic2=pickle.load(output)
print(myDic2)
output.close()