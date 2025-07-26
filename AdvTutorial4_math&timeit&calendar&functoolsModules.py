"""
Topic: Python Modules - math, timeit, calendar, functools
Covers:
- Math operations and constants
- Measuring execution time
- Working with calendars
- Memoization using lru_cache
"""

# ===== math module =====
import math

# Square root
a = math.sqrt(10)
print(f"Square root of 10: {a}")

# Constant Pi
Pi = math.pi
print(f"Value of Pi: {Pi}")

# Trigonometric functions
sin_val = math.sin(Pi / 2)
cos_val = math.cos(0)
tan_val = math.tan(Pi / 4)
print(f"sin(pi/2): {sin_val}, cos(0): {cos_val}, tan(pi/4): {tan_val}")

# Exponential function: e^2
exp_val = math.exp(2)
print(f"e^2 = {exp_val}")

# Ceiling and Floor
ceil_val = math.ceil(3.01)
floor_val = math.floor(3.99)
print(f"Ceiling: {ceil_val}, Floor: {floor_val}")

# Area of a Circle
radius = float(input("Enter radius: "))
area = Pi * radius ** 2
print(f"Area of circle with radius {radius} is {area}")


# ===== timeit module =====
import timeit

# Measure execution time of a simple print statement
time = timeit.timeit("print('TEST')", number=1000)
print(f"Execution time for print 1000 times: {time}")

# Measure execution time of a loop
time = timeit.timeit("for i in range(100): pass", number=1000)
print(f"Execution time for loop: {time}")


# ===== calendar module =====
import calendar

# Display calendar for a specific month
print("Calendar for August 2029:")
print(calendar.month(2029, 8))

# Print month names
print("Month Names:")
for i in range(1, 13):
    print(calendar.month_name[i])

# Check for leap year
YEAR = int(input("Enter a year to check for leap year: "))
print(f"Is {YEAR} a leap year? {calendar.isleap(YEAR)}")

# Get day of the week for a specific date
day = calendar.weekday(2025, 7, 25)
print(f"Day of week for 25 July 2025 is: {calendar.day_name[day]}")

# Print full calendar of a year
YEAR = int(input("Enter a year to print its calendar: "))
for month in range(1, 13):
    print(calendar.month(YEAR, month))
    print()

# Count number of Friday 13ths in a year
YEAR = int(input("Enter a year to count Friday the 13ths: "))
count = 0
for month in range(1, 13):
    if calendar.weekday(YEAR, month, 13) == 4:  # 4 = Friday
        count += 1
print(f"Number of Friday 13ths in {YEAR}: {count}")


# ===== functools module =====
import functools
from functools import lru_cache

# Fibonacci using recursion with memoization
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter n to get nth Fibonacci number: "))
print(f"{n}th Fibonacci number is {fib(n)}")
