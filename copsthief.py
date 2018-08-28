a=[]
for i in range(int(input())):
    m,x,y=list(map(int,input().split(" ")))
    d=x*y
    count=0
    flag=1
    a=list(map(int,input().split(' ')))
    a.sort()
    if(d<a[0]):
       count+=(a[0]-d-1)
    if(d+a[m-1]<100):
       count+=100-a[m-1]-d
    for j in range(0,m-1,1):
        if((a[j+1]-a[j])>2*d):
           count+=a[j+1]-a[j]-2*d-1
    print(count)         
    
    
    
