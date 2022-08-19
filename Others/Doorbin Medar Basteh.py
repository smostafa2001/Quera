x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
coordinates=[]
coordinates.append(x1)
coordinates.append(x2)
coordinates.append(x3)
coordinates.append(y1)
coordinates.append(y2)
coordinates.append(y3)
coordinate=[]
for i in coordinates:
    if coordinates.count(i)==1:
        coordinate.append(i) 
for i in coordinate:
    print(i,end=' ')  