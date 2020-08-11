
# json 使用字典和列表组成的 {'order':[{'lily':'three books'},{'Tom':'one piano'}], 'amt':'200'}
import json

data = {'order':[{'lily':'three books'},{'Tom':'one piano'}], 'amt':'200'}
data1 = json.dumps(data)
print(type(data))
print(data)
print(type(data1))
print(data1)
data2 = json.loads(data1)
print(type(data2))
print(data2)

