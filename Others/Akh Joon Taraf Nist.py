all_days=['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jome']
n1=int(input())
d1=input().split()
n2=int(input())
d2=input().split()
n3=int(input())
d3=input().split()
busy_days=[]
busy_days.extend(d1)
busy_days.extend(d2)
busy_days.extend(d3)
free_days=[i for i in all_days if i not in busy_days]
print(len(free_days))