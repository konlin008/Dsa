def gcdChecker(num1,num2):
    for i in range(1,min(num1,num2)+1):
        if (num1%i==0 and num2%i==0):
            gcd=i
    print(gcd)
print("To Check The GCD of Two Numbers:")            
num1=int(input("Enter The First: "))
num2=int(input("Enter The Second: "))
gcdChecker(num1,num2)