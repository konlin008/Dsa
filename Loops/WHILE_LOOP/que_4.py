# Write a Python program that uses a while loop to reverse a given integer number.
num=123456
reversedd_num=0
last_digit=0

while num>0:
    last_digit=num%10
    reversedd_num= reversedd_num*10+last_digit
    print(reversedd_num)
    num= num//10