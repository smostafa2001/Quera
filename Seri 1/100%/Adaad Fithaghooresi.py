numbers=[int(input())for i in range(3)]
numbers.sort()
if numbers[-1]**2==(numbers[-2]**2)+(numbers[-3]**2):print('YES')
else:print('NO')