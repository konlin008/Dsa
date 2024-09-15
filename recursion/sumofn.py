def sumofN(i,sum=0):
    if(i<1):
        print(sum)
        return
    else:
        sum +=i
        sumofN(i-1,sum)
sumofN(5)