for i in range(int(input())):
    x=input()
    y=input()
    z=list()
    for j in range(len(x)):
        if(x[j]=='W' and y[j]=='W'):
            z.append('B')
        elif(x[j]=='B' and y[j]=='B'):
            z.append('W')
        elif(x[j]=='W' and y[j]=='B'):
            z.append('B')
        elif(x[j]=='B' and y[j]=='W'):
            z.append('W')
    a=''
    for j in z:
        a+=j
    print(a)    
