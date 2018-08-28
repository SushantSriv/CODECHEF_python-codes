import itertools
for test in range(int(input())):
    int(input())
    s=list(map(int,input().split(" ")))
    a=[]
    for i in range(len(s)):
        while(s[i]!=0):
            r=s[i]%10
            a.append(r)
            s[i]=s[i]//10
    print(a)        
    res=[seq for i in range(len(a),0,-1) for seq in itertools.combinations(a,i) if sum(seq)%3==0 ]
    print(len(res[0]))
    if(len(res[0])>1 and len(a)>1):
        print("Yes")
    elif(len(res[0])==1 and len(a)==1):
        print("Yes")
    else:
        print("No")
    
            
        
