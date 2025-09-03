# continue关键字用于：中断本次循环，直接进入下一次循环
# continue可以用于for循环和while循环，效果一致
# break是直接结束循环
"""for i in range(1,6):
    print(f"语句{i}")
    continue

    print(f"语句{i}")
"""
"""
for i in range(1,6):
    print(f"语句1")
    for j in range(1,6):
        print(f"语句2")
        # continue只在所在范围内生效
        continue
        print(f"语句3")

    print(f"语句4")
"""
#

for i in range(1,6):
    print("语句1")

    for j in range(1,6):
        print("语句2")
        # break 跳出此循环
        break
        print("语句3")

    print("语句4")

