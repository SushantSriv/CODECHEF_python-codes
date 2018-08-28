from itertools import groupby
for i in range(int(input())):
    a=[]
    n=int(input())
    d=list(map(int,input().split(" ")))
    d.sort()
    n=len(d)
    a=[len(list(group)) for key,group in groupby(d)]
    for j in range(len(a)):
        n=n-a[j]+1
    print(n)    
            
            
               
    
