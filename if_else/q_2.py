# q2>>Write a program that takes two numbers and an operator (+, -, *, /) as input and prints the result of the operation.

num1=float(input("Enter First Number: "))
num2=float(input("Enter Second Number: "))
opr= int(input("Choose The Operation You Want To Perform \n1.)For (+) Enter 1\n2.)For (-) Enter 2\n3.)For (*) Enter 3\n4.)For (/) Enter 4\n>> "))

if(opr==1):
    print(f"Sum of {num1} & {num2} is: {num1+num2}")
elif(opr==2):
    print(f"Subtraction of {num1} & {num2} is: {num1-num2}")
elif(opr==3):
    print(f"Multipication of {num1} & {num2} is: {num1*num2}")
elif(opr==4):
    if(num2 !=0):
        print(f"Division of {num1} & {num2} is: {num1/num2}")
    else:
        print("Not divisable by zero")
else:
    ("Enter a Valid Input")
