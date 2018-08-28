for i in range(int(input())):
    c=int(input())
    a=[]
    b=[]
    for j in range(1,int(c**0.5+1),1):
        if(c%j==0):
            a.append([j,c//j])
    for j in range(len(a)):
        b.append(abs(a[j][1]-a[j][0]))
    print(min(b))    
