a,b=int(input()),int(input())
primes=[]
for i in range(a,b+1):
    shomarande=0
    for j in range(2,i):
        if i%j == 0:
            shomarande+=1
            break
    if shomarande==0 and i!=1:primes.append(i)
for prime in primes:print(prime)