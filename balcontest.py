for i in range(int(input())):
    n,p=list(map(int,input().split(" ")))
    s=input().split(" ")
    countc=0
    countd=0
    for j in range(len(s)):
        if(int(s[j])>=(p/2)):
            countc+=1
        if(int(s[j])<=(p/10)):
            countd+=1
    if(countc==1 and countd==2):
        print("yes")
    else:
        print("no")
    
    
