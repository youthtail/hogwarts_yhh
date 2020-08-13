import time
# 打印时间戳
print(time.time())
# 时间的元组tuple
print(time.localtime())
print(time.strftime('%Y年%m月%d %H:%M:%S', time.localtime()))
# 3天后的时间
new_time = time.time()
three_day_after = new_time + 3*24*60*60
three_day_after_tuple = time.localtime(three_day_after)
print(time.strftime('%Y年%m月%d %H:%M:%S', three_day_after_tuple))

