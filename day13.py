class Test():
    a = 10
    b = 11

obj = Test()
print(obj)
print(obj.b)
obj.a = 60
obj.c = 90
print(obj.a)
print(obj.c)

obj1 = Test()
print(obj1.a)
# print(obj1.c)

print(obj1 == obj)


class math():
    a = 10
    b = 50

    def add(self):
        self.c = 10
        return self.a+self.b+self.c
    
obj = math()
print(obj.add())
print(obj.c)

# output function or string function
class test():
    message = 'this is testing'

    def __str__(self):
        return self.message
    
obj = test()
print(obj)


class test():

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I am from class test")
        return
    
    def add(self,c):
        return self.a+self.b+c
    
obj = test(10,60)
print(obj.add(11000))

class BankAccount():
        def init(self, account_holder, balance):
            self.account_holder = account_holder
            self.balance = balance
        
        def deposit(self, amount):
           if amount <= 0:
            print("Deposit amount must be positive.")
            return
           self.balance = self.balance + amount
           print(f"Deposited {amount}. New balance: {self.balance}")

        def withdraw(self, amount):
           if amount <= 0:
            print("Withdraw amount must be positive.")
            return
           if amount > self.balance:
            print(f"Insufficient funds. Available balance: {self.balance}")
            return
           self.balance = self.balance - amount
           print(f"Withdraw {amount}. New balance: {self.balance}")

        def show_balance(self):
            print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

obj = BankAccount("hari",2000)
print(obj.deposit(500))
print(obj.withdraw(1000))
print(obj.show_balance())
        


