def p12(n):
    space=2*(n-1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        for sp in range(space):
            print(" ", end=" ")
        space -= 2
        for k in range(i,0,-1):
            print(k, end=" ")
        print()
        
num=int(input("Enter A Number: "))
p12(num)