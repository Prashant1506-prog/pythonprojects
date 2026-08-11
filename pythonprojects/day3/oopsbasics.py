class Student:

    def show(self):
        print("Student object:")

s1 = Student()
s1.show()
s2 = Student()
s2.show()

class Student:

    def __init__(self):
        print("Student created")

s1 = Student()

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("hh", 20)
print(s1.name)
print(s1.age)

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)
        print("My course is", self.course)


student1 = Student("Prashant", 20, "BCA")

student1.introduce()