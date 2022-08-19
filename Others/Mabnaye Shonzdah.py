n=int(input(),16)+1
def numberToBase(n, b):
    strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:return 0
    numbers = ""
    while n:
        numbers += strings[n % b]
        n //= b
    numbers = numbers[::-1]
    return "".join(numbers)
print(numberToBase(n,16))