def p7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for z in range(i*2+1):
            print("*",end="")
        # for x in range(n-i-1):
        #     print(" ",end="")
        print()
def p8(n):
    for i in range(n):
        for z in range(i):
            print(" ", end="")
        for j in range(n*2-(2*i+1)):
            print("*", end="")
        for x in range(i):
            print(" ", end="")
        print()
p7(50) 
p8(50)