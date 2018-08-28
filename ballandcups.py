for test in range(int(input())):
    n,c,q=list(map(int,input().split(" ")))
    l=[]
    b=[]
    for i in range(q):
        l1,r1=list(map(int,input().split(" ")))
        l.append([l1,r1])
    for i in range(n):
        b.append('0')
    b[c-1]='1'
    for i in range(len(l)):
            L=l[i][0]-1
            R=l[i][1]-1
            for j in range(int(round(((l[i][1]-l[i][0])/2),0))):
               b[L],b[R]=b[R],b[L]
               L+=1
               R-=1
    print(b.index('1')+1)    
        
        
