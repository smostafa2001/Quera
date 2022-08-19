n = int(input())


def isPrime(number: int) -> bool:
    counter = 0
    for i in range(n, 1, -1):
        if counter >= 2: return False
        if number % i == 0:
            counter += 1
    return True


if n == 1:
    print("fard")
elif isPrime(n) and n % 2 != 0:
    print("zoj")
else:
    print("fard")
