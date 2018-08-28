n = 46870
d = 33102
f = "3."
for i in range(1000000):
    x = n//d 
    f += str(x)
    n = (n%d)*10
t = int(input())
for i in range(t):
    k = int(input())
    if k:
        print(f[:k+2])
    else:
        print("3") 
