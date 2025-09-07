# 变量作用域指的是变量的作用范围（变量在哪里可用，在哪里不可用） 主要分为两类 局部变量和全局变量
# 局部变量是定义在函数体内部变量
def testA():
    num = 100
    print(num)

testA()
# 变量a是定义在testA函数内部的变量，在函数外部访问则报错
"""print(num)"""

# 全局变量指的是在函数体内外都能生效的变量
num = 100
def testB():
    print(num)
# 使用global关键字可以在函数内部声明为全部变量
def testC():
    global num
    num = 1000
    print(num)

print(num)

