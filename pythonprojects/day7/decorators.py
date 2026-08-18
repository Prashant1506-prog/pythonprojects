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

