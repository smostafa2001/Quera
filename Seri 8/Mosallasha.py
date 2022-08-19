s=[""," ","   ","     ","****"]
s1=["* ","   ","     ","***"]
s2=["* ","   ","     ","****"]
n=int(input())
c=4*n
for i in s:
    print(' '*c,end='')
    print(i)
    c-=1
if n>1:
    for f in range(2, n+1):
        d=5
        i=0
        length=3 #sabet
        while i<=length:
            print(' '*c,end='')
            for j in range(f-1):
                print(s1[i]+' '*d,end='')
            print(s2[i],end='\n')
            c-=1
            d-=2
            i+=1