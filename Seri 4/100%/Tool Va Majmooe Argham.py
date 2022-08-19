def Largest(m, s):
    if (s == 0):
        if (m == 1):
            return ("0")
        else:
            return ("-1")
    if (s > 9 * m):
        return ("-1")
    array = [0] * m
    for i in range(0, m):
        if (s >= 9):
            array[i] = 9
            s -= 9
        else:
            array[i] = s
            s = 0
    solve = ''
    for i in range(0, m):
        solve += str(array[i])
    return (f"{solve}")


def smallest(m, s):
    if (s == 0):
        if (m == 1):
            return ("0")
        else:
            return ("-1")
    if (s > 9 * m):
        return ("-1")
    marray2 = [0 for i in range(m + 1)]
    s -= 1
    for i in range(m - 1, 0, -1):
        if (s > 9):
            marray2[i] = 9
            s -= 9
        else:
            marray2[i] = s
            s = 0
    marray2[0] = s + 1
    solve = ""
    for i in range(m):
        solve += str(marray2[i])
    return solve
m, s = input().split()
m, s = int(m), int(s)
print(smallest(m, s), Largest(m, s))
