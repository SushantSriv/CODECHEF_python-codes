for i in range(int(input())):
    x=input().lower()
    y=input().lower()
    for j in range(len(x)):
        if((x[j]==y[j]) and (x[j]!='?' and y[j]!='?')):
                flag=1
        elif(x[j]=='?' or y[j]=='?'):
                flag=1
        else:
            flag=0
            break
    if(flag==1):
        print('Yes')
    else:
        print('No')
                
