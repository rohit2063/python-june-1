# f = open('day1.py','r')
# print(f.read())
# f.close()

# f = open('day17.txt','w')
# f.write("Hello world")
# f.close()

# f = open('day17.txt','a')
# f.write('\n Hello world')
# f.close()

# f = open('day12.py','r+')
# print(f.read())
# f.write("Hello world")
# f.close()

# with open('day12.py','r') as file:
#     print(file.read())


from datetime import datetime

print(datetime.now)

def error (file_name,message):
    with open(file_name, "a") as f:
      f.write(f'{datetime.now().date} {message} \n')

try:
    a = 5 / 0

except ZeroDivisionError as message:
    error("err_division.txt",message)

except NameError as message:
    error("name_error.txt",message)

except Exception as message:
    error("error.txt",message)

finally:
    print("this is running")

import csv
with open('data.csv','r') as file:
    read = csv.reader(file)
    for row in read:
        print(row)
        print(file.read())


data = [["name","age"],["Rohit",19]]
with open("data1.csv","w", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(data)
