'''functions are blocks of code which can be used multiple times

def greet():
    print('Hello World')
greet()
greet()

def greetName(name):
    print(f"Name: {name}")
greetName('Talal')

def add(a, b):
    return a + b
print(add(2, 3))

def greetName(name = 'Talal'):
    print(f"Name: {name}")
greetName("Ali")

def square(a = 5):
    return a*a
print(square(3))

arbitrary arguments (*args) and arbitrary keyword arguments (**kwargs)

def sumAll(*args):
    total = 0 
    for i in args:
        total += i
    return total
print(f"Sum is: {sumAll(10, 20, 30, 40, 50)}")
print(f"Sum is: {sumAll(1, 2, 3)}")

def printInfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
printInfo(name = 'Ahmad', age = 40, city = 'Lahore', gender = 'Male')

fuction scope
scope outside the func
x = 10
def myFunc():
    #scope inside the func
    y = 20
    print(f"Inside Func: x:{x}, y:{y}")
myFunc()
print(f"Outside Func: x:{x}, y:{y}")

Recursion: a function calls itself as many times as the base case is reached to stop it

Example 1: Factorial

7 = 7*6*5*4*3*2*1*1
6 = 6*5*4*3*2*1

def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)
n = 10
print(f"Factorial of {n} is {Factorial(n)}")

Example 2: nth Fibonacci sequence
0, 1, 1, 2, 3, 5, 8, 13, ....
return fibonacci(n-1) + fibonacci(n-2)

Conatact app, add contacts, show, search, update, delete, exit
'''
