a = [1,2,3,4,5]
print(type(a))
print(a)

a = []
print(a)

data = ["Hello","world","boardway"]
print(data)
print(len(data))

print(data[0])
print(data[-1])
# print(data[3]) Out of range

data = [1,2,3,"Hello","Test",10.0,None,True]
print(data)

#Slicing
print(data[1:5])
print(data[:5])
print(data[2:])
print(data[:])
print(data[-3:-1])

# Method of adding items in lists
'''
append
insert
extend
concat(+)
'''

#Append
data = [1,2,3,4,5]
data.append(6)
print(data)

data = []
data.append(1)
data.append(2)
print(data)

#Insert
data = [1,2,3,4,5]
data.insert(1,"Insert")
print(data)

data.insert(100,500)
print(data)

# Extend
a = [1,2,3,4]
b = [5,6,7,8,9]
a.extend(b)
print(a)
print("--------------------"*4)
#Concate(+)
a = [1,2,3,4]
b = [5,6,7,8,9]
c=a+b
print(c)
# print(a,b)

'''
del 
remove
pop
clear
'''
# Del
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del data[0]
print(data)

# Remove
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data.remove(4)
print(data)

# Pop
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_data = data.pop()
data.pop(5)
print(data)
print(last_data)

# Clear
data = [1,2,3,4,5,"Hello"]
data.clear()
print(data)