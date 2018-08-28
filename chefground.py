for test in range(int(input())):
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    Max=max(a)
    ans=0
    for i in range(len(a)):
        if a[i]==Max:
            continue
        else:
            ans+=Max-a[i]
    if (m-ans)%n==0:
        print("Yes")
    else:
        print("No")
            
    
