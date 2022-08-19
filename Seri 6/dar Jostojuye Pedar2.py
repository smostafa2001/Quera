t=int(input())
n=[]
for i in range(1,t+1):
   n.append(int(input()))
primes=[]
def primeNumbers(la):
    for i in n:
        for j in range(2,i+1):
            if j%2!=0 and j%3!=0 and j%5!=0 and j%7!=0 and j%11!=0 and j%13!=0 and j%17!=0 and j%19!=0:
                primes.append(j)
            
    return primes
for i in n:
    print(primeNumbers(i))