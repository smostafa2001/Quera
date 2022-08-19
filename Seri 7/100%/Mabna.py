a,b=map(int,input().split())
def numberToBase(n,b=2):
    strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:return 0
    numbers=''
    while n:
        numbers += strings[n % b]
        n //= b
    return numbers[::-1]
c=list(numberToBase(a,b))
c=[int(i) for i in c]
sum1=0
sum2=0
for i in range(0,len(c),2):sum1+=c[i]
for j in range(1,len(c),2):sum2+=c[j]
if sum1==sum2:print('Yes')
else:print('No')