n,m=map(int,input().split())
peymane=[i for i in range(2,110000)if (n-m)%i==0]
for i in peymane:print(i,end=' ')