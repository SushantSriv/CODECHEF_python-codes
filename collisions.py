for i in range(int(input())):
    b,g=map(int,input().split(" "))
    r=[]
    c=[]
    count1=0
    for j in range(b):
        r.append(input())    
    for j in range(b):
        for k in range(g):
            c.append(r[j][k])
    for j in range(0,len(c),3):
        if(c[j]==1):
            count1+=1
    print(count1)        
       
