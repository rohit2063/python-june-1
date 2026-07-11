# class Student:
#     name = "Karan Kumar"
#     Rollno = 101

# s1 = Student()
# print(s1.name)
# print(s1.Rollno)

# class Car:
#     color = "blue"
#     brand = "Mercedes"
    # Defult Constructor
#     def __init__(self):
#         pass

    # Parameterized constructor
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("Adding new Student to Database..")

# car1 = Car("Karan", 95)
# print(car1.name,car1.marks)

# car2 = Car("Rohit", 97)
# print(car2.name,car2.marks)

# print(car1.color)
# print(car1.brand)

# class Name:
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#     def welcome(self):
#         print("Welcome Student",self.name)
#     def get_marks(self):
#         print("Your marks is",self.marks)
        
# s1 = Name("Rohit Ghimire", 95)
# s1.welcome()
# s1.get_marks()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_average(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val
#         print("Hi",self.name,"your average score is",sum/3)

# s1 = Student("tony stark", [99, 98, 97])
# s1.get_average()

# s1.name = "Rohit Ghimire"
# s1.get_average()

# class Student:
#     @staticmethod
#     def hello():
#         print("hello")

# s1 = Student()
# s1.hello()

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Your car is being start..")

# car1 = Car()
# car1.start()

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.accountno = acc
    def debit(self, money):
        self.money = money
        CurrentBalance = self.balance - money
        print("Your account",self.accountno,"is being debited by Rs",money,".","Now Your Current Balance is Rs",CurrentBalance)

    def credit(self, Balance):
        self.Balance = Balance
        print("Your account",self.accountno,"is being credited by", Balance,".","Now Your Current Balance is Rs",self.balance + self.Balance)

s1 = Account(10000, 12345)
s1.debit(10000)
s1.credit(2000)
s1.debit(1000)
s1.credit(20000)

