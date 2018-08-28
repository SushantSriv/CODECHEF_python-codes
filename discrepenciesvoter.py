n1,n2,n3=list(map(int,input().split(" ")))
a=[]
b=[]
c=[]
for i in range(n1):
    a.append(int(input()))
for i in range(n2):
    b.append(int(input()))
for i in range(n3):
    c.append(int(input()))
d1=(set(a).intersection(set(b)))
d2=(set(a).intersection(set(c)))
d3=(set(b).intersection(set(c)))
d4=(d1.union(d2)).union(d3)
print(len(d4))
d4=list(d4)
d4.sort()
for i in range(len(d4)):
    print(d4[i])
