a=[]
b=[]
for test in range(int(input())):
    r,w=list(map(int,input().split()))
    a.append(r)
    b.append(w)
a1=a[:]
b1=b[:]
a1.sort()
b1.sort()
flag=0
if 10 in a:
    flag=1
if a1==a and b1==b and flag==0:
    print('YES')
elif a1==a and b1==b and flag==1:
    if a.index(10)==len(a)-1:
        print("YES")
else:
    print('NO')
