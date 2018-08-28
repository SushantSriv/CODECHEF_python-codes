import itertools
def countArray(n,k,x):
    a=[]
    for j in range(1,k+1,1):
        a.append(j)
    a=list(a)    
    res=[seq for i in range(len(a),0,-1) for seq in itertools.combinations(a,i)]
    count=0
    for j in range(len(res)):
        if(len(res[j])==n-2):
            count+=1
    print(count)

n,k,x=list(map(int,input().split(" ")))
countArray(n,k,x)


    
    
    
    
