p, d = [int(i) for i in input().split()]
x = 1
while True:
    if 0 <= (x * d) % p <= p / 2:
        print(x * d)
        break
    x += 1