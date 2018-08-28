a=[]
for i in range(int(input())):
    count=0
    for j in range(int(input())):
        a.append(input())
    for i in range(len(a)):
        if(int(a[i])%2!=0):
            count+=1
        else:
            continue
    print(count)        
