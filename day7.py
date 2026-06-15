import random

for i in [1,2,3,4,5]:
    print(i)

for j in "Hello":
    print(j)

a = {
    "program":"C",
    "Type":"Compiler"
}
for i in a:
    print(i)

for i in a.values():
    print(i)

for i in a.items():
    print(i)

for i in a:
    print(a[i])

for i,j in a.items():
    print(i,j)
print("------------"*4)

for i in[1,2,3,4,5,6,7]:
    if i==4:
        break
    print(i)
print("---------"*4)

for i in[1,2,3,4,5,6,7]:
    if i==4:
        continue
    print(i)

print("------------"*4)

for i in [1,2,3,4,5]:
    if i%2==0:
        print(i)

range(1,10,1)

for i in range(1,10,1):
    print(i)

print("------------"*4)

for i in range(10):
    print(i)

print("------------"*4)

for i in range(10,1,-1):
    print(i)


for i in range(1,11,1):
    # print("2 X", i ,"=", 2*i)
    print(f'2 X {i} ={2*i}')

# a = input("Enter any value ")
# b = int(a)
# print("User input",a)
# print(type(b))

for i in[1,2,3]:
    for j in [2,3,4]:
        print(i,j)
    print("------------"*4)

print(random.random())

data = [1,2,3,4,5,6,7]
print(random.choice(data))

print(random.randint(13,80))

data = random.randint(1,10)
for i in range(1,6):
    a  = input("Enter any number ")
    b = int(a)
    if(data==b):
        print("You got it")
        break
    else:
        print("Wrong")