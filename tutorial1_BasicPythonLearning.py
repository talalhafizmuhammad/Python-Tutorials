# This is my first Python program

'''This is a 
multi-line comment'''

print('Hello World')

# Demonstrating types
a = 5
print(type(a))  # <class 'int'>

b = 5.5
print(type(b))  # <class 'float'>

c = 3 + 4j  # complex number
print(type(c))  # <class 'complex'>

d = """string1"""
print(type(d))  # <class 'str'>

# Addition of different types
a = 5
b = 6.5
c = 3 + 5j
d = a + b + c
print(d)
print(type(d))  # <class 'complex'>

# String + string conversion
a = 5 + 6j
b = 'a'
c = str(a) + b
print(c)

# Multiple assignment
a, b, c = 10, 20, 30
d = e = 'abc'
print(d, e)

# Input from user
a = float(input("Enter something: "))
print(a)
print(type(a))

# Formatted output
print('This is the value of', a)
print(f'This is the value of {a}')  # f-string

# Logical operators
# &&, ||, ! in C/C++ → and, or, not in Python
a = 5
b = 10
print(not a > b)  # True

# IF-ELSE
a = int(input("Enter a number: "))

if a > 1:
    print(a)

if a > 5:
    print("True")
else:
    print("False")

# Membership check using 'in'
if a in range(1, 11):
    print("Exists")
else:
    print("Does not exist")

# Identity check using 'is'
# Not recommended for primitive types, better use ==
if a == True:
    print("TRUE")

# if-elif-else
a = 10
if a > 10:
    print("Large")
elif a < 10:
    print("Small")
else:
    print("a = 10")

# Nested if
if a > 5:
    if a > 3:
        print("True")
    else:
        print("False")

# 'is' vs '=='
a, b = 5, 5
print(a is b)  # True in CPython, but prefer a == b
