for i in range(int(input())):
    n=int(input())
    for j in range(n):
        i,n,q=list(map(int,input().split(" ")))
        a=[]
        if(i==1):
            for k in range(n):
                a.append("H")
        else:
            for k in range(n):
                a.append("T")        
        for k in range(n):
            for m in range(k+1):
                if(a[m]=="H"):
                    a[m]="T"
                else:
                    a[m]="H"
        if(q==1)
        :
            print(a.count("H"))
        else:
            print(a.count("T"))
                
