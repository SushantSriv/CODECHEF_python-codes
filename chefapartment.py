for i in range(int(input())):
    int(input())
    a=list(map(int,input().split(" ")))
    fine=0
    if(a.count(0)!=0 and a.count(1)!=0):
        fine=1100
        for j in range(0,len(a)-1,1):
           if (a[j]==1 and a[j+1]==0):
              fine+=1100 
              continue
           elif(a[j]==1 and a[j+1]==1):
              continue
           else:
              fine+=100
              continue
        print(fine)
    elif(a.count(1)==0):
         print(len(a)*1100)
    else:
         print("0")
         
            
