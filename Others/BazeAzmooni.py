s, f, l, x = map(int, input().split())
if x == s:
    print(l)

elif (s < x) and (x < f):
    if f - x < l:
        print(f - x)
    else:
        print(l)
elif x < s:
    print("exam did not started!")
elif x >= f:
    print("exam finished!")
