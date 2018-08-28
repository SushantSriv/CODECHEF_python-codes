import math
for i in range(int(input())):
    l,b=map(int,input().split(" "))
    n1=int(abs(math.sqrt(l)))
    n2=int((-1+math.sqrt(1+4*b))/2)
    n11=n1-1
    if(n11==n2):
        print("Limak")
    elif(n11>n2):
        print("Limak")
    else:
        print("Bob")
