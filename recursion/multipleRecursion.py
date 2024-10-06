def fibonatchiNo(n):
    if(n==0):return n
    elif(n==1):return n
    else:
        last=fibonatchiNo(n-1)
        last2=fibonatchiNo(n-2)
        print(last2,last,end="")
        return last+last2
    

ret=fibonatchiNo(4)
print(ret)