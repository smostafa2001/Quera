r,c=map(int,input().split())
rdic={1:10 , 2:9 , 3:8, 4:7, 5:6 , 6:5 , 7:4 ,8:3 , 9:2, 10:1}
cdic1={}
myc=c
for i in range(1,11):
    cdic1[i]='Right'
for i in range(11,21):
    cdic1[i]='Left'
cdic2={1:20 , 2:19 , 3:18, 4:17, 5:16 , 6:15 , 7:14 ,8:13 , 9:12, 10:11,11:10,12:9,13:8,14:7,15:6,16:5,17:4,18:3,19:2,20:1}
if cdic1[c]=='Right':
    myc=myc
else:
    myc=cdic2[c]
print(cdic1[c],rdic[r],myc)    