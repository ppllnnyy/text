"""print("欢迎来到动物园")
height = int(input("输入你的身高cm"))
vip_level = int(input("输入您的vip等级"))
day = int(input("请输入日期"))
# 多条件下条件之间互斥
if height < 120:
    print("您的身高小于120cm，可以免费游玩")
elif vip_level > 3:
    print("您的vip等级大于3，可以免费游玩")
elif day == 1:
    print("今天1号免费日")
else:
    print("所有条件不满足，需要购票10元")

print("祝您游玩愉快")
"""
# 可将代码填进条件判断
print("欢迎来到动物园")
# 多条件下条件之间互斥
if int(input("输入你的身高cm")) < 120:
    print("您的身高小于120cm，可以免费游玩")
elif int(input("输入您的vip等级")) > 3:
    print("您的vip等级大于3，可以免费游玩")
elif int(input("请输入日期")) == 1:
    print("今天1号免费日")
else:
    print("所有条件不满足，需要购票10元")

print("祝您游玩愉快")