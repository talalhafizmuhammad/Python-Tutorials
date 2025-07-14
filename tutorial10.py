'''Exception Handling
Exception: Errors that occurs during the program execution, without handling them the program would crash 

Exception Handling:
    try:
    except:

crashed program
num = int(input("Enter a number: "))
print(f"Num's half is {num/2}")

try:
    num = int(input("Enter a number: "))
    print(f"Half of num is {num/2}")
except:
    print("Something went wrong, please enter a valid number")
    
ValueError, ZeroDivisionError

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Result = {a / b}")
except ZeroDivisionError:
    print("You can not divide by zero")
except ValueError:
    print("Please enter only numbers")
    
age = int(input())

if age < 0:
    raise ValueError("Age can't be negative")
else:
    print(f"Valid age: {age}")

height = float(input('Enter: '))
if height < 0:
    raise ValueError("Height should be greater than 0")
else:
    print("Your height: ", height)

-> Take a num1 and divide by num2, handle both ValueError and ZeroDivisionError


try:
    num1 = int(input("Enter a number (Dividend): "))
    num2 = int(input("Enter a number (Divisor): "))
    print("value is", num1/num2)
except ValueError:
    print('You entered an irrelevant datatype')
except ZeroDivisionError:
    print("Cannot divide by zero")

-> Ask for someone's name and raise error if let blank

name = (input("Enter your name: "))
if name == '':
    raise ValueError("Name cannot be empty")
else:
    print(f"Your name is {name}")
'''