# 通过外层控制行数
for i in range(1,10):
    # 通过内层循环控制每一行的数据
    for j in range(1,i+1):
        # 在内层循环中输出每一行内容
        print(f"{i} * {j} = {i * j}\t", end='')
    # 外层循环可以通过print输出一个回车符
    print()