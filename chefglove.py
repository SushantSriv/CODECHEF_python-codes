for i in range(int(input())):
    int(input())
    fingers=list(map(int,input().split(" ")))
    gloves=list(map(int,input().split(" ")))
    flag=0
    for j in range(len(fingers)):
        if(fingers[j]<=gloves[j]):
            flag=1
        else:
            flag=0
            break
    gloves.reverse()
    flag1=0
    for j in range(len(fingers)):
        if(fingers[j]<=gloves[j]):
            flag1=1
        else:
            flag1=0
            break
    if(flag==1 and flag1==1):
        print("both")
    if(flag==0  and flag1==1):
        print("back")
    if(flag==1 and flag1==0):
        print("front")
    if(flag==0 and flag1==0 ):
        print("none")    
    
