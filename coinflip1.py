for i in range(int(input())):
    for j in range(int(input())):
        i,a,q=list(map(int,input().split(" ")))
        x=0
        y=a
        if(a%2==1):
                x+=1
                y-=1
                a=a-1
                return
        if(q==1):
                   print(x)
        else:
                   print(y)
