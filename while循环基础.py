i = 0
while i < 100:
    print("你好")
    # 增加条件变量 大于后循环停止
    i += 1
# 小练习 通过while循环 计算从1累计到100的和
i = 1
sum = 0
while i <= 100:
    # sum记录i累加的和
    sum += i
    i += 1


print("1到100累加和为%d" % sum)
