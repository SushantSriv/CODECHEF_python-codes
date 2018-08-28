for i in range(int(input())):
    int(input())
    a=list(map(int,input().split(" ")))
    sum=0
    for j in range(len(a)):
        sum=sum|a[j]
    print(sum)    
