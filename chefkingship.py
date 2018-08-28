for test in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    p.sort()
    sum1=0
    for i in range(1,n):
        sum1+=p[0]*p[i]
    print(sum1)    
    
