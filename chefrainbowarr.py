for i in range(int(input())):
    int(input())
    a=[]
    a=list(map(int,input().split(" ")))
    d=len(a)//7
    b=[]
    flag=0
    for j in range(d):
        b.append(a[(0+7*j):7*(j+1)])
    for k in range(d):
        for j in range(1,7,1):
            if(k%2==0):
                if(b[k][j]==j):
                    flag=1
                    continue
                else:
                    print("no")
                    break
            if(k%2==1):
                if(b[k][j]==7-j):
                    flag=1
                    continue
                else:
                    print("no")
                    break
    r=len(a)%7
    e=[]
    e=a[(7*d):(7*d+r)]
    if(d%2==0):
         for j in range(1,len(e),1):
             if(e[j]==j):
                 flag=1
                 continue
             else:
                 print("no")
                 break
    else:
         for j in range(1,len(e),1):
             if(e[j]==7-j):
                 flag=1
                 continue
             else:
                 print("no")
                 break
        
                 
        

    
