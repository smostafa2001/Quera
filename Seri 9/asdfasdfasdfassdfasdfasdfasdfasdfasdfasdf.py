q = int(input())
dictionary = {}
bank = {}
answer = []
def s():
    for i in range(q):
        a,b = input().split()
        if a == "1":
            ip,username = b.split(":")
            for sings in "_*#$":
                if sings in username:
                    n = "invalid username"
                    answer.append(n)
                    break
            else:
                dictionary[ip] = username
                bank[ip] = 0
        if a == "2":
            ip,username,money = b.split(":")
            if ip in dictionary:
                bank[ip] -= int(money)
                new_dict = dict(map(reversed, dictionary.items()))
                bank[(new_dict[username])] += int(money)
            else:
                n = "invalid username"
                answer.append(n)
                break
        if a == "3":
            answer.append(bank[b])
    for i in range(len(answer)):
        print(answer[i])
s()