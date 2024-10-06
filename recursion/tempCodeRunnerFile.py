import re
def ispel(i,s):
    s = re.sub(r'[^\w\s]', '', s.lower().replace(" ", ""))
    print(s)
    if(i>(len(s)-1)//2): return True
    elif(s[i]!=s[len(s)-i-1]):return False
    else:
        return ispel(i+1,s)
ans=ispel(0,"madam aman : dh")
print(ans)