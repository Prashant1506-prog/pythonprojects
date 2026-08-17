#getter and setter methods

class Employee:
    def __init__(self):
        self.__salary = int(input("Enter the current salary:"))
    def get_salary(self):
        return self.__salary
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount!")

emp = Employee()
print(f"current salary: {emp.get_salary()}")
emp.set_salary(int(input("Enter the new salary:")))
print(f"Updated salary: {emp.get_salary()}")


#name mangling

class Student:
    def __init__(self, name):
        self.__name = name
s = Student("prashant")
print("s._Student__name")

