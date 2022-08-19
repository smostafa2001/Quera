v=int(input())
divs=[]
masahatha=[]
def hajm(n):
    for i in range(1,v+1):
        if v%i==0:
            divs.append(i)
    for a in divs:
        for b in divs:
            for c in divs:
                if a*b*c==v:
                    s=(2*a*b)+(2*a*c)+(2*b*c)
                    masahatha.append(s)
hajm(v)
print(min(masahatha))