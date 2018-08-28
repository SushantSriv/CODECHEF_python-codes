for j in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    count=0
    for i in range(len(l)):
        if l[i]%2==0:
            count+=1
            if(count==k):
                print("YES")
                break
        else:
            count=0
    if(count<k):
        print("NO")
