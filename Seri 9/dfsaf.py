n = int(input())
userdic={}
bankdic = {}
answer = []
for i in range(n):
    a,b = input().split()
    if a == '1':
        ip,username = b.split(':')
        for symbol in '_*#$':
            if symbol in username:
                qaqalili = 'invalid username'
                answer.append(qaqalili)
                break
        else:
            userdic[username]=0
            bankdic[ip] = 0
    if a == '2':
        ip,username,money = b.split(':')
        bankdic[ip] -=int(money)
        userdic[username]+=int(money)
    if a == "3":
        answer.append(bankdic[b])
for i in answer:
    print(i)
