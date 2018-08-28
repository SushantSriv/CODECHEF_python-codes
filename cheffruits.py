for i in range(int(input())):
    n,m,k=map(int,input().split(" "))
    print(max(n,m)-min(min(n,m)+k,max(n,m)))
        
    
