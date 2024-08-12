def p8(n):
    for i in range(n):
        for z in range(i):
            print(" ", end="")
        for j in range(n*2-(2*i+1)):
            print("*", end="")
        for x in range(i):
            print(" ", end="")
        print()
p8(5)