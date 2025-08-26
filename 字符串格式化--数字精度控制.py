avg_salary = 12333
avg = 114.56
message = "12333限制宽度8 %8d" % avg_salary
print(message)
message = "114.56限制宽度8 精度限制1 %8.1f" % avg
# .n会对小数部分做精度限制的同时对小数四舍五入
print(message)