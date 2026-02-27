n=int(input("Enter a number: "))

sum = 0

for i in range(1, n+1):
    sum = sum + i

print("Sum of numbers from 1 to", n, "is:", sum)
##
m = int(input("Enter a number: "))

count = 0

for i in range(1, m+1):
    if i % 2 == 0:
        count = count + 1

print("Total even numbers between 1 and", m, "are:", count)