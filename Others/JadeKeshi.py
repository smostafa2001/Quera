n=int(input())
print(int((n/2)+1)**2 if n%2==0 else ((n//2)+1)**2+((n//2)+1))