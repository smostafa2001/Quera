n = int(input())
numbers = [int(i) for i in input().split()]
print(numbers.index(max(numbers)) + 1)