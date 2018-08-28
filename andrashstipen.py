for i in range(int(input())):
    int(input())
    a=[]
    a=list(map(int,input().split(" ")))
    avg=(sum(a)/len(a))
    if 2 not in a:
        if 5 in a:
            if(avg>=4):
                print("Yes")
                
            else:
                print("No")
            
            
