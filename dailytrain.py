import math
x,n=list(map(int,input().split()))
a=[]
b=[]
count=0
for i in range(n):
    s=list(map(int,input()))
    a=s[0:36]
    b=s[36:54]
    c=list(reversed(b))
    for j in range(0,9,1):
        if a[4*j:4*(j+1)].count(0)+c[2*j:2*(j+1)].count(0)>=x:
            count+=math.factorial(a[4*j:4*(j+1)].count(0)+c[2*j:2*(j+1)].count(0))/math.factorial(a[4*j:4*(j+1)].count(0)+c[2*j:2*(j+1)].count(0)-x)/math.factorial(x)
print(int(count))
