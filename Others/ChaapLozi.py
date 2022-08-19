n=int(input())
for i in range(1,((2*n)+1)+1,2):
    print(('*'*i).center((2*n)+1))
for i in range((2*n)-1,0,-2):
    print(('*'*i).center((2*n)+1))
