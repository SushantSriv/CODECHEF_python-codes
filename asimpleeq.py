for test in range(int(input())):
    p=list(map(int,input().split()))
    a=[]
    b=[]
    c=[]
    for i in range(p[1]):
        a.append(i)
    for i in range(p[2]):
        b.append(i)
    for i in range(p[3]):
        c.append(i)    
    print(a,b,c) 
        
