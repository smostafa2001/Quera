n=int(input())
def hexa(n):
    mylist=[0] * 11
    mylist[0] = 1
    for i in range(1,11):mylist[i]=mylist[i-1]*2
    count=1
    ans=0
    while n:
        if (n%10==1):ans+=mylist[count-1]
        elif (n%10>1):ans=mylist[count]-1
        count+=1
        n//=10
    return ans
print(hexa(n))