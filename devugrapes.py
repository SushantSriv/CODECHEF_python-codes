for i in range(int(input())):
    x,y=input().split(" ")
    a=list(map(int,input().split(" ")))
    count=0
    for j in range(len(a)):
        b=a[j]//int(y)
        if((a[j]%int(y))<(int(y)*(b+1)-a[j])):
              count+=a[j]%int(y)
        else:
            count+=(int(y)*(b+1)-a[j])
    print(count)    
