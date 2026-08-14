n = int(input("Enter a number: "))
s = int(input("Enter a number: "))


try:
    res = n / s
except ZeroDivisionError:
    print(f"number {n} cannot be divided by zero {s}")
else:
    print(f"Result of {n} / {s} is :{res} ")
finally:
    print("Execution completed")

#catch all the excepton ant their risks 

try:
    res = "10" / 8
except ArithmeticError:
    print(" arithmeticError")
except:
    print("Error")

#raisin an excepton by rAISE

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age is set to {age }")

try:
    set(-3)
except ValueError as e:
    print(e)

#custom exception

class MyCustomError(Exception):
    pass

def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed")
    return a / b

divide(10, 0)
try:
    result = divide(10, 0)
except MyCustomError as e:
    print(f"Caught an error: {e}")