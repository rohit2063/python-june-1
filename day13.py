class Test():
    a = 10
    b = 11

obj = Test()
print(obj)
print(obj.b)
obj.a = 60
obj.c = 90
print(obj.a)
print(obj.c)

obj1 = Test()
print(obj1.a)
# print(obj1.c)

print(obj1 == obj)
