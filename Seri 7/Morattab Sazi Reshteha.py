s=input().split()
if '0' in s:
    s=s
    s.remove('0')
la=[]
lb=[]
lc=[]
ld=[]
le=[]
lf=[]
lg = []
lh=[]
li = []
lj=[]
lk=[]
ll=[]
lm=[]
ln=[]
lo=[]
lp=[]
lq=[]
lr=[]
ls=[]
lt=[]
lu=[]
lv=[]
lw=[]
lx=[]
ly=[]
lz = []
for item in s:
    if item.startswith('A'):
            la.append(item)
    elif item.startswith('a'):
        la.append(item)
    elif item.startswith('B'):
        lb.append(item)
    elif item.startswith('b'):
        lb.append(item)
    elif item.startswith('C'):
        lc.append(item)
    elif item.startswith('c'):
        lc.append(item)
    elif item.startswith('D'):
        ld.append(item)
    elif item.startswith('d'):
        ld.append(item)
    elif item.startswith('E'):
        le.append(item)
    elif item.startswith('e'):
        le.append(item)
    elif item.startswith('F'):
        lf.append(item)
    elif item.startswith('f'):
        lf.append(item)
    elif item.startswith('G'):
        lg.append(item)
    elif item.startswith('g'):
        lg.append(item)
    elif item.startswith('H'):
        lh.append(item)
    elif item.startswith('h'):
         lh.append(item)
    elif item.startswith('I'):
        li.append(item)
    elif item.startswith('i'):
        li.append(item)
    elif item.startswith('J'):
        lj.append(item)
    elif item.startswith('j'):
        lj.append(item)
    elif item.startswith('K'):
        lk.append(item)
    elif item.startswith('k'):
        lk.append(item)
    elif item.startswith('L'):
        ll.append(item)
    elif item.startswith('l'):
        ll.append(item)
    elif item.startswith('M'):
        lm.append(item)
    elif item.startswith('m'):
        lm.append(item)
    elif item.startswith('N'):
        ln.append(item)
    elif item.startswith('n'):
        ln.append(item)
    elif item.startswith('O'):
        lo.append(item)
    elif item.startswith('o'):
        lo.append(item)
    elif item.startswith('P'):
        lp.append(item)
    elif item.startswith('p'):
        lp.append(item)
    elif item.startswith('Q'):
        lq.append(item)
    elif item.startswith('q'):
        lq.append(item)
    elif item.startswith('R'):
        lr.append(item)
    elif item.startswith('r'):
        lr.append(item)
    elif item.startswith('S'):
        ls.append(item)
    elif item.startswith('s'):
        ls.append(item)
    elif item.startswith('T'):
        lt.append(item)
    elif item.startswith('t'):
        lt.append(item)
    elif item.startswith('U'):
        lu.append(item)
    elif item.startswith('u'):
        lu.append(item)
    elif item.startswith('V'):
        lv.append(item)
    elif item.startswith('v'):
        lv.append(item)
    elif item.startswith('W'):
        lw.append(item)
    elif item.startswith('w'):
        lw.append(item)
    elif item.startswith('X'):
        lx.append(item)
    elif item.startswith('x'):
        lx.append(item)
    elif item.startswith('Y'):
        ly.append(item)
    elif item.startswith('y'):
        ly.append(item)
    elif item.startswith('Z'):
        lz.append(item)
    elif item.startswith('z'):
        lz.append(item)
la.sort()
lb.sort()
lc.sort()
ld.sort()
le.sort()
lf.sort()
lg.sort()
lh.sort()
li.sort()
lj.sort()
lk.sort()
lm.sort()
ln.sort()
lo.sort()
lp.sort()
lq.sort()
lr.sort()
ls.sort()
lt.sort()
lu.sort()
lv.sort()
lw.sort()
lx.sort()
ly.sort()
lz.sort()
totall=[]

totall.append(la)
totall.append(lb)
totall.append(lc)
totall.append(ld)
totall.append(le)
totall.append(lf)
totall.append(lg)
totall.append(lh)
totall.append(li)
totall.append(lj)
totall.append(lk)
totall.append(ll)
totall.append(lm)
totall.append(ln)
totall.append(lo)
totall.append(lp)
totall.append(lq)
totall.append(lr)
totall.append(ls)
totall.append(lt)
totall.append(lu)
totall.append(lv)
totall.append(lw)
totall.append(lx)
totall.append(ly)
totall.append(lz)
totall=str(totall)
totall=totall.replace('[','')
totall=totall.replace(']','')
totall = totall.replace(',', '')
totall=totall.replace("'",'')
totall1=totall.split()
totall1=str(totall1)
totall1=totall1.replace('[','')
totall1=totall1.replace(']','')
totall1 = totall1.replace(',', '')
totall1=totall1.replace("'",'')
totall1=totall1.strip()
print(totall1)