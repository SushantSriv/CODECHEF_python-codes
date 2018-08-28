for i in range(int(input())):
    a,b=list(map(int,input().split(" ")))
    if(a%2==1 and a<b):
        if(abs(b-a)==1 or abs(b-a)==2):
            print("YES")
        else:
            print("NO")
    elif(a%2==0):
        if(abs(b-a)==2 or b==a-1):
            print("YES")
        else:
            print("NO")
    elif(a%2==1 and a>b):
        if(abs(a-b)==2):
            print("YES")
        else:
            print("NO")
