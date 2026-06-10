#Type casting or conversion
a = "123"
print(type(a))

b = int(a)
print(type(b))

data = "Hello"
print(type(data))
# print(int(data))

a = 500
print(type(a))

b = str(a)
print(type(b))

#Type validation
a = 100.0
print(isinstance(a,int))

b = "hello"
print(isinstance(b,str))

#Operator
# + - \  * ** // %
a = 1001
b = 100
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# % //
print(a%b)
print(a//b)

# **
print(a**2)

# String
a = "Hello "
b = "World"
print(a+" "+b)
print(10*a)

# Comparison Operator
print(5==4)
print("hello"=="hello")
print(5!="5")

#Logical Operator

print(5==2 and 1!=4)
print(True and True)

print(not(5==2 or 1==1))

