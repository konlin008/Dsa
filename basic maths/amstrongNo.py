def cnt(num):
    sum=0
    dupnum=num
    while(num>0):
        lastDigit=num%10
        sum = sum+(lastDigit*lastDigit*lastDigit)
        num=num//10  
    if(sum==dupnum):
        print("Amstrong Number")
    else:
        print("Not Amstrong Number")
cnt(153)