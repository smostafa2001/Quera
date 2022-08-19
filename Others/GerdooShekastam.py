l, w, h = map(int, input().split())
flag=False
for i in range(0, (l // h) + 1):
    if (l - (i * h)) % w == 0:
        print((l - (i * h)) // w, i)
        flag=True
if not flag:print(-1)