for i in range(int(input())):
    a=[]
    for j in range(int(input())):
        s=list(map(int,input().split(" ")))
        a.append(s)
        discount1=[]
        discount2=[]
        discount3=[]
    for j in range(len(a)):
        if a[j][1]==1:
            discount1.append([a[j][0],a[j][2]])
        elif a[j][1]==2:
            discount2.append([a[j][0],a[j][2]])
        else:
            discount3.append([a[j][0],a[j][2]])
    c1=d1=c2=d2=c3=d3=0
    for j in range(len(discount1)):
        if d1<discount1[j][1]:
            c1=discount1[j][0]
            d1=discount1[j][1]
        elif d1==discount1[j][1]:
            if(c1>discount1[j][0]):
                c1=discount1[j][0]
    print(d1,c1)

    for j in range(len(discount2)):
        if d2<discount2[j][1]:
            c2=discount2[j][0]
            d2=discount2[j][1]
        elif d2==discount2[j][1]:
            if(c2>discount2[j][0]):
                c2=discount2[j][0]
    print(d2,c2)

    for j in range(len(discount3)):
        if d3<discount3[j][1]:
            c3=discount3[j][0]
            d3=discount3[j][1]
        elif d3==discount3[j][1]:
            if(c3>discount3[j][0]):
                c3=discount3[j][0]
    print(d3,c3)
            
