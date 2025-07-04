'''name = 'Ali'  #string 
age = 20  #integer
pi = 3.14  #float
is_student = True  #boolean

print(type(name))
print(type(age))
print(type(pi))
print(type(is_student))

print(name, age, pi, is_student)

Task input

a = input("Enter a string: ")  #string
print(a, type(a))

a = int(input("Enter an integer: "))
print(a, type(a))

Type Casting

a = input("Enter: ")
print(a, type(a))

a = int(a)
print(a, type(a))

a = int(input("Enter 1st number: "))
b = int(input('Enter 2nd number: '))

print(f"Sum is {a + b}")

Conditions: if, elif, else, nested if

is positive or negative or 0

num = int(input("Enter a number: "))

if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print("Zero")

check whether a number is divisible by 3 or 5 or both

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 only")
elif num % 5 == 0:
    print(f"{num} is divisible by 5 only")
else:
    print(f"{num} is not divisible")

Match case

input in value

match value:
    case 1:
        print(lines)
    case 2:
        print(lines)
    case _:
        print(unknown)
num = int(input("Enter a number: "))
match (num % 3 == 0, num % 5 == 0):
    case (True, True):
        print("Both divisible")
    case (True, False):
        print("Div by 3")
    case (False, True):
        print('Div by 5')
    case (False, False):
        print('Not div')

while condition:
    code
    inc/dec

i = 1
while i <= 5:
    print(i)
    i += 1

for i in range(start, end):
    code

for i in range(1, 11):
    print(i)

Table of 5
a = 5
for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")
    '''