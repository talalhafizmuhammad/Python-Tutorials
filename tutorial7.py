'''Functions and recursion (revision)

Define functions
Parameters and return values
Default args
args and *kwargs
Recursion

Function provides reusability, organized, modular code

def greet():
    print('Hello')
greet()

parameters and return values

def add(a, b):
    return a + b
a = int(input('1:'))
b = int(input('2:'))
print(add(a,b))

Default args

def add(a = 5, b = 7):
    return a + b
print(add()) #12

args: multiple positional args (tuple)

def scores(*abc):
    print(f"Scores: {abc}")
    
scores(65, 77)

*kwargs: multiple keyword arguments (dictionaries)

def profile(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")
profile(name = 'Ali', age = 21)

using args and *kwargs together

def details(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")
details(10, 20, 35, 47, -11, name = 'Ahmad', age = 25, course = 'AI')

RECURSION: Function that calls itself (req: 1. Base case 2. Recursive call)

factorial
 7! = 7*6*5*4*3*2*1!

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
n = int(input('Enter a number: '))
print(f"Factorial of {n} is {fact(n)}")

Recursion (2)

nth fibonacci 

0, 1, 1, 2, 3, 5, 8, 13, 21, ...
n = 6

def fibb(n):
    if n <= 1:
        return n
    else:
        return fibb(n - 1) + fibb(n - 2)
n = int(input())
print(f"{n}th value of seq is {fibb(n)}")
'''