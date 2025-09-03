# 设一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
import random
num = random.randint(1, 100)
# 定义一个变量记录猜测多少次
count = 0
# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True

while flag:
    guess_num = int(input("请输入你猜测的数字"))
    count += 1
    if guess_num == num:
        print("猜中了")
        print("猜中次数为:%d" % count)
        flag = False
    elif guess_num < num:
        print("数字小了")

    elif guess_num > num:
        print("数字大了")

