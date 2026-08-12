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

#multiple inheritance

class Father:
    def skill1(self):
        print("Father's skill")


class Mother:
    def skill2(self):
        print("Mother's skill")


class Child(Father, Mother):
    def skill3(self):
        print("Child's skill")

child = Child()
child.skill1()
child.skill2()
child.skill3()