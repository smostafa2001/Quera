n=int(input())
binos=[i**2 for i in range(30)]
for i in range(n):
    binos.append(2**i)
    if 2**i>=n:break
print(binos[-1])