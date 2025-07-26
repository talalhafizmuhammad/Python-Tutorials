"""
Topic: Functions and Recursion (Revision)
Covers:
- Defining functions
- Parameters and return values
- Default arguments
- *args and **kwargs
- Recursion (factorial and Fibonacci)
"""

# Basic function
def greet():
    print('Hello')

greet()

# Parameters and return values
def add(a, b):
    return a + b

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
print(f"Sum is: {add(a, b)}")

# Default arguments
def add_default(a=5, b=7):
    return a + b

print(f"Default sum: {add_default()}")

# *args: multiple positional arguments (as tuple)
def scores(*abc):
    print(f"Scores: {abc}")

scores(65, 77, 88)

# **kwargs: multiple keyword arguments (as dictionary)
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name='Ali', age=21)

# Using both *args and **kwargs
def details(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

details(10, 20, 35, name='Ahmad', age=25, course='AI')

# Recursion: function that calls itself (with base case)

# Factorial using recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {n} is {fact(n)}")

# Fibonacci using recursion
def fibb(n):
    if n <= 1:
        return n
    else:
        return fibb(n - 1) + fibb(n - 2)

n = int(input("Enter nth term to find in Fibonacci sequence: "))
print(f"{n}th value in Fibonacci sequence is {fibb(n)}")
