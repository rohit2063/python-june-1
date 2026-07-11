# f = open("demo.txt","r")

# data = f.read()
# print(data)
# data1 = f.readline()
# print(data1)

# data2 = f.readline()
# print(data2)

# data3 = f.readline()
# print(data3)

# f.close()

# f = open("demo.txt","a")
# f.write("\nI will move to javascript after python..")
# f.close()

# f = open("sample.txt","w")
# f.close()

# f = open("demo.txt","w+")
# f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")

# import os
# os.remove("sample.txt")

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)
# def check_for_word():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#            print("Found")
#         else:
#             print("Not Found")

# check_for_word()

# def check_for_line():
#     word = "pqr"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
    
#     return -1

# print(check_for_line())
# def even_number():
#     # count = 0
#     data1 = int(data)
#     data1 = True
#     with open("practice.txt","r") as f:
#        while data:
#             data = f.read()
#             if(data1%2 == 0):
#                 print(data)

# even_number()

count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

nums = data.split(",")
for value in nums:
    if(int(value) % 2 == 0 ):
        print(int(value))
        count += 1

print(count)


