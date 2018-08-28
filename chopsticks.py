n,d=list(map(int,input().split(" ")))
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
i=0
count=0
while i<(n-1):
    if a[i+1]-a[i]<=d:
        i+=1
        count+=1
    i+=1    
print(count)        
