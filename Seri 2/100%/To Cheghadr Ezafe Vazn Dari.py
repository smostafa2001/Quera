n,m=int(input()),float(input())
bmi=n/(m**2)
print(f'{bmi:.2f}')
if bmi<18.5:print('Underweight')
elif 18.5<=bmi<25:print('Normal')
elif 25<=bmi<30:print('Overweight')
else:print('Obese')
    