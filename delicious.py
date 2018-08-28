import math
n,q=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in range(q):
    x,l,r=list(map(int,input().split()))
    ans=0
    for j in range(l-1,r,1):
        ans+=math.ceil(x/a[j])
    print(ans)    
