
from math import sqrt
def Checkit():
    if a >= 0 and a < n and b >= 0 and b < n:
        return True 
    else:
        return False

def CheckSide():
    if result == 'up':
        return side[0]
    else:
        return side[side.index(result)+1]
def Next():
    a = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in range(4):
        if side[i] == result:
            return x+a[i][0],y+a[i][1]

def GetNumber():
    checklist[x][y] = True
    return eval(mylist[x][y])

def CheckPoint():
    Number = sqrt(Total)
    if Number == int(Number):
        return 1
    else:
        return 0
n = int(input())
if n >= 1 and n <= 5:
    mylist = []
    for num in range(n):
        Number = input().split()
        mylist.append(Number)
    checklist = [[False for _ in range(n)] for _ in range(n)]
    Total = Points = x = a = 0
    y = b = -1
    side = ["right",'down','left','up']
    result = side[0]
    for i in range(n*n):
        a,b = Next()
        if Checkit() and checklist[a][b] == False:
            x,y = a,b
            Total += GetNumber()
            Points += CheckPoint()
        else:
            result = CheckSide()
            x,y = Next()
            Total += GetNumber()
            Points += CheckPoint()
    print(Points)