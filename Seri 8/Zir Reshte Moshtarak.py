n=int(input())
words=[]
for i in range(1,n+1):
    words.append(input())
str_words=''.join(words)
lsw=list(str_words)
commons=[]
for i in lsw:
    if lsw.count(i)==n:
        commons.append(i)
pure_commons=[]
for i in commons:
    if i not in pure_commons:
        pure_commons.append(i)
spc=''.join(pure_commons)
print(spc)

