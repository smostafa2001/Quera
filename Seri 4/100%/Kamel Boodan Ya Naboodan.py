n=int(input())
avamel=[]
for i in range(1,n):
    if n%i==0:
        avamel.append(i)
if sum(avamel)==n:
    print('YES')
else:
    print('NO')