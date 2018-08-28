a=[]
sum=0
sum1=0
j=0
n=int(input())
for i in range(n):
    a.append(int(input()))
    while(int(a[i])!=2**j):
            j+=1
            l=1
            if(int(a[i])>2**j):
                l=0
                break
            else:
                continue
m=0
for i in range(n):
    while(sum>=int(a[i])):
        sum+=2**m
        m+=1
        sum1+=1
if(l==1):
    print("1")
else:
    print(int(sum1)/2)
    
        
