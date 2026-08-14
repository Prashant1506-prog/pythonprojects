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

try:
    res = "10" / 8
except ArithmeticError:
    print(" arithmeticError")
except:
    print("Error")

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age is set to {age }")

try:
    set(-3)
except ValueError as e:
    print(e)