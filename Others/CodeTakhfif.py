n, t = input().split()
n = int(n)
s = [input() for i in range(n)]
t=list(t)
t.sort()
ct=""
for i in t:
    if i not in ct:ct+=i
s=[list(s) for i in s]
for i in s:i.sort()
cs=[]
for i in s:
    ci=""
    for j in i:
        if j not in ci:ci+=j
    cs.append(ci)
for i in range(len(cs)):
    cnt=0
    for j in range(len(cs[i])-1):
        if cs[i][j]==ct[j]:cnt+=1
    if cnt==len(ct):print("Yes")
    else:print("No")
