num=int(input("Enter The Number For Factorial>>>"))
factotial=1
for i in range(1,num+1):
    factotial *=i
    i+=1
print(f"Factorial of {num} is: {factotial}")