# math -> Includes advance math functions and constants

import math

#Square root -> sqrt()

# a = math.sqrt(10)
# print(a)

#Constant PI
Pi = math.pi


#Sine function

# a = math.sin(Pi/2)

#Cosine function

# b = math.cos(0)

#Tangent function

# c = math.tan(Pi/4)


# print(a, b, c)


#Exponential function

#e^2 (gives the value of const(e) raise to the power)

# a = math.exp(2)
# print(a)

#Ceiling and flooring

# a = math.ceil(3.01)
# b = math.floor(3.99)

# print(a, b)

#Program to calculate area of circle

# radius = float(input("Enter radius: "))

# area = Pi * radius ** 2

# print(f"Area of circle with radius {radius} is {area}")

#timeit Module -> Measures execution time

# import timeit

#Usage

# time = timeit.timeit("print('TEST')", number=1000)
# print(f"Execution time is: {time}")
# x = 0

# time = timeit.timeit("for i in range(100): pass", number = 1000)
# print(time)

#Calendar Module -> Handle calendar related functions

import calendar

#Displaying calendar of a month of any year

# cal = calendar.month(2029, 8)
# print(cal)

#print month names

# for i in range(1, 13):
    # print(calendar.month_name[i])
    
#Check if it is a leap year or not

# YEAR = int(input("Enter an year: "))
# print(f"Year is leap? {calendar.isleap(YEAR)}")

#Day of the week for a date

# day = calendar.weekday(2025, 7, 25)

# print(day)  #0 -> Monday....onwards


#To print calendar of an year
# YEAR = int(input("Enter an year: "))

# for month in range(1, 13):
    # print(calendar.month(YEAR, month))
    # print()
    
#Count how many friday 13th occur in given year

# YEAR = int(input("Enter an year: "))

# count = 0

# for month in range(1, 13):
#     if calendar.weekday(YEAR, month, 13) == 4:
#         count += 1
# print(count)

# FUNCTOOLS module -> Offers higher-order functions that acts on the function, or on some other functions

# -> lru_cache -> usage of lru_cache is called memoization (Decreases complexity)

# fibbonacci series -> 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# Time complexity of recursion -> O(n^2)

# import functools
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fab(n):
#     if n <= 1:
#         return n
#     else:
#         return fab(n-1) + fab(n-2)
# print(fab(77))