for test in range(int(input())):
    n,x=list(map(int,input().split(" ")))
    s=list(map(int,input().split(" ")))
    a=s[:]
    a.sort(reverse=True)
    sum1=0
    sum2=0
    b=[]
    for i in range(x):
        sum1+=a[i]*(s.index(a[i])+1)
        sum2+=s.index(a[i])+1
    print(sum1/sum2)
