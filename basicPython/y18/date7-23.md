1.1 grep -e 
显示文件中符合条件的字符 
查找当前目录下所有文件中包含字符串”Linux”的文件，会将含有Linux字符串的所有文件匹
配出来。
  2.grep -w用于字符串精确匹配 
若文件中的内容包括如下： 
262 a3 
262 
26 
如果 grep ‘26’ file，结果是三行全部都被显示 
若要精确匹配26所在行 
使用grep -w ‘26’ file
2. 不小心关闭桌面，可以执行命令：sudo service lightdm restart。2. 不小心关闭桌面
，可以执行命令：sudo service lightdm restart。
3.GPU属于显卡。是图形处理器，GPU加速运算可显著提升应用程序运行速度。
  回去配置ubuntu tensorflow gpu。磁盘分区，linux系统扩容。
4.print( y, end=" ")不换行输出。
5.isinstance 和 type 的区别在于：  
```
class A:  
    pass
class B(A):
    pass
isinstance(A(), A)  # returns True
type(A()) == A      # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
区别就是:
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
```
6.```
  a, b = 0, 1
while b < 10:
    a, b = b, a+b#理解了a, b是引用这里就好理解了。
    print(b, end=' ')
print()
7.# lambda 函数拥有自己的命名空间,
# 且不能访问自己参数列表之外或全局命名空间里的参数。
sum = lambda arg1, arg2: arg1 + arg2
print(sum(10, 20))
8.
 1.Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作
用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作
用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
>>> if True:
...  msg = 'I am from Runoob'
... 
>>> msg
'I am from Runoob'
 2.
  a = 10
def test():
    global a
    a += 1
test()
print(a)
 3.
  >>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
 4.__name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块
中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
运行输出如下：

$ python using_name.py
程序自身在运行
$ python
>>> import using_name
我来自另一模块
>>>
 5.运算符重载
Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：

实例(Python 3.0+)
#!/usr/bin/python3
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
以上代码执行结果如下所示:

Vector(7,8)
 6.https://blog.csdn.net/zhangleaimeiling/article/details/78486191Tensorflow入门
及项目。
 7.Linux下怎么将自己编写的Python模块添加到PYTHONPATH上https://blog.csdn.net/zjwc
dd/article/details/51454762,可以在anaconda中切换python环境。
 8.bc计算器：https://blog.csdn.net/huangjin0507/article/details/45045957
 9.Tensorflow入门之softmax函数。
 10.Greenplum, postgres。
 ```

