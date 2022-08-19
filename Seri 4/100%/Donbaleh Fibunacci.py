n,n1=int(input()),int(input())
fibs=[]
first,second=1,1
while True:
    fibs.append(first)
    first,second=second,first+second
    if fibs[-1]==n:break
for fib in fibs[::-1]:print(fib)

