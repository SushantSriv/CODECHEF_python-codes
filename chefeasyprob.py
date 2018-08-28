for test in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    li.sort()
    ans=0
    for i in range(len(li)-1,-1,-2):
        ans+=li[i]
    print(ans)     
        
