n=int(input())
first=1
second=2
fibs=[]
while len(fibs)!=n:
    fibs.append(first)
    first,second=second,first+second
print(fibs[-1])