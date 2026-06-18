#arvitory argument
def add(*data):
    print(type(data))
    print(data)
    return data

add(1,2)
add(1,2,3,4,5)
add(1,2,3,4,"Hello","Yes",5,6)
add(1)
add()

def add_number(*data):
    print(data)
    total = 0
    for i in data:
       if (i>0):
           continue
       total = total + i
    return total

print(add_number(5,-2,-5,6))

def has_duplicate(*args):
    result = [0]
    for i in args:
       if i in result:
         return True
       result.append(i)
       return False
print(has_duplicate(1,2,3,4,1,2,3,4))

def info(**data):
   print(data)

info(lname="Rohit",fname="Hello",age =20)
info(lname="Rohit",age =20)

def filter_string(**kwargs):
   result = {}
   for i in kwargs:
      if isinstance(kwargs[i], str):
         result[i]=kwargs[i]
   return result

print(filter_string(name = "Hari",address = "Nepal",age = 10,role = "developer"))

def all_args(data,*args,**kwargs):
   print(args)
   print(kwargs)
   print(data)

all_args(1,2,3,4,5,6,7,8,name = "Rohit")

def student_marks_sheets(*args,**kwargs):
   total = sum(args)
   percent = total / len(args)
   return f'{kwargs['name']} percentage is {percent}'
print(student_marks_sheets(100,30,45,60,name = "Hari"))

