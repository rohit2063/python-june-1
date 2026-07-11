# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Rohit Ghimire")
# print(s1.name)
# del s1.name
# print(s1.name)

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def __reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account(12345, "Abcde")

# print(acc1.acc_no)
# # print(acc1.__acc_pass)
# print(acc1.__reset_pass())

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped..")

class Toyotacar(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("Fortuner")
car2 = Toyotacar("Mercedes")
print(car1.color)
        