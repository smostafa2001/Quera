a,b=int(input()),int(input())
def drawRect(m, n):
    t = (m-n)//2
    trow = m*'* ' + '\n'
    prow = t*'* ' + n*'  ' + t*'* ' + '\n'
    print(t*trow + n*prow + (t-1)*trow + m*'* ')
if b>=a:print('Wrong order!')
elif (a-b)%2!=0:print('Wrong difference!')
else:drawRect(a,b)