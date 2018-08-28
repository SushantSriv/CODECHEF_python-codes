a=['mon','tues','wed','thur','fri','sat','sun']
for i in range(int(input())):
    w,s=input().split(" ")    
    b=[4,4,4,4,4,4,4]
    for j in range(int(w)-28):
        b[a.index(s)+j] += 1
    print(' '.join(str(j) for j in b))  
