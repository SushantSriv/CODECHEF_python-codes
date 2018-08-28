for i in range(int(input())):
    c,d,l=map(int,input().split(" "))
    maxl=c*4+d*4
    minl=d*4
    if l in range(minl,maxl+1) and l%4==0:
        print("yes")
    else:
        print("no")
    
