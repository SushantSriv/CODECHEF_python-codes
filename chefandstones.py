for test in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in range(n):
        c.append((k//a[i])*b[i])
    print(max(c))    
