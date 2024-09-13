def printnof(n,count=1):
    if(count>n):
        return
    else:
        print("Aman")
        count=count+1
        printnof(n,count)
        
printnof(5)

def printN(n,count=1):
    if(count>n):
        return
    else:
        print("Aman")
        count+=1
        printN(n,count)
    
printN(5)