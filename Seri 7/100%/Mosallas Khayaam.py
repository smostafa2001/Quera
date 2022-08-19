n=int(input())
def khayyam_mosallas(n):
    list1=[[1]*i for i in range(1,n+1)]
    for i in range(2,n):  
        for j in range(1,i):list1[i][j]=list1[i-1][j-1]+list1[i-1][j]
    return list1        
mosallas=[str(i) for i in khayyam_mosallas(n)]
mosallas=[i.replace(',','') for i in mosallas]
mosallas=[i.replace('[','') for i in mosallas]
mosallas=[i.replace(']','') for i in mosallas]
for satr in mosallas:print(satr)