# marks = [34, 43, 54 ,23 ,67]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ["karan", 95.5 , "Delhi"]
# student[0] = "Rohit" # no error because the list is mutable data types
# print(student)

#List Slicing
# marks = [34, 43, 54 ,23 ,67]
# print(marks[1:-1])

#List methods
Fruits = ["apple", "banana", "orange" ,"litchi" ,"mango"]
# print(Fruits.append("guava"))
# print(Fruits.sort(reverse=True))
# print(Fruits)
# Fruits.reverse()
# print(Fruits)
# Fruits.insert(1,"Papaya")
# print(Fruits)
# Fruits.remove("mango")
# print(Fruits)
print(Fruits.pop(1))
# print(Fruits)

#Tuple
# Fruits = ("apple", "banana", "orange" ,"litchi" ,"mango")
# print(type(Fruits))
# print(Fruits[0])
# Fruits[0] = "Guava" Error because the tuple is immutable data types like string..

# tup = (1.0)
# print(tup)
# print(type(tup)) # if we don't have comma after its fist element in the tuple it gives type according to its data type..

# tup = (1.0,2 ,3 , 4)
# print(tup.index(1.0)) #provides us the index of the element that we pass through the  parenthesis
# print(tup.count(1.0)) #counts the element pass through parenthesis that how many times does the element gets repeats

#Wap to ask user his/her favorite movie and store them in list
# movies = []
# movies.append(input("Enter your first favorite movie:"))
# movies.append(input("Enter your second favorite movie:"))
# movies.append(input("Enter your third favorite movie:"))

# print(movies)

#Wap to check if the list contain the palindrome of elements
# list1 = ["r", "a", "c" , "e", "c", "a", "r"]

# a = list1.copy()
# a.reverse()

# if(a == list1):
#     print("The given list is a palindrome list..")
# else:
#     print("The given list is not a palindrome list..")
# WAP to count the number of student with the grade "A" in following tuple
# tup = ("A", "B", "C", "A", "D", "A")

# print(tup.count("A"))
