n=(int(input()))
a=[]
ax,ay=list(map(int,input().split()))
bx,by=list(map(int,input().split()))
for i in range(n):
    x,y=list(map(int,input().split()))
    a.append([x,y])
b=[]
c=[]
d=[]
for i in range(n):
    b.append(abs(ax-a[i][0])+abs(ay-a[i][1]))
print(b)    
for i in range(n):
    c.append(abs(bx-a[i][0])+abs(by-a[i][1]))
print(c)
for i in range(n-1):
    for j in range(i+1,n):
        d.append(abs(a[i][0]-a[j][0])+abs(a[i][1]-a[j][1]))    
print(d)    
      
        
