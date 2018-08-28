import random
a,b=list(map(int,input().split(" ")))
res=a-b
res=list(res)
ran=str(random.randint(1,9))
print(ran)
for i in range(len(res)):
    if(res[i]!=0):
        if(res[i]!=ran):
            res[i]='ran'
            print(res)
            break
        else:
            ran=random.randint(1,9)
            res.replace(res[i],'ran')
            print(res)
            break
