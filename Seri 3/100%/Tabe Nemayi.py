x,n=int(input()),int(input())
def factorial(number):
	if number==0:return 1
	fact=1
	for i in range(1,number+1):fact*=i
	return fact
soorat=0
makhraj=0
answers=[]
while len(answers)!=n:
	answers.append((x**soorat)/(factorial(makhraj)))
	soorat+=1
	makhraj+=1
print(f'{sum(answers):.3f}')