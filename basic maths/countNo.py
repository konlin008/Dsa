def check(num):
    count=0
    while(num>0):
        lastDigit= num%10
        count= count+1
        num= num//10
    print(count)
    
check(5478)