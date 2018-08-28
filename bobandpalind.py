import random
import string
ans=''
for i in range(int(input())):
    ans+=random.choice(string.ascii_lowercase)
print(ans)    
