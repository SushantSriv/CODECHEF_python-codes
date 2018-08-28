n=int(input())
c=list(map(int,input().split(" ")))
total=sum(c)
for i in range(1,len(c)+1,1):
    total=total-i
if(total==0):
    print("YES")
else:
    print("NO")
    
