for i in range(int(input())):
    a,b=list(map(str,input().split(" ")))
    a1=len(a)
    b1=len(b)
    d=min(len(a),len(b))
    c=[]
    for j in range(d):
        r=int(a[a1-1])+int(b[b1-1])
        a1=a1-1
        b1=b1-1
        if(d>1 and len(str(r))==2):
            r=r%10
            c.append(r)
        elif(d>1 and len(str(r))==1):
            c.append(r)
        else:
            c.append(r)
    if(d>1):
        c.append(int(a[0])+int(b[0]))
    sum=c[0]
    sum1=c[len(c)-1]
    if(len(c)==1):
        print(r)
    else:
        for j in range(len(c)-3,0,-1):
            sum+=(10**j)*c[j]  
        print(str(sum1)+str(sum))
