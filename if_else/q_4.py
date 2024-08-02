# Check if a Year is a Leap Year

# Write a program that takes a year as input and prints whether it is a leap year or not

year=int(input("Enter Year"))
if( year%100 !=0 and year%4==0 )or (year%400==0):
    print("Leap Yaer")
else:
    print("Not A Leap Year")