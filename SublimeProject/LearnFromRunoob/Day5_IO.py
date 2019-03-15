print(str(1/4))
print(type(str(1/4)))#返回一个用户易读的表达式
print(repr(1/4))#返回要给解释器移动的表达形式
print(type(repr(1/4)))
x=4
print(repr(x).rjust(4),end=' ')#rjust是在当前字符串串靠右, 并在左边填充空格。
print(repr(x*x*10).rjust(1))
 