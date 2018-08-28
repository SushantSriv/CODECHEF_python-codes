for i in range(int(input())):
    n=int(input())
    sum=0
    for j in range(n):
        price,quantity,discount=list(map(float,input().split(" ")))
        newprice=price+(price*discount)/100
        finalprice=newprice-(newprice*discount)/100
        loss=price-finalprice
        sum+=(loss*quantity)
    print(sum)    
        
