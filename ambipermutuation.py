while(1):
    n=int(input())
    if n==0:
        break
    a=[int(e) for e in input().split(" ")]
    num=a[:]
    for j in range(len(a)):
        num[a[j]-1]=j+1
    if(num==a):
        print("ambigous")
    else:
        print("ambigous")
    
