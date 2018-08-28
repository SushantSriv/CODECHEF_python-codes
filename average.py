import itertools
for test in range(int(input())):
    n,a=list(map(int,input().split()))
    b=[]
    for i in range(-2*a,2*a):
        b.append(i)
    print(b)
    res=[seq for i in range(len(b),0,-1) for seq in itertools.combinations(b,i) if sum(seq)==2*a and len(seq)==n]
    print(res)
        
