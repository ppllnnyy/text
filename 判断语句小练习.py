import random
num = random.randint(1 , 10)
sz = int(input("输入数字"))
if sz == num:
    print("恭喜你答对了")
else:
    if sz > num:
        print("大了")
    else:
        print("小了")

    sz = int(input("输入数字"))

    if sz == num:
        print("恭喜你第二次答对了")
    else:
        if sz > num:
            print("大了")
        else:
            print("小了")
    sz = int(input("输入数字"))
    if sz == num:
        print("恭喜你第三次答对了")
    else:
        print("次数结束，正确答案是%d" % num)

# print("答错了，正确答案是%d" % num)