num=int(input("Enter The Number>>"))
total=0
for i in range(1,num+1):
    if i % 2 ==0:
        total+= i
        print(f"{i}Sum of The Even Number Upto {num} is: {total}")
        i+=1
        
print(f"Sum of The Even Number Upto {num} is: {total}")