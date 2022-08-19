from string import punctuation as pc
s=input()
s=s.lower()
for p in pc:s=s.replace(p,'')
s=s.replace(' ','')
if s==s[::-1]:print('YES')
else:print('NO')   
