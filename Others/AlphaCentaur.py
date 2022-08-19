n, b = map(int, input().split())


def numberToBase(number, base):
    convertedNumber = ""

    strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number == 0: return 0
    while number != 0:
        convertedNumber += strings[number % base]
        number //= b
    convertedNumber = convertedNumber[::-1]
    return convertedNumber


print(numberToBase(n, b))
