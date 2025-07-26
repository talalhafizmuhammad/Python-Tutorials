"""
Topic: Python Basics Revision
Covers: Variables, Data Types, Type Casting, Conditions, Loops, Match-Case
"""

# Variables and Data Types
name = 'Ali'         # string
age = 20             # integer
pi = 3.14            # float
is_student = True    # boolean

print(type(name))
print(type(age))
print(type(pi))
print(type(is_student))

print(name, age, pi, is_student)

# Input and Type Checking
a = input("Enter a string: ")
print(a, type(a))

a = int(input("Enter an integer: "))
print(a, type(a))

# Type Casting
a = input("Enter: ")
print(a, type(a))
a = int(a)
print(a, type(a))

# Sum of two numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(f"Sum is {a + b}")

# Conditions: if, elif, else
# Check if a number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Check if a number is divisible by 3 or 5 or both
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 only")
elif num % 5 == 0:
    print(f"{num} is divisible by 5 only")
else:
    print(f"{num} is not divisible")

# Match-case statement (Python 3.10+)
num = int(input("Enter a number: "))
match (num % 3 == 0, num % 5 == 0):
    case (True, True):
        print("Both divisible")
    case (True, False):
        print("Divisible by 3 only")
    case (False, True):
        print("Divisible by 5 only")
    case _:
        print("Not divisible by 3 or 5")

# While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# For loop
for i in range(1, 11):
    print(i)

# Multiplication Table of 5
a = 5
for i in range(1, 11):
    print(f"{a} * {i} = {a * i}")
