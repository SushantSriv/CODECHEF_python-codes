import itertools
for test in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    res=[seq for i in range(n,0,-1) for seq in itertools.combinations(a,i) if len(seq)==2]
    count=0
    for i in range(len(res)):
        if sum(res[i])/2 in a:
            count+=1
    print(count)        
