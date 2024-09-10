import math
def checkPrime(num):
    count=0
    for i in range(1,int(math.sqrt(num))+1):
        if(num%i==0):
            count +=1
            if(num% (num//i)==0):
                count +=1
    if(count==2):
        print("Prime Number")
    else:
        print("Not A Prime Number")
        
number= int(input("Enter A number To Check Prime Or Not : "))
checkPrime(number)