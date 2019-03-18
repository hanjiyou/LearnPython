# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-18 19:47:42
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-18 19:54:24

#正则表达式
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
