def cnt(x):
    revNum=0
    maxInt,minInt=2**31-1,-2**31
    if(x<0):sign=-1
    else:sign=1
    x=abs(x)
    while(x>0):
        lastDigit=x%10
        revNum=revNum*10+lastDigit
        x=x//10
    revNum*=sign  
    if(revNum>=maxInt or revNum<=minInt ):
        print(0)
        return 0
    print(revNum)
cnt(-5556545)