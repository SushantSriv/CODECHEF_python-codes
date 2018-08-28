(x,y)=input().split()
x=float(x)
y=float(y)
if x+0.5<=y and x%5==0:
    print(y-x-0.5)
else:
    print('%.2f'%y)    
