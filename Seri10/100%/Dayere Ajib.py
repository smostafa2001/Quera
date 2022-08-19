n,k=map(int,input().split())
marhale=0
nafar=0
while True:
    marhale+=1
    nafar+=k
    nafar%=n
    if nafar==0:
        break
print(marhale)