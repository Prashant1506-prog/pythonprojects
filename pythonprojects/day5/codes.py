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