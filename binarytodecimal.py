for i in range(int(input())):
    n=list(map(int,input()))
    l=len(n)
    d=0
    for i in range(len(n)):
        d+=n[i]*(2**(l-i-1))
    print(d)    
    
