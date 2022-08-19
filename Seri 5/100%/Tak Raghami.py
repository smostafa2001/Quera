n=int(input())
def raddeBeAahaad(number):
    argham=list(str(number))
    argham=[int(i) for i in argham]
    if sum(argham)<10:return sum(argham)
    else:return raddeBeAahaad(sum(argham))
print(raddeBeAahaad(n))