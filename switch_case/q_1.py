# Check Positive, Negative, or Zero:
# Write a function that takes a number and uses match to return whether the number is "positive", "negative", or "zero".

num=int(input("Enter a number: "))
match num:
    case num if num<0:
        print("The Number Is Negetive")
    case num if num==0:
        print("The Number Is Zero")
    case num if num>0:
        print("The Number Is Positive")