for i in range(int(input())):
    n,x=list(map(int,input().split(" ")))
    s=list(map(int,input().split(" ")))
    s.sort()
    flag=0
    if(sum(s)>x and len(s)==1):
        flag=1
        print("1")
    elif(sum(s)%x==0):
            flag=1
            print(sum(s)//x)
    else:
        for j in range(len(s)):
            if((sum(s)-s[j])%x==0):
                print((sum(s)-s[j])//x)
                flag=1
            else:
                continue
    if(flag==0):
        print("-1")
  

        
    
    
