for i in range(int(input())):
    s=input().upper()
    count=0
    count1=0
    for j in range(0,len(s)-2,1):
        if(s[j]=="U"):
            if(s[j+1]=="U"):
                continue
            else:
                count+=1
        if(s[j]=="D"):
            if(s[j+1]=="D"):
                continue
            else:
                count1+=1
    print(min(count,count1))              
