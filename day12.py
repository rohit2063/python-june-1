def enroll(*args, **kwargs):
    length = len(args)
    if(length==0):
        return f'{kwargs.get('name')} {kwargs.get('level','beginner')} have {length} subject enrollment'
    else:
        return f'{kwargs.get('name')} {kwargs.get('level','beginner')} have {length} subject enrollment {args}'



print(enroll(
    "Python",
    "Django",
    "SQL",
    name="Anita",
    level="Beginner"
))
# Name: level: 3 subject enroll list the subject

print(enroll(
    "Python",
    "SQL",
    name="Anita",
))



print(enroll(
    name="Anita",
))


# Lamda Function
n = lambda x,y : x+y

print(n(1,90))


a = [1,2,3,4,5,6]
output = []
for i in a:
    output.append(i*i)

print(output)


data = [i*i for i in a]
print(data)

n = lambda a : [i*i for i in a]
print(n([1,2,3,4,5]))
# Hello worldHello worldHello world

"Hello world"