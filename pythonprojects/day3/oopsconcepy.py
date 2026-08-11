class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(self.balance)


class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Prashant", 101, 85)

student1.display()
student1.result()

class Animal:

    def sound(self):
        print("Some animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()