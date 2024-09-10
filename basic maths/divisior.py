def checkDivisior(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
number=int(input("Enter A Number : "))   
checkDivisior(number)
import math
def checkDivisior2(num):
    divisors=[]
    for i in range(1,int(math.sqrt(num))+1):
        if(num%i==0):
            divisors.append(i)
            if(i!= num//i):
                divisors.append(num//i)
    divisors=sorted(divisors)
    for value in divisors:
        print(value)
number=int(input("Enter A Number : "))   
checkDivisior2(number)