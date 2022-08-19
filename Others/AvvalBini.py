def isPrime(number):
    for j in range(2, number):
        if number % j == 0:
            return False
    return True
a, b = int(input()), int(input())
result = []
for number in range(a + 1, b):
    if isPrime(number):
        result.append(f"{number}")
print(",".join(result))