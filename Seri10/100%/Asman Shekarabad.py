n,m=map(int,input().split())
window=[]
for i in range(n):
    window.extend(input())
print(window.count('*'))