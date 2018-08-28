for i in range(int(input())):
    a=[]
    for j in range(int(input())):
        s=list(map(int,input().split(" ")))
        a.append(s)
        discount1=[]
        discount2=[]
        discount3=[]
        city1=[]
        city2=[]
        city3=[]
    for j in range(len(a)):
        if a[j][1]==1:
            discount1.append(a[j][2])
            city1.append(a[j][0])
        elif a[j][1]==2:
            discount2.append(a[j][2])
            city2.append(a[j][0])
        else:
            discount3.append(a[j][2])
            city3.append(a[j][0])
    repeatindex=[]
    repeat=[]
    if discount1.count(max(discount1))==1:
        print(max(discount1),city1[discount1.index(max(discount1))])
    else:
        for j in range(len(discount1)):
            if discount1[j]==max(discount1):
                repeatindex.append(j)
        for j in range(len(repeatindex)):
            repeat.append(city1[repeatindex[j]])
        print(max(discount1),min(repeat))
        
    repeatindex=[]
    repeat=[]
    if discount2.count(max(discount1))==1:
        print(max(discount2),city2[discount2.index(max(discount2))])
    else:
        for j in range(len(discount2)):
            if discount2[j]==max(discount2):
                repeatindex.append(j)
        for j in range(len(repeatindex)):
            repeat.append(city2[repeatindex[j]])
        print(max(discount2),min(repeat))
        
    repeatindex=[]
    repeat=[]
    if discount3.count(max(discount3))==1:
        print(max(discount3),city3[discount3.index(max(discount3))])
    else:
        for j in range(len(discount3)):
            if discount3[j]==max(discount3):
                repeatindex.append(j)
        for j in range(len(repeatindex)):
            repeat.append(city3[repeatindex[j]])
        print(max(discount3),min(repeat))        
            
        

            
    
    
