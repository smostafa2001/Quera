n, k = [int(i) for i in input().split()]

sum = 0
for i in range(n):
    sum += int(input())

print("YES" if sum >= k else "NO")