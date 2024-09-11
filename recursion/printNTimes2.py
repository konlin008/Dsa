def printnof(n,count=1):
    if(count>n):
        return
    else:
        print(count)
        count=count+1
        printnof(n,count)
        
printnof(5)