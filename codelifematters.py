for i in range(int(input())):
    s=list(map(int,input().split(" ")))
    flag=0
    count1=0
    for j in range(len(s)-1):
        if(s[j]==1):
            if(s[j+1]==1):
                count1+=1
            else:
                count1=0
            if(count1==5):
                 flag=1
            else:
                continue
    if(flag):
        print("#coderlifematters")
    else:
        print("#allcodersarefun")
        
