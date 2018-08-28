import math
for test in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    g=0
    for i in range(len(a)):
        g=math.gcd(a[i],g)
    flag=0    
    for i in range(2,int(g**0.5)):
        if g%i==0:
            flag=1
            print(i)
    if flag==0:
        if g==1:
            print(-1)
        else:
            print(g)
