a, b, l = map(int, input().split())
s = 0
for i in range(1, l+1):
    if i % 2 != 0:
        s += a
    else:
        s += b
print(s)