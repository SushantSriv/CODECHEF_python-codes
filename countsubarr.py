for i in range(int(input())):
    int(input())
    a=list(map(int,input().split(" ")))
    count=0
    for j in range(len(a)):
        for k in range(len(a)):
            if(a[i]<=a[k]):
                count+=1
    print(count)
            
    
