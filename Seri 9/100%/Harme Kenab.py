ipdic={}
bankdic={}
responds=[]
for i in range(int(input())):
    la,si=input().split()
    if la =='1':
        ip,username=si.split(':')
        for symbol in '#$*_':
            if symbol in username:
                answer='invalid username'
                responds.append(answer)
                break
            else:
                ipdic[ip]=username
                bankdic[username]=0
    if la=='2':
        ip,username,money=si.split(':')
        bankdic[ipdic[ip]]-=int(money)
        bankdic[username]+=int(money)
    if la == '3':responds.append(bankdic[ipdic[si]])
for respond in responds:print(respond) 