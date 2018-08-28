for test in range(int(input())):
    n,c,q=list(map(int,input().split(" ")))
    l=[]
    b=[0]*n
    b[c-1]=1
    for i in range(q):
        l,r=list(map(int,input().split(" ")))
        if c>=l and c<=r:
            c=r-(c-l)
    print(c)        
        
