def p10(n):
    for i in range(n*2-1):
        if(i<=n):
            stars=i
        else:
            stars=n*2-i
        for j in range(stars):
            print("*", end="")
        for k in range(n-stars):
            print(end=" ")
        print()
p10(5)