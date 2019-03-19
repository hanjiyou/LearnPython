# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-18 19:47:42
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-19 19:46:02
print('-------------------------字符串编码的简单介绍模块')
str1='哦哦哦'
str2=u'哦6哈哈'#字符串的存储方式都是以Unicode字符来存储的，所以前缀带不带u，其实都一样。
print(str2==str1)
print(str2 is str1)#都是True
mystru8=str1.encode('utf-8')#将指定字符串转成二进制bytes类型 utf-8用三个十六进制来表示一个中文字符
print('转成utf8后的16进制为:',mystru8)
mystrgbk=str2.encode('gbk')#gbk用二个十六进制来表示一个中文字符。
print('转成gbk后的16进制为:',mystrgbk)
mystrgbk=mystrgbk.decode('gbk')#将指定二进制解码成源字符串
print('解码后gbk:',mystrgbk)
str3=b'!@#'#bytes字符串组成形式，必须是16进制数胡总和ascii字符
#正则表达式
print('-------------------------re正则模块')
import re
mylist=re.findall(r'\bw[a-z]*','f which foot or hand fell fa f f')
print('正则re.findall mylst=',mylist)
mystr=re.sub(r'(b[a-z]+)\1',r'\1','cat in the the hat')
print('正则sub mystr=',mystr)
mylsit=[x for x in range(2,9,3)]#range(s,e,l)表示从s到e步长为l,做for循环的目标 通过for获取其中的每个元素
print(range(2,9)[1:])#类型是range 可以通过索引和截取获取值
print('111',mylsit)

#访问互联网
from urllib.request import urlopen
#for line in urlopen('http://www.baidu.com'):#打开指定的url 返回html源码 需要加上http前缀
#	line=line.decode('utf-8')#decoding the binary data to text
	#print(line)
import smtplib
#server=smtplib.SMTP('localhost')#报错 当前主机拒绝
#server.sendmail('1156781974@qq.com','1156781974@qq.com',"afsdlkfja")
#server.quit()
print('-------------------------datetime时间模块')
from datetime import date
now=date.today()#获取当前时间 y-m-d 返回类型datetime.date
print('now=',now,'type=',type(now))
birthday=date(2018,3,18)
age=now-birthday
print('天数=',age.days)

print('-------------------------zlib压缩模块')
import zlib
s = b'witch which has which witches wrist watch'
print('bytes字符串,原长度:',len(s))
s2=zlib.compress(s)
print('压缩后长度:',len(s2),'压缩后=',s2,)
#print(s)
s2=zlib.decompress(s2)
print(s2)
print('-------------------------性能度量模块')
from timeit import Timer
print(Timer('t=a;a=b;b=t','a=1;b=2').timeit())#查看执行指定程序所需时间
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

