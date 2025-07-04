def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)
n = 10
print(f"Factorial of {n} is {Factorial(n)}")
