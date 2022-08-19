X=int(input())
N=int(input())
if N==0:
    print(20)
elif N==7:
    print(X)
elif 0<N<7 or 7<N:
    if X-N>=0:
        print(X-N)
    else:
        print(0)

    