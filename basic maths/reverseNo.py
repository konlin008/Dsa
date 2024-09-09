def rv(n):
    min_int,mix_int=-2**31,2**31-1
    if(n<0):
        sign=-1
    else:
        sign=0  
    n= abs(n)
    revrseDigit=0
    while(n>0):
        lastDigit= n%10
        if(revrseDigit>mix_int//10)
        revrseDigit= (revrseDigit * 10)+lastDigit
        n= n//10
    revrseDigit=revrseDigit*sign
    print(revrseDigit)
    
num= int(input("Enter The Number You Want To Reverse"))
rv(num)