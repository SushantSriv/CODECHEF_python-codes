for i in range(int(input())):
    n=int(input())
    ms=list(map(int,input().split(" ")))
    count=1
    min1=ms[0]
    for j in range(1,len(ms),1):
        if ms[j]<min1:
            count+=1
            min1=ms[j]
    print(count)    
        
    
