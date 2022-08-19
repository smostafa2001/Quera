t=int(input())
n=[]
for i in range(1,t+1):
    n.append(int(input()))
#def isAval(n):
#   shomarande=0
#    for i in range(1,n+1):
#        if n%i==0:
#            shomarande=shomarande+1
#    if shomarande==2:
#        return True
#    return False
def tajziye(n):
    avamel=[]
    cleanAvamel=[]
#    if isAval(n)==True:
#        return avamel.append(n)
    while n%2==0:
        n=n/2
        avamel.append(2)
    while n%3==0:
        n=n/3
        avamel.append(3)
    while n%5==0:
       n=n/5
       avamel.append(5)
    while n%7==0:
        n=n/7
        avamel.append(7)
    while n % 11 == 0:
        n = n/11
        avamel.append(11)
    while n % 13 == 0:
        n = n/13
    avamel.append(13)
    while n % 17 == 0:
        n = n/17
    avamel.append(17)
    while n % 19 == 0:
        n = n/19
    avamel.append(19)
    for item in avamel:
        if item not in cleanAvamel:
            cleanAvamel.append(item)
    return(cleanAvamel)
def sumAvamel(n):
    #if tajziye(n)==None:
    #    return
    return sum(tajziye(n))
def sumAdad(n):
    n1=str(n)
    n2=list(n1)
    n3=[int(i) for i in n2]
    return sum(n3)
def d(x):
    #if isAval(x)==True:
    #    return
    return sumAvamel(x)+sumAdad(x)+(x)
def hasFather(n):
    father=0
    for i in range(1,n+1):
        if d(i)==n:
            father+=1
    if father==0:
        return'No'
    else:
        return'Yes'
for i in n:
    print(hasFather(i))



