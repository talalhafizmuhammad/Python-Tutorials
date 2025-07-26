"""
Topic: Exception Handling in Python
Description: Demonstrates how to handle runtime errors like ValueError and ZeroDivisionError,
             and how to raise custom exceptions using raise.
"""

# Example of a crashed program (no exception handling)
# num = int(input("Enter a number: "))
# print(f"Num's half is {num / 2}")

# Safer version with try-except
try:
    num = int(input("Enter a number: "))
    print(f"Half of num is {num / 2}")
except:
    print("Something went wrong, please enter a valid number.")

# Handling multiple specific exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Result = {a / b}")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter only numeric values.")

# Raising custom exception for age
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age can't be negative.")
    else:
        print(f"Valid age: {age}")
except ValueError as e:
    print("Error:", e)

# Raising custom exception for height
try:
    height = float(input("Enter your height in cm: "))
    if height < 0:
        raise ValueError("Height must be a positive number.")
    else:
        print("Your height:", height)
except ValueError as e:
    print("Error:", e)

# Take num1 and divide by num2, handle both errors
try:
    num1 = int(input("Enter a number (Dividend): "))
    num2 = int(input("Enter a number (Divisor): "))
    print("Result:", num1 / num2)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Ask name and raise error if left blank
name = input("Enter your name: ")
if name.strip() == '':
    raise ValueError("Name cannot be empty.")
else:
    print(f"Your name is {name}")
