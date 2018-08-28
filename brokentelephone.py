for test in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    b=[]
    for i in range(n-1):
        if a[i]!=a[i+1]:
            b.append(i)
            b.append(i+1)
    print(len(list(set(b))))
