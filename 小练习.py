name = "11公司"

stock_price = "114514"

stock_code = 114

stock_price_daily_growth_factor = 1.2

growth_days = 7

print(f"公司：{name},股票代码：{stock_price},当前股价：{stock_code},")

zmxs =  "每日增长系数是：%.1f 经过%d天的增长后，股价达到了:%.2f" % (stock_price_daily_growth_factor , growth_days , stock_price_daily_growth_factor * growth_days)
print(zmxs)