n = int(input())
for i in range(1,n+1,2):
    a1=i*'*'
    a2=i*'*'
    b1=a1.center(n)
    b2=a2.center(n)
    print(b1,b2,sep='')
for j in range(2,n,2):
    c1=(n-j)*'*'
    c2=(n-j)*'*'
    d1=c1.center(n)
    d2=c2.center(n)
    print(d1,d2,sep="")
