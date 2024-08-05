# Factorial of a Number
num= int(input("Please Enter The Number"))
i=1
fact=1
while i<num:
    fact *=i
    i+=1
print(f"Factorial of {num} is >> {fact}")