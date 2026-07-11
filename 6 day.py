# Function Defination
# def calc_sum(a, b): # Parameters
#     return a+b

# print(calc_sum(2, 10)) # Function call; arguments
# print(calc_sum(13, 23))

# def mul(a, b):
#     return a*b

# print(mul(2, 6))

# def print_hello():
#     print("Hello")
# output = print_hello()
# print(output)  # if the function don't have return type then when we try to print it by storing it in another variable then it gives the output none

# To find the average of three number
# def average(a, b, c):
#     sum = a+ b+ c
#     return sum / 3

# print(average(1, 2 ,3))

# print("Hello", end=" ")
# print("World")

# def calc_len(a = [1, 2, 3, 4, 5]):
#     return len(a)

# print(calc_len())

# a = ["a", "b", "c", "d"]
# def output_of_list(list):
#     for item in list:
#         print(item, end=" ")

# output_of_list(a)

# n = int(input("Enter any number:"))
# def factorial_of_num(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact


# print(factorial_of_num(n))

# n = int(input("Enter any number:"))
# def fact_of_num(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         a = n * fact_of_num(n - 1)
#         return a
    

# print(fact_of_num(n))

# a = int(input("Enter any number:"))
# def rupee_to_indian(a):
#     return a * 83

# print("The indian rupee of",a,"usd is",rupee_to_indian(a))

# Recursion Function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# n = int(input("Enter any number:"))
# def sum_of_natural_num(n):
#     if(n == 0):
#         return 0
#     return sum_of_natural_num(n-1) + n
# print(sum_of_natural_num(n))

# n = [1, 2, 3, 4, 5, 6]
# def print_List_value(n, indx):
#         if(indx == len(n)):
#             return 
#         print(n[indx])
#         print_List_value(n, indx+1)

# print_List_value(n, 0)