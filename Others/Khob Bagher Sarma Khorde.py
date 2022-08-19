strings=[input() for i in range(5)]
answers=[]
for i in strings:
    if 'MOLANA' in i:answers.append(strings.index(i)+1)
    elif 'HAFEZ' in i:answers.append(strings.index(i)+1)
if not len(answers):print('NOT FOUND!')
else:
    for answer in answers:print(answer,end=' ')
