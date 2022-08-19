a,b,c=float(input()),float(input()),float(input())
from math import sqrt as sq
def taghrib(n):return f"{int(n*1000)/1000:.3f}"
delta=(b**2)-(4*a*c)
if a==0:
    if b!=0:print(taghrib((-c)/b))
    else:print('IMPOSSIBLE')
elif delta<0:print('IMPOSSIBLE')
elif delta==0:
    print(taghrib((-b)/(2*a)))
elif delta>0:
    answer1=((-b)+sq(delta))/(2*a)
    answer2=((-b)-sq(delta))/(2*a)
    answers=[answer1,answer2]
    print(taghrib(min(answers)),taghrib(max(answers)),sep='\n')
