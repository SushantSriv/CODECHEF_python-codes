n=int(input())
t=int(input())
m=int(input())
a=[]
if(t!=0):
    for i in range(m):
      s=list(map(int,input().split(" ")))
      a.append(s)
    count=0
    b=[]
    for i in range(m):
      sum1=a[i][0]
    for j in range(1,len(a[i])):
      sum1+=a[i][j]
      if(sum1==n//2 and j%3==0 and j not in b):
        b.append(j)
        count+=1
    print(count)
else:
    print('0')
