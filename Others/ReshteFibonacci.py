n=int(input())
def fib(n):
    if n==1:return 1
    if n==2: return 2
    return fib(n-1)+fib(n-2)
fibonacciNumbers=[fib(number) for number in range(1,11)]
for number in range(1,n+1):
    if number in fibonacciNumbers:print('+',end='')
    else:print('-',end='')