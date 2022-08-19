numbers=input().split()
numbers=[int(i) for i in numbers]
m=max(numbers)
n=min(numbers)
def gcd(m,n):
    while n:
        m,n=n,m%n
    return m
lcm=abs(m*n)//gcd(m,n)
print(gcd(m,n),lcm)