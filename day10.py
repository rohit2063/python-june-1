def user_info(fname, lname):
    return f'My name is. {fname} {lname}'

#Positional argument
print(user_info("Ghimire", "Rohit"))

#Keyword argument
print(user_info(fname="Rohit", lname="Ghimire"))

def test():
    pass
#same line 10,11 and 13
def test():...

def add():
    return 1,"Hello",[1,2,3,4]

print(add())

def test():
    return 1,2 

a,b = test()
#a,b = (1,2)
print(a,b)

# Wap to create a function, and sum the number of args should be in list of integer, if args is not list throw error..


def add_number(data):
    global total
    total = 0
    for i in data:
        total = total + i
    return total

print(add_number([1,2,3,4,5,6]))
print(total)

def area(r,pie = 3.14):
    return pie*r*r

print(area(7))
print(area(7,4))

