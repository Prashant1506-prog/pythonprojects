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