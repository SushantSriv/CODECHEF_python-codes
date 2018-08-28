for test in range(int(input())):
    s=list(map(int,input().split(" ")))
    s.sort(reverse=True)
    if s[0]%s[1]==0:
        print(2*s[1])
    else:
        print((s[0]%s[1])*2)
        
        
