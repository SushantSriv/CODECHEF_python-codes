for test in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c2=0
    c=0
    for i in range(n):
        if a[i]==2:
            c2+=1
        elif a[i]>2:
            c+=1
    print(int(c2*c+c*(c-1)/2))
