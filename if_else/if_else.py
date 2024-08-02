# age=int(input("Enter Your Age: "))
# if(age<18):
#     print("You Are Not Aligble To Vote")
# elif(age>=18):
#     print("You Are Aligble To Vote")  
# else:
#     print("Enter A Valid Input")  



# q1>> Check if a Number is Positive, Negative, or Zero

# num=int(input("Plaese Enter A Number: "))
# if(num<0):
#     print("The Number is Negetive")

# elif(num==0):
#     print("The Number is Zero")
# elif(num>0):
#     print("The Number is Positive")

# else:
#     print("Enter A Valid Input")


# q2>>Write a program that takes two numbers and an operator (+, -, *, /) as input and prints the result of the operation.

# num1=float(input("Enter First Number: "))
# num2=float(input("Enter Second Number: "))
# opr= float(input("Choose The Operation You Want To Perform \n1.)For (+) Enter 1\n2.)For (-) Enter 2\n3.)For (*) Enter 3\n4.)For (/) Enter 4\n: "))

# if(opr==1):
#     print(f"Sum of {num1} & {num2} is: {num1+num2}")
# elif(opr==2):
#     print(f"Subtraction of {num1} & {num2} is: {num1-num2}")
# elif(opr==3):
#     print(f"Multipication of {num1} & {num2} is: {num1*num2}")
# elif(opr==4):
#     print(f"Division of {num1} & {num2} is: {num1/num2}")
# else:
#     ("Enter a Valid Input")


# Write a program that takes a character as input and prints whether it is a vowel or a consonant.

# alph= (input("Enetr A Character: "))
# alph=alph.lower()

# if(alph=='a' or alph=='e' or alph=='i'  or alph=='o'  or alph=='u'  ):
#     print("The Character Is Vowel")
# else:
#     print("The Character Is Consonant")

# Check if a Year is a Leap Year

# Write a program that takes a year as input and prints whether it is a leap year or not

year=int(input("Enter Year"))
if( year%100 !=0 and year%4==0 )or (year%400==0):
    print("Leap Yaer")
else:
    print("Not A Leap Year")
