
import time
s=time.clock()
for test in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(set(a))
    ans=0
    for i in range(len(b)):
        if a.count(b[i])==k:
            ans+=b[i]    
    if(ans==0):
        print(-1)
    else:
        print(ans)
    
    print(time.clock()-s)
