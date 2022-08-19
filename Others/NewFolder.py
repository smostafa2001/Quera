n = int(input())
names = []
duplicatedFolders = {}
folders=[]
for i in range(n):
    a = input()
    duplicatedFolders[a] = duplicatedFolders.get(a, 0) + 1
    if duplicatedFolders[a] >1:
        folders.append(f"{a} ({duplicatedFolders[a]-1})")
    else:
        folders.append(a)
for i in names:
    if i not in folders:
        folders.append(i)
createdFolders = []
for i in range(n):
    if folders[i] in createdFolders:
        createdFolders.append(f"{folders[i]} ({createdFolders.count(folders[i])})")
    else:
        createdFolders.append(folders[i])
    createdFolders.sort()
    print(f"{createdFolders}".replace("[","").replace("]",""))
