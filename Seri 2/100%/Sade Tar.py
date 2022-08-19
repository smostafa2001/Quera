Numbers=[int(input())for i in range(4)]
p=1
for i in Numbers:p*=i
print('Sum : '+f'{sum(Numbers):f}')
print('Average : '+f'{sum(Numbers)/4:f}')
print('Product : '+f'{p:f}')
print('MAX : '+f'{max(Numbers):f}')
print('MIN : '+f'{min(Numbers):f}')