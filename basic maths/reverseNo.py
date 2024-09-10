def cnt(num):
    reversedNumber=0
    while(num>0):
        lastDigit=num%10
        reversedNumber=reversedNumber*10+lastDigit
        num=num//10  
    print(reversedNumber)
cnt(45621)