t = int(input())
keeper = []

for i in range(t):
    keeper.append([int(i) for i in input().split()])

locs = [(0, 0)]
k = 1

for i in range(1, 15000):
    if i % 2 != 0:
        locs.append((locs[i - 1][0] + 1, locs[i - 1][1] + 1))

    else:
        if k % 2 != 0:
            locs.append((locs[i - 1][0] + 1, locs[i - 1][1] - 1))

        else:
            locs.append((locs[i - 1][0] - 1, locs[i - 1][1] + 1))
        k += 1

for i in keeper:
    if (i[0], i[1]) in locs:
        print(locs.index(((i[0], i[1]))))

    else:
        print(-1)