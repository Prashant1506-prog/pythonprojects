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