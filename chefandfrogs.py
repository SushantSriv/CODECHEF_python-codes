n,k,p=list(map(int,input().split()))
a=list(map(int,input().split()))
b=a[:]
b.sort()
for i in range(p):
    flag=0
    m,n=list(map(int,input().split()))
    for i in range(min(m,n)-1,max(m,n)-1,1):
        if b[i+1]-b[i]<=k:
            flag=1
            continue
        else:
            flag=0
            print("No")
            break
    if(flag):
        print("Yes")
