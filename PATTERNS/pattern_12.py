def p12(n):
    space=n*n-1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        for k in range(space):
            print(" ", end="")
        space= space-(n+1)
        for l in range(i,0,-1):
            print(l, end=" ")
        print()
p12(3)

   
        