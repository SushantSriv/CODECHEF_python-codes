for i in range(int(input())):
    int(input())
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    a.sort()
    b.sort()
    a.pop()
    b.pop()
    if(sum(a)<sum(b)):
        print("Alice")
    elif(sum(a)>sum(b)):
        print("Bob")
    else:
        print("Draw")
