#Function
def add():
    a = 20
    b = 22
    print(a+b)

add()

def number_add(a,b):
    print(a+b)

number_add(190,300)

#Tuple
a = (1,2,3,4,5)
print(type(a))
# print(a[90]) index error

# a[0] = 100 unable to assign the data

print(len(a))

a = ()
print(a)

a = (1,2,3,4,5)
b = list(a)
b.append(6)
b[0]=10

print(b)
a = tuple(b)
print(a)

#set
a = {"HEllo","Testing","Team","google",1,1,2,2}
print(a)
print(type(a))
a = set()
print(type(a))

a = [1,2,3,4,5]
b = set(a)
a = list(b)

