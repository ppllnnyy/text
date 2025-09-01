print("欢迎来到游乐场，儿童免费，成人收费")
age = int(input("请输入年龄"))
if age >= 18:
    print("您已成年，需要补票10元")
# 当不满足if条件时，else执行
else:
    # 同样需要缩进
    print("您未成年，可免费游玩")

print("祝您游玩愉快")