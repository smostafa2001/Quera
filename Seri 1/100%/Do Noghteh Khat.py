x1,y1,x2,y2=map(int,input().split())
if y1==y2:
    print('Horizontal')
elif x1==x2:
    print('Vertical')
else:
    print('Try again')