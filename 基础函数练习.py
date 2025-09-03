""" name = "itititit"
length = len(name)
print(length)

"""

str1 ="itititit"
str2 = "icicicicic"
str3 = "ibibibibib"

""" count = 0
count2 = 0
count3 = 0
for i in str1:
    count += 1
print("字符串长度是：",count)
for i in str2:
    count2 += 1
print("字符串长度是：",count2)
for i in str3:
    count3 += 1
print("字符串长度是：",count3)
"""
# 使用函数优化过程

# 已组织好的，可重复使用，针对特定功能
def my_les(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为:{count}")

my_les(str1)

