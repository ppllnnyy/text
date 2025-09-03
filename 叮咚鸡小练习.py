print("欢迎查核酸，请配合检查体温")

def tiwen(data):
    if data >37.3:
        print("赶紧隔离")
    elif data <= 37.3:
        print("体温正常，请进")

tw = int(input("请输入你的体温"))

tiwen(tw)