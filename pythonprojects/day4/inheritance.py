class Vehicle:
    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass

car = Car()
bike = Bike()
car.start()
bike.start()
car.stop()
bike.stop()

#single inheritance

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")

dog = Dog()

dog.eat()
dog.bark()

# multilevel inher
class Animal:
    def eat(self):
        print("Eating")


class Mammal(Animal):
    def walk(self):
        print("Walking")


class Dog(Mammal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()

#hierarchical inheritance

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

# mro

class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass

print(D.mro())

d=D()
d.show()

#mro 
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

obj = B()
obj.show()

# code for mro

class Company:
    def work(self):
        print("Company work")


class Employee(Company):
    def work(self):
        print("Employee work")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Manager(Employee):
    def work(self):
        print("Manager manages team")


class TechLead(Developer, Manager):
    pass


person = TechLead()
person.work()