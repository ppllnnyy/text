print("输入你的名字")
# 将input赋值给左边的变量
name = input()
print(name)
print("你是：%s" % name)
name = input("告诉我你是谁")
print("你的名字是： %s" % name)
# 无论input写入什么都会转换成字符串 需要数字需要进行转换
num = input("输入你的数字")
num = int(num)
print(type(num))