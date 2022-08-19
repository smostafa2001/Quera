n=int(input())
nums1=[]
for i in range(1,n+1):
    nums1.append(i)
def divisor(n):
    maghsooms=[]
    for i in range(1, n+1):
        if n % i == 0:
            maghsooms.append(i)
    return maghsooms
nums2=[]
for i in nums1:
    nums2.extend(divisor(i))
print(len(nums2),sum(nums2))