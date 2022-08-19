times=[int(input())for i in range(1,int(input())+1)]
change_mode=0
new_mode=times[0]
for time in times:
    if new_mode!=time:
        change_mode+=1
        new_mode=time
print(change_mode)