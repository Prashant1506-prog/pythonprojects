#decorators 

def decorator(func):
    def wrapper():
        print("before")
        func()
        print("After")
    return wrapper


def greet ():
    print("hello")
greet = decorator(greet)
greet()

#decorators with args and kwargs

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3))

#function decortors 

def simple_decorator(func):
    def wrapper():
        print(">>> Starting function")
        func()
        func()
        print(">>> Function finished")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")
greet = simple_decorator(greet)
greet()

#method decorators

def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("before")
        result = func(self, *args, **kwargs)
        print("After")
        return result
    return wrapper

class Myclass:
    @method_decorator
    def my_method(self):
        print("Inside")
obj = Myclass()
obj.my_method()