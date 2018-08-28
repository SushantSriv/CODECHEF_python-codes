for T in range(int(input())):
 
    X,Y,K,N = map(int,input().split())
 
    p = []
    c = []
    for i in range(N):
        P,C = map(int,input().split())
        p.append(P)
        c.append(C)
 
    req = X-Y
 
    ans = False
    for i in range(N):
        if (p[i]>=req)and(c[i]<=K):
            ans = True
            break
 
    if ans:
        print("LuckyChef")
    else:
        print("UnluckyChef")
 
