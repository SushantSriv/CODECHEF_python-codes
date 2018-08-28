for i in range(int(input())):
    n,k=map(int,input().split(" "))
    a=[]
    for j in range(n):
        a.append(input().split(" "))    
    sum=0
    m=0
    flag=1
    while(flag!=0):
        if(sum<k):
          sum+=int(a[m][0])
          m+=1
          flag=1
          continue
        else:
          flag=0
          continue
    pay=0    
    pay=(sum-k)*int(a[m-1][1])
    for j in range(m,len(a),1):
        pay+=int(a[j][0])*int(a[j][1])
    print(pay)    
        
