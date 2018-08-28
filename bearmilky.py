for i in range(int(input())):
    n=int(input())
    a=list(map(str,input().split(" ")))
    flag=0
    for j in range(len(a)-1):
            if((a[j]=="cookie" and a[j+1]=="milk") or (a[j]=="milk" and a[j+1]=="milk") or (a[j]=="milk" and a[j+1]=="cookie")):
                flag=1
                continue
            else:
                flag=0
                break
    if "cookie" not in a:
        flag=1
    if(flag):
        print("YES")
    else:
        print("NO")
