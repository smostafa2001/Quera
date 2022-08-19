def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        fact *= i
    return fact


n = int(input())

if n == 1:
    print(0)
else:
    print(int(factorial(n) / (factorial(n - 2) * factorial(2))))
