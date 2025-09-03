import random

ygbh = 1
yuer = 10000

for ygbh in range(1,21):

    jixiaofen = random.randint(1,10)

    if jixiaofen < 5:
        print(f"员工{ygbh},绩效分{jixiaofen},低于5，不发工资，下一位")
        continue
    if yuer >= 1000:
        yuer -= 1000
        print(f"员工{ygbh},绩效分{jixiaofen}，发放工资1000元，公司账户余额{yuer}，下一位")
    else:
        print(f"余额不足，当前余额：{yuer}元")
        # break结束发放
        break
