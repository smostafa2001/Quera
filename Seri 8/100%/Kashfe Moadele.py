import math
n=int(input())
Xs=[]
Ys=[]
for i in range(n):
    x,y=input().split()
    Xs.append(x)
    Ys.append(y)
Xs=[float(i) for i in Xs]
Ys=[float(i) for i in Ys]
zipped=zip(Xs,Ys)
coordinates=list(zipped)
def one(x,y):
    yn=x-math.floor(x)
    if abs(y-yn)<=0.2:return True
    return False
def two(x,y):
    yn=x**2+x
    if abs(y-yn)<=0.2:return True
    return False
def three(x,y):
    yn=abs((-1*(x**3))+1)+(x**3)
    if abs(y-yn)<=0.2:return True
    return False
a=0
b=0
c=0
for i in coordinates:
    if one(*i):a+=1
for i in coordinates:
    if two(*i):b+=1
for i in coordinates:
    if three(*i):c+=1
if a==n:print('1')
if b==n:print('2')
if c==n:print('3')
if a!=n and b!=n and c!=n:print('No ones')