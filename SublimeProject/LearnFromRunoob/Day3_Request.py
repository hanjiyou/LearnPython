# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-11 10:27:22
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-11 10:41:27
import requests

url = 'http://www.baidu.com'
data = requests.get(url)
print(data)
data.encoding='utf-8' #查看r.text的时候 需要先设置编码为utf-8 否则报错
print(data.text)  #这里.text等同于read()
code = data.encoding
print(code)
page_status = data.status_code
print(page_status)