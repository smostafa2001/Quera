n=int(input())
def Factorial(n):
    if n==0:return 1 
    elif n==1:return 1
    else:return n*Factorial(n-1)
print(Factorial(n))