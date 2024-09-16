def StringPalindromeChecker(i,s):
    if(i>(len(s)-1)/2):return True
    if(s[i] !=s[len(s)-i-1]):return False
    else:
        StringPalindromeChecker(i+1,s)
    
    
output=StringPalindromeChecker(0,"MADAM")
print(output)