# 当外层if满足条件时，才会执行内层if判断
if int(input("你的身高是多少")) > 120:
    print("身高超出限制，不可以免费")
    print("但是vip级别大于3可以免费")
    if int(input("输入您的vip级别")) > 3:
        print("可以游玩")
    else:
        print("需要补票，10元")
# 不满足直接执行外层else
else:
    print("欢迎，可以免费游玩")

age = int(input("输入你的年龄"))
year = int(input("输入你的工龄"))
level = int(input("输入你的等级"))
if age >= 18:
    print()
    if age < 30:
        print("年龄达标")
        if year > 2:
            print("恭喜你，年龄和工龄达标")
        elif level > 3:
            print("年龄与等级达标")
        else:
            print("对不起，仅年龄达标")
    else:
        print("年龄过大")
else:
    print("年龄过小")