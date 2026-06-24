# class Parent():
#     a = 20
#     b = 11

#     def display(self):
#         return "This is from parent class"

#     def add(self):
#         return self.a + self.b

# class child(Parent):
#     a = 2
#     c = 60
#     d = 200

# obj = child()
# print(obj.add())
# print(obj.c)
# print(obj.d)
# print(obj.b)
# print(obj.a)
# print(obj.display())

# class Parent():
#     def __init__(self):
#         print("parent constructor")

# class child(Parent):
#     def __init__(self):
#         print("Child constructor")
#         # Parent.__init__(self)
#         super().__init__()

# class GrandChild(child):
#     d = 2

# obj = GrandChild()

# class Course():
#     course_name = "Python"
#     ins_name = "Sudan"
#     duration = "1 hour"

#     def show_course_details(self):
#         return f'''
#         Course: {self.course_name}
#         instructor: {self.ins_name}
#         duration: {self.duration}
# '''


# class OnlineCourse(Course):
#     platform_name = "Google Meet"
#     course_link = "jkslfjd.kljdlfds"

#     def show_platform_details(self):
#         return f'''
#         Platform_name: {self.platform_name}, 
#         Course_Link: {self.course_link}
# '''


# class PaidOnlineCourse(OnlineCourse):
#     price = 124
#     payment_status = "Completed"

#     def show_payment_detail(self):
#         return f'''
#         Price: {self.price}, 
#         Payment Status: {self.payment_status}
# '''

# paid_obj = PaidOnlineCourse()
# print(paid_obj.show_course_details())
# print(paid_obj.show_platform_details())
# print(paid_obj.show_payment_detail())

class parent():
    a = 100

    def display(self):
        return "from parent class"
    
class parent1():
    def display(self):
        return "From parent1 class"
    
class child(parent, parent1):
    a = 20

print(child.__mro__)
    
obj = child()

print(obj.display())


class test():
    __a = "testing@1"
    password1 = __a

    def login(self):
        password = self.__a
        return True
    
obj = test()
# print(obj.__a)
# print(obj.__login())
print(obj.password1)


class test():
    __a = "testing@1"
    password1 = __a

    def __login(self):
        password = self.__a
        return True
    
    def data(self):
        return self.__login()

class test1(test):

    def display(self):
        return self.password1, self.data()
    
obj = test1()
print(obj.display())


class Wallet():
    owner_name = "Rohit Ghimire"
    wallet_id = 1234
    __balance = 2000000
    __transaction_logs = "private"

    def deposite():
        return __balance + amount


    def withdraw():
        return __balance - amount


    def get_balance():
        return __balance


    def view_trancation_histroy():
        return withdraw(), deposite()


    def __add_transaction_log():
        


class child(Wallet):
    cashback_rate = "10%"


