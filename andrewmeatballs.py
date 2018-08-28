for test in range(int(input())):
    n,m=list(map(int,input().split()))
    li=list(map(int,input().split()))
    li.sort(reverse=True)
    sum1=0
    count=0
    for i in range(n):
        sum1+=li[i]
        count+=1
        if(sum1>=m):
            print(count)
            break
    if(sum1<m):
        print(-1)
        
