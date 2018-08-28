s=list(map(str,input().split(" ")))
sum2=''
for i in range(1,len(s)):
    sum2+=s[i]
    sum2+=" "
sum1=''
a=[]
b=[]
for i in range(1,len(s)):
    if(s[i][0]==s[i][0].upper()):
        sum1+=s[i][0].upper()
        a.append('1')
    else:
        a.append('0')        
if(len(sum1)!=len(s[0])):
    for i in range(len(s[0])-len(sum1)):
        sum1+='_'
for i in range(len(s[0])):
    if(s[0][i]==sum1[i]):
        b.append('1')
    else:
        b.append('0')
flag=0
if(len(a)==len(b)):
    for i in range(len(a)):
        if(a[i]==b[i]):
            flag=1
        else:
            flag=0
            break
    if(flag):
        print(str(s[0])+" is a COMPLETE SIMPLE acronym for "+sum2)
    else:
        print(str(s[0])+" is a PARTIAL SIMPLE acronym for "+sum2)
else:
     flagc=0
     for i in range(len(b),len(a),1):
        if a[i]=='1':
            flagc=1
            break
     flagp=0        
     for i in range(len(b)):
        if(a[i]==b[i]):
            flagp=0
        else:
            flagp=1
            break
     if(flagc and flagp):
        print(str(s[0])+" is a PARTIAL COMPLEX acronym for "+sum2)
     else:
        print(s[0]+" is a not an acronym for "+sum2)
                
            
                
         
    
            
    
    
