n = int(input())
matris1 = [input().split() for i in range(n)]
matris2 = [input().split() for j in range(n)]
matris1 = [[int(j) for j in i] for i in matris1]
matris2 = [[int(j) for j in i] for i in matris2]
hasel = [[0 for x in range(n)] for y in range(n)]
for i in range(len(matris1)):
    for j in range(len(matris2[0])):
        for k in range(len(matris2)): hasel[i][j] += matris1[i][k] * matris2[k][j]

def determinant(a, total=0):
    if len(a) == 2 and len(a[0]) == 2:
        det = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return det
    for indice in range(len(a)):
        b = a[1:]
        for i in range(len(b)): b[i] = b[i][0:indice] + b[i][indice + 1:]
        sign = (-1) ** (indice % 2)
        total += sign * a[0][indice] * determinant(b)
    return total


print('Danial' if determinant(hasel) % 2 != 0 else 'Farzad')
