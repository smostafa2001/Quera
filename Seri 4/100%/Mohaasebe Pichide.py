def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
def c(a,b):
    return f(a)/(f(b)*f(a-b))

a,x,n=list(map(int,input().split (" ")))

s=0
for i in range(n+1):
    s+=c(n,i)*(x**i)*(a**(n-i))
print(int(s))