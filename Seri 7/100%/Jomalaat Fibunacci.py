n=int(input())
def fib(n):
    if n==0:return 0
    if n==1:return 1
    return fib(n-1) + fib(n-2)
fibs=[fib(i) for i in range(2,30) if fib(i)<=n]
print(fibs)