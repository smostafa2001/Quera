# a,b=map(int,input().split())
# ra=str((12-a)%12).zfill(2)
# rb=str((60-b)%60).zfill(2)
# print(ra+':'+rb)
a,b=input().split()
a,b=int(a),int(b)
ra=(12-a)%12
rb=(60-b)%60
print(f'{ra:02d}:{rb:02d}')