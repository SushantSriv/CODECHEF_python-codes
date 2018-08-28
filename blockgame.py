for i in range(int(input())):
    b=[]
    a=input()
    for j in range(len(a)-1,-1,-1):
        b.append(str(a[j]))
    c=''.join(map(str,b))     
    if(a==c):
        print('wins')
    else:
        print('losses')

