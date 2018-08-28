import itertools
n,m,k=list(map(int,input().split()))
a=list(map(int,input().split()))
p=list(map(int,input().split()))
c=[]
for i in range(1,k+1):
    c.append(i)
e=[] 
res=[seq for i in range(len(c),0,-1) for seq in itertools.permutations(c,i) if len(seq)==n]
for i in range(len(res)):
    sum1=res[i][0]+a[0]
    for j in range(1,len(res[i])):
        sum1=sum1*(res[i][j]+a[j])
    d=[]    
    for j in range(m):
        d.append(sum1%p[j])
    e.append(sum(d))
ans=res[e.index(max(e))]
for i in range(n):
    print(a[i]+ans[i],end=" ")       
        
    
