for i in range(1, 11):
    print(i)

for v in range(0, 10, 2):
    print(v)

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"The sum of numbers from 1 to {n} is: {total}")

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

for i in range(1, 6):
    print("*" * i)

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)