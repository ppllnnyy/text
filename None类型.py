"""

None是类型‘NoneType的字面量，用于表示：空的，无意义的’

def say_hello():
    print("hello")
# 使用变量接受say_hello函数的返回值

result = say_hello()

print(result)
# 打印返回值
print(type(result))
# None可以主动使用return返回，效果等同不写return语句
def say_hello():
    print("hello")
    return None
# 使用变量接收say_hello函数的返回值
result = say_hello()
# 打印返回值
print(result)
"""
# 在if判断中，None等同于False

def check_age(age):
    if age >18:
        return "SUCCESS"
    else:
        return None

result = check_age(16)
if not result:
    # 进入if表示result是None值 也就是False
    print("未成年，不可以进入")


