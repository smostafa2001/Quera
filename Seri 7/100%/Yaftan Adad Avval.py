n=int(input())
n1=list(str(n))
n1=[int(i) for i in n1]
b=sum(n1)
primes=[]
for i in range(n,n+1000):
    shomarande=0
    for j in range(2,i//2+1):
        if i%j == 0:
            shomarande+=1
            break
    if shomarande==0 and i!=1:primes.append(i)
if n in primes:print(primes[b])
else:print(primes[b-1])
