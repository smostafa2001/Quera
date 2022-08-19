n=int(input())
fn=1
for i in range(1,n+1):
    fn*=i
    fn=int(str(fn).strip('0')[-5:])
print(str(fn)[-1])