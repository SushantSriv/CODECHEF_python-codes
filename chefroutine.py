for j in range(int(input())):
    s=input().upper()
    flag=0
    for j in range(len(s)-1):
        if(s[j]=="C"):
            if(s[j+1]=="E" or s[j+1]=="S" or s[j+1]=="C"):
                flag=1
                continue
            else:
               flag=0
               break
        if(s[j]=="E"):
            if(s[j+1]=="E" or s[j+1]=="S"):
                flag=1
                continue
            else:
               flag=0
               break
        if(s[j]=="S"):
            if(s[j+1]=="S"):
                flag=1
                continue
            else:
               flag=0
               break    
            
    if(flag): 
        print("yes")
    else:
        print("no")
               
               
    
             
    
    
