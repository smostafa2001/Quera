n,k=map(int,input().split())
answers=[]
i=1
while len(answers)!=n:
    answers.append(i%n if i%n!=0 else n)
    i+=(n-k)
if answers[1]-answers[0] < k:print('Impossible')
else:
    for answer in answers:print(answer,end=' ')