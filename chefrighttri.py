import math
a=[]

for i in range(int(input())):
    s=list(map(int,input().split(" ")))
    a.append(s)
count=0
for i in range(5):
    b=[]
    s1=(math.sqrt((a[i][0]-a[i][2])**2+(a[i][1]-a[i][3])**2))
    s2=(math.sqrt((a[i][0]-a[i][4])**2+(a[i][1]-a[i][5])**2))
    s3=(math.sqrt((a[i][2]-a[i][4])**2+(a[i][3]-a[i][5])**2))
    b.append([s1,s2,s3])
    b[0].sort(reverse=True)
    x=round(b[0][0]**2,2)
    y=round(b[0][1]**2,2)
    z=round(b[0][2]**2,2)
    if(x==y+z):
        count+=1
print(count)        
          
