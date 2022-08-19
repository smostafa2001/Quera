a,b,c=map(int,input().split())
matris1=[input().split() for i in range(a)]
matris2=[input().split() for i in range(b)]
matris1=[[int(j) for j in i]for i in matris1]
matris2=[[int(j)for j in i] for i in matris2]
haselzarb=[[0 for j in range(c)] for i in range(a)]
for i in range(len(matris1)):
    for j in range(len(matris2[0])):
        for k in range(len(matris2)):haselzarb[i][j]+=matris1[i][k]*matris2[k][j]
for satr in haselzarb:
    for sotoon in satr:print(sotoon,end=' ')
    print()
    