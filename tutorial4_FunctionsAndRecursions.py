"""
Topic: Functions and Recursion in Python
Description: Covers basics of functions, arguments, return values, *args, **kwargs, scope, and recursion.
"""

# Functions
def greet():
    print('Hello World')

greet()
greet()

def greet_name(name):
    print(f"Name: {name}")

greet_name('Talal')

def add(a, b):
    return a + b

print(add(2, 3))

# Default Parameters
def greet_name(name='Talal'):
    print(f"Name: {name}")

greet_name("Ali")
greet_name()

def square(a=5):
    return a * a

print(square(3))
print(square())

# *args
def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(f"Sum is: {sum_all(10, 20, 30, 40, 50)}")
print(f"Sum is: {sum_all(1, 2, 3)}")

# **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name='Ahmad', age=40, city='Lahore', gender='Male')

# Function Scope
x = 10

def my_func():
    y = 20
    print(f"Inside Function: x = {x}, y = {y}")

my_func()
# y is local — not accessible outside

# Recursion - Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = 6
print(f"Factorial of {n} is {factorial(n)}")

# Recursion - Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 7
print(f"{n}th Fibonacci number is {fibonacci(n)}")

# Project Idea: Contact Management App
"""
Build a CLI-based contact manager with:
- Add Contact
- Show All Contacts
- Search
- Update
- Delete
- Exit

Use:
- Dictionaries or lists
- Menu-based loop
- Functions for each feature
"""
