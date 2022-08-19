n=int(input())
def fibunacci(n):
    first = 1
    second=2
    fibs=[]
    while first<=n:
        fibs.append(first)
        first,second=second,first+second
    return fibs
def jomalaat(n):
    list1 = fibunacci(n)
    list2 = fibunacci(n)
    list3 = []
    natije=n
    while natije:
        list3.append(list1.index(list2[-1])+1)
        natije-=list2[-1]
        list2=fibunacci(natije)
    for i in list3:print(i, end=" ")
jomalaat(n)