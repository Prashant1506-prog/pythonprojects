#compile time polymorphism using argument

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))

#runtime polymorphism 

class Animal:
    def sound(self):
        return "Some generic animal sound"
class Dog(Animal):
    def sound(self):
        return "bhayuuu"
class Cat(Animal):
    def sound(self):
        return "meaaayyuuuu"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

#polymorphism in built in function

print(len("Hello"))  
print(len([1, 2, 3])) 

print(max(1, 3, 2))  
print(max("a", "z", "m"))  

#method overriding

class Animal:
    def display(self):
        print("This is an animal")
class Dog(Animal):
    def display(self):
        print("This is dog")

obj = Dog()
obj.display()

#method overriding with super() and constructor

class Employee:
    def __init__(self):
        self.role = "Employee"
    def display(self):
        print("Role: ", self.role)
class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.role = "manager"

    def display(self):
        print("Role: ", self.role)

e1 = Employee()
e2 = Manager()
e1.display()
e2.display()

#operator overloading using built in functions

class A:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value

ob1 = A(5)
ob2 = A(5)
print(ob1 + ob2)
print(ob1.__add__(ob2))
print(ob1.value + ob2.value)