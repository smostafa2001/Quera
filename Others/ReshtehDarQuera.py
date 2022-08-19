memo = {}


def s(number):
    if number == 1:
        return str(1)
    if number not in memo:
        memo[number] = s(number - 1) + str(number) + s(number - 1)
    return memo[number]


n = int(input())
sumOfNumbers = 0
for i in s(n):
    sumOfNumbers += int(i)

print(sumOfNumbers % 1000000007)
