import random
i = 1
while i == 1:
    print("Hello world")
    i = 2
    print("--------"*4)

i = 0
while(i<=10):
    print(i)
    i = i+1

# random_com = (random.randint(1,50))
# print("random number is",random_com)
# count = 0

# while True:
#     user = int(input("Enter any number"))
#     count = count + 1
#     if(user == random_com):
#      print("You got it ",count," chance !!")
#      break
#     elif(user>random_com):
#      print("Lower")
#     elif(user<random_com):
#      print("higher")

    


random_com = (random.randint(1,50))
print("random number is",random_com)
count = 0
max_attempt = 5
print("You have maximum 5 chance")
while True:
    if(count>=max_attempt):
     print("Limit reached")
     print("random number is",random_com)
     break
    count = count + 1
    user = int(input("Enter any number "))
    if(random_com==user):
     print("You have got it in",count,"chance !!")
     break
    elif(user>random_com):
     print("Lower")
    elif(user<random_com):
     print("higher")
    else:
     print("Try Again !!")
     
    