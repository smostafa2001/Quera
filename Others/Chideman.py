n=int(input())
columns=[]
for i in range(n):columns.append(int(input()))
avg=sum(columns)//n
la=[]
for col in columns:
	if col>avg:
		la.append(col-avg)
print(sum(la))