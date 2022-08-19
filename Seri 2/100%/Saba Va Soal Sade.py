# n,k=map(int,input().split())
from math import floor


n, k = input().split()
n, k = int(n), int(k)
n //= (k*2)
print(floor(n))
# for i in range(k):n//=2
# print(n)
    