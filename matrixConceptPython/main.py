

#parse json convert json to python
import json
x = '{"name":"salsal","age":30,"gender":"femal"}'
t = type(x)
y = json.loads(x)
print(y)
print(type(y))
