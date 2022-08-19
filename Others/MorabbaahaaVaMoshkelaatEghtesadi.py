n, k = [int(i) for i in input().split()]
string = [int(i) for i in input().split()]
print(n - (- (-sum(string) // k)))