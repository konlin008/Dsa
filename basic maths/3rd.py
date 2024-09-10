# palindrome

def  checkTheNumber(num):
    reversedNumbr=0
    dupNumber=num
    while(num>0):
        lastDigit=num%10
        reversedNumbr=reversedNumbr*10+lastDigit
        num=num//10
    if(reversedNumbr==dupNumber):
        print(" Palindrome Number")
    else:
        print("Not A  palindrome")
        
number=int(input("Enter A Number : "))        
checkTheNumber(number)