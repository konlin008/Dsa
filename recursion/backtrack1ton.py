def backtrack(i,n):
    if(i<1):
        return
    else:
        backtrack(i-1,n)
    print(i,end=" ")
    
n= int(input("Enter A Number : "))
backtrack(n,n)