#encapsulation

class Employee:
    def __init__(self, name, salaray):
        self.name = name
        self.__salary = salaray
emp = Employee("prashant", 100000000000)
print(emp.name)
print(emp.__salaray)

#public and protcted member use 

class BankAccount:
    def __init__(self):
        self.balance = int(input("enter the balance: "))

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}") 

    def __update_balance(self, amount):
        self.balance += amount             

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  
            self._show_balance()           
        else:
            print("Invalid deposit amount!")
            
account = BankAccount()
account._show_balance()  
x = int(input("Enter the amount to deposit: "))    
account.deposit(x)       