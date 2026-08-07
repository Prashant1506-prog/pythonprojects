for i in range(1, 11):
    print(i)

for v in range(0, 10, 2):
    print(v)

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"The sum of numbers from 1 to {n} is: {total}")
