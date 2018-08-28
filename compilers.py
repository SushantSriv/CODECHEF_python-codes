for test in range(int(input())):
    s=input()
    ans=''
    for i in range(200000):
         if ans in s:
            ans1=ans
            ans='<'+ans+'>'    
         else:
            break
        
    print(len(ans1))    
