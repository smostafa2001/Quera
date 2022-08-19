names=[input() for i in range(int(input()))]
pureNames=[]
for name in names:
    pureName=str()
    for char in name:
        if char not in pureName:pureName+=char
    pureNames.append(pureName)
lengthOfPureNames=[len(pureName) for pureName in pureNames]
print(max(lengthOfPureNames))