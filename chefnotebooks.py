for test in range(eval(input())):
    x,y,n,k=map(int,input().split())
    flag=0
    for i in range(n):
        p,c=map(int,input().split())
        if (x-y)<=p and c<=k:
            flag=1
    if(flag):
        print("LuckyChef")
    else:
        print("UnluckyChef")
    test+=1    
            
            
    
