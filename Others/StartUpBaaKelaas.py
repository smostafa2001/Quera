string = [int(i) for i in input().split()]

keeper = [0, 0, 0, 0]

person = 0
while True:
    if 0 in string:
        break
    string[person % 4] -= 1
    keeper[person % 4] += 1
    string.insert(3, string.pop(0))
    person += 1

print(" ".join([str(i) for i in keeper]))