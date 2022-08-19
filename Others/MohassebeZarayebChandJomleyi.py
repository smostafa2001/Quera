m, n = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
dic = {}
dic_c = {}
for i in range(1, m + 2):
    dic[i] = t[-i]
    dic_c[i] = t[-i]
result = {}
for i in range(n - 1):
    for key1 in dic_c.keys():
        for key2 in dic.keys():
            x = dic[key2] * dic_c[key1]
            d = {key2 + key1: x}
            if key2 + key1 in result:
                result[key2 + key1] += x
                continue
            result.update(d)
    dic_c = result
    result = {}
finals = []
for final in dic_c.values(): finals.append(final)
for i in finals[::-1]: print(i, end=' ')
