numbers=[]
while 0 not in numbers:numbers.append(int(input()))
numbers.remove(0)
for number in numbers[::-1]:print(number)