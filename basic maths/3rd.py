# palindrome

def  checkTheNumber(x):
    reversedNumbr=0
    dupNumber=x
    while(x>0):
        lastDigit=x%10
        reversedNumbr=reversedNumbr*10+lastDigit
        x=x//10
    if(reversedNumbr==dupNumber):
        
        return True
    else:
        return False
        
number=int(input("Enter A Number : "))        
checkTheNumber(number)